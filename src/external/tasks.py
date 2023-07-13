from django.conf import settings
from core.tasks import send_slack_message
import logging


logger = logging.getLogger(__name__)


def get_message(action=None):
    blocks = []
    if settings.DEBUG:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "これは開発テストです :computer:"
            }
        })
    if action == 'colorme_app_install':
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "ColorMeのアプリ登録がありました！ :art:"
            }
        })
    elif action == 'colorme_app_uninstall':
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "ColorMeのアプリがアンインストールされました！ :art:"
            }
        })
    return blocks


def send_notifications(action=None, context=None):
    # TO US
    try:
        if settings.CELERY_BROKER_URL:
            blocks = get_message(action)
            send_slack_message.delay("canal通知", blocks)
    except:
        logger.error('Could not send slack notification from external views. action: {}'.format(action))
