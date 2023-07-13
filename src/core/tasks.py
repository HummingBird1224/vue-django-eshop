from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings
import slack


slack_token = settings.SLACK_KEY
sc = slack.WebClient(token=slack_token)


@shared_task
def send_slack_message(channel, blocks):
    sc.chat_postMessage(
        channel=channel,
        blocks=blocks
    )
