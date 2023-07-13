from datetime import datetime
from django.conf import settings
from django.utils import timezone
from notices.models import NoticeCategory, Notice, NoticeRead, NoticeReminder
from core.tasks import send_slack_message
from utils.notification_tools import send_mail
import logging


logger = logging.getLogger(__name__)

def create_notice(item, action=None):
    # TODO: dry queries
    try:
        if action == 'resubmission_request':
            category = NoticeCategory.objects.get(name='data import reminder')
            past_log = NoticeRead.objects.filter(
                read_at=None,
                notices__category=category,
                notices__noticereminder__orderitem_id=item
            )
            if past_log.exists():past_log.update(read_at=datetime.now());
            NoticeReminder.objects.create(notice_ptr=None, orderitem=item, category_id=category.id)
        elif action == 'checked':
            previous_category = NoticeCategory.objects.get(name='data import reminder')
            past_log = NoticeRead.objects.filter(
                read_at=None,
                notices__category=previous_category,
                notices__noticereminder__orderitem_id=item
            )
            if past_log.exists():past_log.update(read_at=datetime.now());
            
            category = NoticeCategory.objects.get(name='notice about design comfirmation')
            NoticeReminder.objects.create(notice_ptr=None, orderitem=item, category_id=category.id)

            if item.order.transaction_set.filter(type='bank_transfer',is_captured=0).exists():
                bank_transfer_category = NoticeCategory.objects.get(name='bank transfer reminder')
                NoticeReminder.objects.create(notice_ptr=None, orderitem=item, category_id=bank_transfer_category.id)
        elif action == 'shipped':
            category = NoticeCategory.objects.get(name='notice about shipping')
            NoticeReminder.objects.create(notice_ptr=None, orderitem=item, category_id=category.id)
        elif action == 'delivered':
            NoticeRead.objects.filter(
               read_at=None,
               notices__noticereminder__orderitem_id=item
            ).update(read_at=datetime.now())
        else:
            pass
    except:
        logger.error('Failed to create a notice with {}.'.format(item.ref_code))


def send_notifications(item, action=None, context=None):
    # TO USER
    # TODO: MAKE THIS A TASK FOR WORKERS
    try:
        if action == 'resubmission_request':
            send_mail('email/design_resubmission_request', item.order.user.email, context)
        elif action == 'checked':
            send_mail('email/design_confirmation_request', item.order.user.email, context)
        elif action == 'confirmed':
            send_mail('email/design_confirm', item.order.user.email, context)
        elif action == 'printing':
            pass
        elif action == 'shipped':
            send_mail('email/delivery_shipping_confirmation', item.order.user.email, context)
        # elif action == 'delivered':
        #     send_mail('email/delivery_shipping_confirmation', item.order.user.email, context)
    except:
        logger.error('Could not send mail to {}.'.format(item.order.user.email))

def send_prompts(item, action=None, context=None):
    # TO USER
    # TODO: MAKE THIS A TASK FOR WORKERS
    try:
        if action == 'draftprompt':
            send_mail('email/draft_prompt', item.order.user.email, context)
        elif action == 'payprompt':
            send_mail('email/pay_prompt', item.order.user.email, context)
    except:
        logger.error('Could not send mail to {}.'.format(item.order.user.email))
