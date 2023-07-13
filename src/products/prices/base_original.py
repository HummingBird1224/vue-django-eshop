from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext


getcontext().prec = 10

prices = {
    '300 420 50': {'unit_price': 0, 'shipping_price': 198},
    '300 420 100': {'unit_price': 18.5, 'shipping_price': 198},
    '300 420 200': {'unit_price': 18.2, 'shipping_price': 396},
    '300 420 300': {'unit_price': 17.9, 'shipping_price': 594},
    '300 420 400': {'unit_price': 17.6, 'shipping_price': 910},
    '300 420 500': {'unit_price': 17.0, 'shipping_price': 910},

    '150 210 50': {'unit_price': 0, 'shipping_price': 198},
    '150 210 100': {'unit_price': 5.7, 'shipping_price': 198},
    '150 210 200': {'unit_price': 5.5, 'shipping_price': 198},
    '150 210 300': {'unit_price': 5.3, 'shipping_price': 396},
    '150 210 400': {'unit_price': 5.1, 'shipping_price': 396},
    '150 210 500': {'unit_price': 4.7, 'shipping_price': 690},

    '105 150 50': {'unit_price': 0, 'shipping_price': 198},
    '105 150 100': {'unit_price': 4.4, 'shipping_price': 198},
    '105 150 200': {'unit_price': 4.3, 'shipping_price': 198},
    '105 150 300': {'unit_price': 4.2, 'shipping_price': 198},
    '105 150 400': {'unit_price': 3.8, 'shipping_price': 198},
    '105 150 500': {'unit_price': 3.5, 'shipping_price': 396},
}


def get_unit_price(options, extra):
    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    quantity = options['quantity']  # 注文数
    key = "{} {} {}".format(width, height, quantity)
    try:
        unit_price = prices[key]['unit_price']
    except KeyError:
        raise ValidationError("Invalid parameter")
    return Decimal(unit_price)


def get_plate_price(options):
    """版代
    """
    return 0


def get_mold_price(options):
    """木型代
    """
    return 0


def get_shipping_price(options):
    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    quantity = options['quantity']  # 注文数
    key = "{} {} {}".format(width, height, quantity)
    try:
        shipping_price = prices[key]['shipping_price']
    except KeyError:
        raise ValidationError("Invalid parameter")
    return Decimal(shipping_price)
