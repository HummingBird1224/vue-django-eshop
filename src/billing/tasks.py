from django.conf import settings
from core.tasks import send_slack_message
from utils.notification_tools import send_mail
import logging


logger = logging.getLogger(__name__)


def get_message(order, action=None):
    blocks = []
    if settings.DEBUG:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*これは開発テストです* :computer:"
            }
        })
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "新規の注文がきました！ :moneybag:"
        }
    })
    if order.extra_info.get('has_reordered_item', False):
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "再注文商品が含まれます！"
            }
        })
    blocks.append({
            "type": "divider"
    })
    blocks.append({
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "発注者：{}様\nメールアドレス：{}\n注文番号：{}\n合計額：{}円".format(
                order.user.get_fullname(),
                order.user.email,
                order.ref_code,
                order.total,
            )
        }
    })
    blocks.append({
            "type": "divider"
    })
    for item in order.get_order_items():
        option_text = ""
        for key, val in item.render_extra_info().items():
            option_text += ("\t*" + key + "：" + val + "*\n")
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
        material = item.extra_info.get('surface_material')
        if material in ['white', 'normal']:
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*※{}です*".format("白ダンボール" if material == 'white' else "クラフトダンボール")
                }
            })
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
                order.delivery_address.get_full_name(),
                order.delivery_address.postal_code,
                order.delivery_address.get_full_address(),
                order.delivery_address.tel,
                order.get_transaction().get_type_display()
            )
        }
    })
    return blocks


def send_notifications(order, action=None, context=None):
    # TO USER
    # TODO: MAKE THIS A TASK FOR WORKERS
    trans = order.get_transaction()
    try:
        if trans.type == 'bank_transfer':
            send_mail('email/order_created_bank_transfer', order.user.email, context)
        elif trans.type == 'credit_card':
            send_mail('email/order_created', order.user.email, context)
        else:
            send_mail('email/order_created', order.user.email, context)
    except Exception as e:
        logger.error(e)
        logger.error('Could not send mail to {}.'.format(order.user.email))

    # TO US
    try:
        if settings.CELERY_BROKER_URL:
            blocks = get_message(order, action)
            send_slack_message.delay("canal通知", blocks)
    except Exception as e:
        logger.error(e)
        logger.error('Could not send slack notification. order ref: {}'.format(order.ref_code))

