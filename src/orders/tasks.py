from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings
from .models import Order, OrderItem
from core.tasks import send_slack_message
from utils.notification_tools import send_mail
from datetime import datetime, timedelta
import logging


logger = logging.getLogger(__name__)


@shared_task
def cancel_expired_order_items():
    # TODO: cancel expired orders by PAYJP_EXPITY_DAYS.
    now = datetime.now()
    for oi in OrderItem.objects.filter(payment='pending'):
        if oi.design.state != 'under_check':
            delta = now - oi.design.updated_at
            if delta.days >= settings.PAYMENT_EXPIRY_DAYS:
                oi.cancel_atomic()


def get_message(item, action=None):
    blocks = []
    if settings.DEBUG:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "これは開発テストです :computer:"
            }
        })
    title = ""
    if action == 'upload':
        title = "データの入稿がありました！ :car:"
    elif action == 'confirm':
        title = "データが承認されました！ :tada:"
    elif action == 'cancel':
        title = "注文のキャンセルがありました！ :face_vomiting:"
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": title
        }
    })
    blocks.append({
            "type": "divider"
    })
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "発注者：{}様\nメールアドレス：{}\n注文番号：{}".format(
                item.order.user.get_fullname(),
                item.order.user.email,
                item.ref_code,
            )
        }
    })
    blocks.append({
            "type": "divider"
    })
    option_text = ""
    for key, val in item.render_extra_info().items():
        option_text += ("\t" + key + "：" + val + "\n")
    price_text = "\n価格：\n"
    price_text += "\t商品代：{}円\n\t単価：{}円\n\t版代：{}円\n\t木型代：{}円\n\t配送料：{}円\n\t小計：{}円\n\t消費税：{}円\n\t合計：{}円\n".format(
        item.product_total,
        item.unit_price,
        item.plate_price,
        item.mold_price,
        item.shipping_price,
        item.subtotal,
        item.tax,
        item.total,
    )
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":pushpin: 商品名：{}\n注文数：{}\nサイズ：{}\nオプション：\n".format(
                item.product_name,
                item.quantity,
                item.size_str,
            ) + option_text + price_text
        }
    })
    blocks.append({
        "type": "divider"
    })
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "納品先：{}様\n郵便番号：{}\n宛先：{}\n電話番号：{}\n決済方法：{}\n".format(
                item.order.delivery_address.get_full_name(),
                item.order.delivery_address.postal_code,
                item.order.delivery_address.get_full_address(),
                item.order.delivery_address.tel,
                item.order.get_transaction().get_type_display()
            )
        }
    })
    if action == 'upload':
        blocks.append({
            "type": "divider"
        })
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "入稿データ:lower_left_crayon:\n<{}>".format(
                    item.design.data.url
                )
            }
        })
    return blocks


def send_notifications(item, action=None, context=None):
    # TO USERS
    # TODO: MAKE THIS A CELERY TASK
    # TODO: MAKE ACTION CONSTANTS
    trans = item.order.get_transaction()
    try:
        if action == 'upload':
            send_mail('orders/email/design_uploaded', item.order.user.email, context)
        elif action == 'cancel':
            send_mail('orders/email/cancel', item.order.user.email, context)
        elif action == 'confirm':
            send_mail('orders/email/design_confirm', item.order.user.email, context)
    except Exception as e:
        logger.error(e)
        logger.error('Could not send mail to {}.'.format(item.order.user.email))


    # TO US
    try:
        if settings.CELERY_BROKER_URL:
            blocks = get_message(item, action)
            send_slack_message.delay("canal通知", blocks)
    except Exception as e:
        logger.error(e)
        logger.error('Could not send slack notification. order ref: {}'.format(item.ref_code))

