from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext


getcontext().prec = 10


prices = {
    '125 100 56 1000': {'unit_price': 118.5, 'plate_price': 0},
    '125 100 56 2000': {'unit_price': 73.0, 'plate_price': 0},
    '125 100 56 3000': {'unit_price': 59.5, 'plate_price': 0},

    '145 110 65 1000': {'unit_price': 119.5, 'plate_price': 0},
    '145 110 65 2000': {'unit_price': 75.7, 'plate_price': 0},
    '145 110 65 3000': {'unit_price': 60.5, 'plate_price': 0},

    '155 120 68 1000': {'unit_price': 123.5, 'plate_price': 0},
    '155 120 68 2000': {'unit_price': 81.2, 'plate_price': 0},
    '155 120 68 3000': {'unit_price': 63.2, 'plate_price': 0},
}


def get_unit_price(options, extra):
    # options
    height = options['size']['height']  # 高さ
    width = options['size']['width']  # 幅
    depth = options['size']['depth']  # 奥行き
    quantity = options['quantity']  # 注文数
    color_num = options['color_num']  # 色数
    key = "{} {} {} {}".format(height, width, depth, quantity)
    try:
        unit_price = prices[key]['unit_price']
    except KeyError:
        raise ValidationError("Invalid parameter")
    return Decimal(unit_price)


def get_plate_price(options):
    height = options['size']['height']
    width = options['size']['width']
    depth = options['size']['depth']  # 奥行き
    quantity = options['quantity']
    color_num = options['color_num']
    # SMALL LOT
    key = "{} {} {} {}".format(height, width, depth, quantity)
    try:
        return Decimal(prices[key]['plate_price'])
    except KeyError:
        raise ValidationError("Invalid parameter")


def get_mold_price(options):
    """木型代
    """
    return Decimal(0)


def get_shipping_price(options):
    return Decimal(0)
