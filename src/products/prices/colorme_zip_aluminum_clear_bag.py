from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext


getcontext().prec = 10


prices = {
    '100 140 100': {'unit_price': 101.8, 'plate_price': 14000},
    '100 140 200': {'unit_price': 80.5, 'plate_price': 14000},
    '100 140 300': {'unit_price': 73.5, 'plate_price': 14000},
    '100 140 400': {'unit_price': 70, 'plate_price': 14000},
    '100 140 500': {'unit_price': 62.1, 'plate_price': 14000},
    '100 140 600': {'unit_price': 60.5, 'plate_price': 14000},
    '100 140 700': {'unit_price': 51.1, 'plate_price': 14000},
    '100 140 800': {'unit_price': 46.7, 'plate_price': 14000},
    '100 140 900': {'unit_price': 42.9, 'plate_price': 14000},
    '100 140 1000': {'unit_price': 39.7, 'plate_price': 14000},
    '100 140 1500': {'unit_price': 37.9, 'plate_price': 14000},
    '100 140 2000': {'unit_price': 35.7, 'plate_price': 14000},

    '120 170 100': {'unit_price': 105.2, 'plate_price': 14000},
    '120 170 200': {'unit_price': 83.9, 'plate_price': 14000},
    '120 170 300': {'unit_price': 76.9, 'plate_price': 14000},
    '120 170 400': {'unit_price': 73.3, 'plate_price': 14000},
    '120 170 500': {'unit_price': 65.5, 'plate_price': 14000},
    '120 170 600': {'unit_price': 63.9, 'plate_price': 14000},
    '120 170 700': {'unit_price': 54.5, 'plate_price': 14000},
    '120 170 800': {'unit_price': 50.1, 'plate_price': 14000},
    '120 170 900': {'unit_price': 46.2, 'plate_price': 14000},
    '120 170 1000': {'unit_price': 43, 'plate_price': 14000},
    '120 170 1500': {'unit_price': 41.3, 'plate_price': 14000},
    '120 170 2000': {'unit_price': 39.1, 'plate_price': 14000},

    '140 200 100': {'unit_price': 114, 'plate_price': 14000},
    '140 200 200': {'unit_price': 92.8, 'plate_price': 14000},
    '140 200 300': {'unit_price': 85.7, 'plate_price': 14000},
    '140 200 400': {'unit_price': 82.2, 'plate_price': 14000},
    '140 200 500': {'unit_price': 75.6, 'plate_price': 14000},
    '140 200 600': {'unit_price': 74, 'plate_price': 14000},
    '140 200 700': {'unit_price': 63.4, 'plate_price': 14000},
    '140 200 800': {'unit_price': 58.9, 'plate_price': 14000},
    '140 200 900': {'unit_price': 55.1, 'plate_price': 14000},
    '140 200 1000': {'unit_price': 51.9, 'plate_price': 14000},
    '140 200 1500': {'unit_price': 50.2, 'plate_price': 14000},
    '140 200 2000': {'unit_price': 48, 'plate_price': 14000},

    '170 240 100': {'unit_price': 123.4, 'plate_price': 14000},
    '170 240 200': {'unit_price': 102.2, 'plate_price': 14000},
    '170 240 300': {'unit_price': 95.1, 'plate_price': 14000},
    '170 240 400': {'unit_price': 91.6, 'plate_price': 14000},
    '170 240 500': {'unit_price': 85, 'plate_price': 14000},
    '170 240 600': {'unit_price': 83.4, 'plate_price': 14000},
    '170 240 700': {'unit_price': 72.7, 'plate_price': 14000},
    '170 240 800': {'unit_price': 68.3, 'plate_price': 14000},
    '170 240 900': {'unit_price': 64.5, 'plate_price': 14000},
    '170 240 1000': {'unit_price': 61.3, 'plate_price': 14000},
    '170 240 1500': {'unit_price': 59.5, 'plate_price': 14000},
    '170 240 2000': {'unit_price': 57.4, 'plate_price': 14000},
}


def get_unit_price(options, extra):
    # options
    height = options['size']['height']  # 高さ
    width = options['size']['width']  # 幅
    quantity = options['quantity']  # 注文数
    color_num = options['color_num']  # 色数
    key = "{} {} {}".format(width, height, quantity)
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
