from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext


getcontext().prec = 10


prices = {
    # width height color_num lot
    '220 310 1 500': {'unit_price': 103.8, 'plate_price': 30000},
    '220 310 1 1000': {'unit_price': 56.3, 'plate_price': 30000},
    '220 310 1 1500': {'unit_price': 40, 'plate_price': 30000},
    '220 310 1 2000': {'unit_price': 33.8, 'plate_price': 30000},
    '220 310 1 2500': {'unit_price': 28.8, 'plate_price': 30000},
    '220 310 1 3000': {'unit_price': 25, 'plate_price': 30000},

    '250 340 1 500': {'unit_price': 107.5, 'plate_price': 35000},
    '250 340 1 1000': {'unit_price': 58.8, 'plate_price': 35000},
    '250 340 1 1500': {'unit_price': 42.5, 'plate_price': 35000},
    '250 340 1 2000': {'unit_price': 36.3, 'plate_price': 35000},
    '250 340 1 2500': {'unit_price': 31.3, 'plate_price': 35000},
    '250 340 1 3000': {'unit_price': 27.5, 'plate_price': 35000},
}


def get_unit_price(options, extra):
    # options
    height = options['size']['height']  # 高さ
    width = options['size']['width']  # 幅
    quantity = options['quantity']  # 注文数
    color_num = options['color_num']  # 色数
    key = "{} {} {} {}".format(width, height, color_num, quantity)
    try:
        unit_price = prices[key]['unit_price']
    except KeyError:
        raise ValidationError("Invalid parameter")
    return Decimal(unit_price)


def get_plate_price(options):
    height = options['size']['height']
    width = options['size']['width']
    color_num = options['color_num']
    quantity = options['quantity']

    # SMALL LOT
    key = "{} {} {} {}".format(width, height, color_num, quantity)
    if key in prices:
        return Decimal(prices[key]['plate_price'])
    else:
        raise ValidationError("Invalid size or color num for small lot.")


def get_mold_price(options):
    """木型代
    """
    return Decimal(0)


def get_shipping_price(options):
    return Decimal(0)
