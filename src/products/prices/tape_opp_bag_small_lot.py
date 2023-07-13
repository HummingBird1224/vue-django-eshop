from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext


getcontext().prec = 10


prices = {
    '110 155 1 100': {'unit_price': 96.7, 'plate_price': 14000},
    '110 155 1 200': {'unit_price': 76.7, 'plate_price': 14000},
    '110 155 1 300': {'unit_price': 48.3, 'plate_price': 14000},
    '110 155 1 500': {'unit_price': 29, 'plate_price': 6000},
    '110 155 1 700': {'unit_price': 22, 'plate_price': 6000},
    '110 155 1 1000': {'unit_price': 17, 'plate_price': 6000},
    '110 155 1 1500': {'unit_price': 13.4, 'plate_price': 6000},
    '110 155 1 2000': {'unit_price': 11.4, 'plate_price': 6000},
    '110 155 1 2500': {'unit_price': 10.6, 'plate_price': 6000},
    '110 155 1 3000': {'unit_price': 10, 'plate_price': 6000},
    '160 220 1 100': {'unit_price': 102, 'plate_price': 14000},
    '160 220 1 200': {'unit_price': 82, 'plate_price': 14000},
    '160 220 1 300': {'unit_price': 75.4, 'plate_price': 14000},
    '160 220 1 500': {'unit_price': 47.4, 'plate_price': 6000},
    '160 220 1 700': {'unit_price': 36.7, 'plate_price': 6000},
    '160 220 1 1000': {'unit_price': 28, 'plate_price': 6000},
    '160 220 1 1500': {'unit_price': 21, 'plate_price': 6000},
    '160 220 1 2000': {'unit_price': 17.4, 'plate_price': 6000},
    '160 220 1 2500': {'unit_price': 15.6, 'plate_price': 6000},
    '160 220 1 3000': {'unit_price': 14, 'plate_price': 6000},
    '225 305 1 100': {'unit_price': 104.7, 'plate_price': 14000},
    '225 305 1 200': {'unit_price': 84.7, 'plate_price': 14000},
    '225 305 1 300': {'unit_price': 78, 'plate_price': 14000},
    '225 305 1 500': {'unit_price': 50, 'plate_price': 6000},
    '225 305 1 700': {'unit_price': 38.7, 'plate_price': 6000},
    '225 305 1 1000': {'unit_price': 30.7, 'plate_price': 6000},
    '225 305 1 1500': {'unit_price': 23.4, 'plate_price': 6000},
    '225 305 1 2000': {'unit_price': 20, 'plate_price': 6000},
    '225 305 1 2500': {'unit_price': 18.2, 'plate_price': 6000},
    '225 305 1 3000': {'unit_price': 16.7, 'plate_price': 6000},

    '270 382 1 100': {'unit_price': 132, 'plate_price': 15000},
    '270 382 1 500': {'unit_price': 54.7, 'plate_price': 6000},
    '270 382 1 1000': {'unit_price': 34.7, 'plate_price': 6000},
    '270 382 1 1500': {'unit_price': 27.4, 'plate_price': 6000},
    '270 382 1 2000': {'unit_price': 23.4, 'plate_price': 6000},
    '270 382 1 3000': {'unit_price': 20, 'plate_price': 6000},
    '290 382 1 100': {'unit_price': 132, 'plate_price': 15000},
    '290 382 1 500': {'unit_price': 56.7, 'plate_price': 6000},
    '290 382 1 1000': {'unit_price': 36.7, 'plate_price': 6000},
    '290 382 1 1500': {'unit_price': 29.4, 'plate_price': 6000},
    '290 382 1 2000': {'unit_price': 25.4, 'plate_price': 6000},
    '290 382 1 3000': {'unit_price': 22, 'plate_price': 6000},

    '110 155 2 100': {'unit_price': 96.7, 'plate_price': 14000},
    '110 155 2 200': {'unit_price': 76.7, 'plate_price': 14000},
    '110 155 2 300': {'unit_price': 48.3, 'plate_price': 14000},
    '110 155 2 500': {'unit_price': 29, 'plate_price': 6000},
    '110 155 2 700': {'unit_price': 22, 'plate_price': 6000},
    '110 155 2 1000': {'unit_price': 17, 'plate_price': 6000},
    '110 155 2 1500': {'unit_price': 13.4, 'plate_price': 6000},
    '110 155 2 2000': {'unit_price': 11.4, 'plate_price': 6000},
    '110 155 2 2500': {'unit_price': 10.6, 'plate_price': 6000},
    '110 155 2 3000': {'unit_price': 10, 'plate_price': 6000},
    '160 220 2 100': {'unit_price': 102, 'plate_price': 14000},
    '160 220 2 200': {'unit_price': 82, 'plate_price': 14000},
    '160 220 2 300': {'unit_price': 75.4, 'plate_price': 14000},
    '160 220 2 500': {'unit_price': 47.4, 'plate_price': 6000},
    '160 220 2 700': {'unit_price': 36.7, 'plate_price': 6000},
    '160 220 2 1000': {'unit_price': 28, 'plate_price': 6000},
    '160 220 2 1500': {'unit_price': 21, 'plate_price': 6000},
    '160 220 2 2000': {'unit_price': 17.4, 'plate_price': 6000},
    '160 220 2 2500': {'unit_price': 15.6, 'plate_price': 6000},
    '160 220 2 3000': {'unit_price': 14, 'plate_price': 6000},
    '225 305 2 100': {'unit_price': 104.7, 'plate_price': 14000},
    '225 305 2 200': {'unit_price': 84.7, 'plate_price': 14000},
    '225 305 2 300': {'unit_price': 78, 'plate_price': 14000},
    '225 305 2 500': {'unit_price': 50, 'plate_price': 6000},
    '225 305 2 700': {'unit_price': 38.7, 'plate_price': 6000},
    '225 305 2 1000': {'unit_price': 30.7, 'plate_price': 6000},
    '225 305 2 1500': {'unit_price': 23.4, 'plate_price': 6000},
    '225 305 2 2000': {'unit_price': 20, 'plate_price': 6000},
    '225 305 2 2500': {'unit_price': 18.2, 'plate_price': 6000},
    '225 305 2 3000': {'unit_price': 16.7, 'plate_price': 6000},
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
