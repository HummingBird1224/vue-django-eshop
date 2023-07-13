from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext


getcontext().prec = 10


prices = {
    '100 125 1000': {'unit_price': 107.5, 'plate_price': 0},
    '100 125 2000': {'unit_price': 66.3, 'plate_price': 0},
    '100 125 3000': {'unit_price': 53.8, 'plate_price': 0},

    '120 155 1000': {'unit_price': 112.5, 'plate_price': 0},
    '120 155 2000': {'unit_price': 72.5, 'plate_price': 0},
    '120 155 3000': {'unit_price': 57.5, 'plate_price': 0},

    '130 165 1000': {'unit_price': 117.5, 'plate_price': 0},
    '130 165 2000': {'unit_price': 75, 'plate_price': 0},
    '130 165 3000': {'unit_price': 62.5, 'plate_price': 0},
}


def get_unit_price(options, extra):
    # options
    height = options['size']['height']  # 高さ
    width = options['size']['width']  # 幅
    quantity = options['quantity']  # 注文数
    key = "{} {} {}".format(width, height, quantity)
    try:
        unit_price = prices[key]['unit_price']
    except KeyError:
        raise ValidationError("Invalid parameter")
    return Decimal(unit_price)


def get_plate_price(options):
    height = options['size']['height']
    width = options['size']['width']
    quantity = options['quantity']

    # SMALL LOT
    key = "{} {} {}".format(width, height, quantity)
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
