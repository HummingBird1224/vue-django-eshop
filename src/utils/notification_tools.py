from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
import logging


######################################
# Email
######################################
def get_from_email():
    """送り主のメールアドレス
    デフォはsettingsに
    """
    return settings.DEFAULT_FROM_EMAIL


def render_mail(template_prefix, email, context):
    """メールの文面のレンダリング (.txt or .html)
    """
    subject = render_to_string('{0}_subject.txt'.format(template_prefix),
                               context)
    subject = " ".join(subject.splitlines()).strip()

    from_email = get_from_email()

    bodies = {}
    for ext in ['html', 'txt']:
        try:
            template_name = '{0}_message.{1}'.format(template_prefix, ext)
            bodies[ext] = render_to_string(template_name,
                                           context).strip()
        except TemplateDoesNotExist:
            if ext == 'txt' and not bodies:
                # We need at least one body
                raise
    if 'txt' in bodies:
        msg = EmailMultiAlternatives(subject,
                                     bodies['txt'],
                                     from_email,
                                     [email])
        if 'html' in bodies:
            msg.attach_alternative(bodies['html'], 'text/html')
    else:
        msg = EmailMessage(subject,
                           bodies['html'],
                           from_email,
                           [email])
        msg.content_subtype = 'html'  # Main content is now text/html
    return msg


def send_mail(template_prefix, email, context):
    """メール送信
    """
    msg = render_mail(template_prefix, email, context)
    msg.send()


######################################
# Slack
######################################
