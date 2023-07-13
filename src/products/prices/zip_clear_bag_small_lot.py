from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext


getcontext().prec = 10


prices = {
    '100 140 1 100': {'unit_price': 97.5, 'plate_price': 14000},
    '100 140 1 200': {'unit_price': 77.5, 'plate_price': 14000},
    '100 140 1 300': {'unit_price': 70.8, 'plate_price': 14000},
    '100 140 1 500': {'unit_price': 60.2, 'plate_price': 14000},
    '100 140 1 700': {'unit_price': 47.5, 'plate_price': 14000},
    '100 140 1 1000': {'unit_price': 27.2, 'plate_price': 7000},
    '100 140 1 1500': {'unit_price': 27.2, 'plate_price': 7000},
    '100 140 1 2000': {'unit_price': 27.2, 'plate_price': 7000},
    '100 140 1 2500': {'unit_price': 27.2, 'plate_price': 7000},
    '100 140 1 3000': {'unit_price': 26.3, 'plate_price': 7000},
    '120 170 1 100': {'unit_price': 98.7, 'plate_price': 14000},
    '120 170 1 200': {'unit_price': 78.7, 'plate_price': 14000},
    '120 170 1 300': {'unit_price': 72, 'plate_price': 14000},
    '120 170 1 500': {'unit_price': 61.4, 'plate_price': 14000},
    '120 170 1 700': {'unit_price': 48.7, 'plate_price': 14000},
    '120 170 1 1000': {'unit_price': 28.4, 'plate_price': 7000},
    '120 170 1 1500': {'unit_price': 28.4, 'plate_price': 7000},
    '120 170 1 2000': {'unit_price': 28.4, 'plate_price': 7000},
    '120 170 1 2500': {'unit_price': 28.4, 'plate_price': 7000},
    '120 170 1 3000': {'unit_price': 27.5, 'plate_price': 7000},
    '170 240 1 100': {'unit_price': 102.3, 'plate_price': 14000},
    '170 240 1 200': {'unit_price': 82.3, 'plate_price': 14000},
    '170 240 1 300': {'unit_price': 75.6, 'plate_price': 14000},
    '170 240 1 500': {'unit_price': 65, 'plate_price': 14000},
    '170 240 1 700': {'unit_price': 52.3, 'plate_price': 14000},
    '170 240 1 1000': {'unit_price': 32.8, 'plate_price': 7000},
    '170 240 1 1500': {'unit_price': 32.8, 'plate_price': 7000},
    '170 240 1 2000': {'unit_price': 32.8, 'plate_price': 7000},
    '170 240 1 2500': {'unit_price': 32.8, 'plate_price': 7000},
    '170 240 1 3000': {'unit_price': 31.9, 'plate_price': 7000},
    '240 340 1 100': {'unit_price': 107.4, 'plate_price': 14000},
    '240 340 1 200': {'unit_price': 87.4, 'plate_price': 14000},
    '240 340 1 300': {'unit_price': 80.7, 'plate_price': 14000},
    '240 340 1 500': {'unit_price': 70, 'plate_price': 14000},
    '240 340 1 700': {'unit_price': 57.4, 'plate_price': 14000},
    '240 340 1 1000': {'unit_price': 37.4, 'plate_price': 7000},
    '240 340 1 1500': {'unit_price': 37.4, 'plate_price': 7000},
    '240 340 1 2000': {'unit_price': 37.4, 'plate_price': 7000},
    '240 340 1 2500': {'unit_price': 37.4, 'plate_price': 7000},
    '240 340 1 3000': {'unit_price': 36.4, 'plate_price': 7000},
    '340 480 1 100': {'unit_price': 122.8, 'plate_price': 14000},
    '340 480 1 200': {'unit_price': 102.8, 'plate_price': 14000},
    '340 480 1 300': {'unit_price': 96.2, 'plate_price': 14000},
    '340 480 1 500': {'unit_price': 84.2, 'plate_price': 14000},
    '340 480 1 700': {'unit_price': 72.8, 'plate_price': 14000},
    '340 480 1 1000': {'unit_price': 60.8, 'plate_price': 14000},
    '340 480 1 1500': {'unit_price': 60, 'plate_price': 14000},
    '340 480 1 2000': {'unit_price': 57.8, 'plate_price': 14000},
    '340 480 1 2500': {'unit_price': 57.6, 'plate_price': 14000},
    '340 480 1 3000': {'unit_price': 57.3, 'plate_price': 14000},
}


def get_unit_price(options, extra):
    # options
    height = options['size']['height']  # 高さ
    width = options['size']['width']  # 幅
    quantity = options['quantity']  # 注文数
    color_num = options['color_num']  # 色数
    key = "{} {} {} {}".format(width, height, color_num, quantity)
    try:
        return Decimal(prices[key]['unit_price'])
    except KeyError:
        raise ValidationError("Invalid parameter")


def get_plate_price(options):
    height = options['size']['height']
    width = options['size']['width']
    quantity = options['quantity']
    color_num = options['color_num']
    key = "{} {} {} {}".format(width, height, color_num, quantity)
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
