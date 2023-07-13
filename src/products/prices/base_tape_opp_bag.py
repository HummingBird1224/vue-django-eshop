from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext
from math import ceil, floor


getcontext().prec = 10

prices = {
    '110 155 1 100': {'unit_price': 90.7, 'plate_price': 14000},
    '110 155 1 200': {'unit_price': 71.9, 'plate_price': 14000},
    '110 155 1 300': {'unit_price': 45.3, 'plate_price': 14000},
    '110 155 1 500': {'unit_price': 34, 'plate_price': 6000},
    '110 155 1 700': {'unit_price': 27.2, 'plate_price': 6000},
    '110 155 1 1000': {'unit_price': 15.9, 'plate_price': 6000},
    '110 155 1 1500': {'unit_price': 12.5, 'plate_price': 6000},
    '110 155 1 2000': {'unit_price': 10.7, 'plate_price': 6000},
    '110 155 1 2500': {'unit_price': 9.9, 'plate_price': 6000},
    '110 155 1 3000': {'unit_price': 9.4, 'plate_price': 6000},

    '160 220 1 100': {'unit_price': 95.7, 'plate_price': 14000},
    '160 220 1 200': {'unit_price': 76.9, 'plate_price': 14000},
    '160 220 1 300': {'unit_price': 70.7, 'plate_price': 14000},
    '160 220 1 500': {'unit_price': 55.5, 'plate_price': 6000},
    '160 220 1 700': {'unit_price': 44.4, 'plate_price': 6000},
    '160 220 1 1000': {'unit_price': 26.3, 'plate_price': 6000},
    '160 220 1 1500': {'unit_price': 19.7, 'plate_price': 6000},
    '160 220 1 2000': {'unit_price': 16.3, 'plate_price': 6000},
    '160 220 1 2500': {'unit_price': 14.7, 'plate_price': 6000},
    '160 220 1 3000': {'unit_price': 13.2, 'plate_price': 6000},

    '225 305 1 100': {'unit_price': 98.2, 'plate_price': 14000},
    '225 305 1 200': {'unit_price': 79.4, 'plate_price': 14000},
    '225 305 1 300': {'unit_price': 73.2, 'plate_price': 14000},
    '225 305 1 500': {'unit_price': 58.7, 'plate_price': 6000},
    '225 305 1 700': {'unit_price': 46.9, 'plate_price': 6000},
    '225 305 1 1000': {'unit_price': 28.8, 'plate_price': 6000},
    '225 305 1 1500': {'unit_price': 21.9, 'plate_price': 6000},
    '225 305 1 2000': {'unit_price': 18.8, 'plate_price': 6000},
    '225 305 1 2500': {'unit_price': 17, 'plate_price': 6000},
    '225 305 1 3000': {'unit_price': 15.7, 'plate_price': 6000},

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

    # 下記注文数の価格設定がないと画面表示がエラーになるため追加
    '270 382 1 200': {'unit_price': 132, 'plate_price': 15000},
    '270 382 1 300': {'unit_price': 54.7, 'plate_price': 6000},
    '270 382 1 700': {'unit_price': 34.7, 'plate_price': 6000},
    '270 382 1 2500': {'unit_price': 23.4, 'plate_price': 6000},
    '290 382 1 200': {'unit_price': 132, 'plate_price': 15000},
    '290 382 1 300': {'unit_price': 56.7, 'plate_price': 6000},
    '290 382 1 700': {'unit_price': 36.7, 'plate_price': 6000},
    '290 382 1 2500': {'unit_price': 25.4, 'plate_price': 6000},

    '110 155 2 100': {'unit_price': 246.9, 'plate_price': 5500},
    '110 155 2 200': {'unit_price': 123.5, 'plate_price': 5500},
    '110 155 2 300': {'unit_price': 82.3, 'plate_price': 5500},
    '110 155 2 500': {'unit_price': 61.8, 'plate_price': 5500},
    '110 155 2 700': {'unit_price': 49.4, 'plate_price': 5500},
    '110 155 2 1000': {'unit_price': 27.5, 'plate_price': 5500},
    '110 155 2 1500': {'unit_price': 20.7, 'plate_price': 5500},
    '110 155 2 2000': {'unit_price': 16.9, 'plate_price': 5500},
    '110 155 2 2500': {'unit_price': 15.3, 'plate_price': 5500},
    '110 155 2 3000': {'unit_price': 13.8, 'plate_price': 5500},

    '160 220 2 100': {'unit_price': 312.5, 'plate_price': 5500},
    '160 220 2 200': {'unit_price': 156.3, 'plate_price': 5500},
    '160 220 2 300': {'unit_price': 104.2, 'plate_price': 5500},
    '160 220 2 500': {'unit_price': 78.2, 'plate_price': 5500},
    '160 220 2 700': {'unit_price': 62.5, 'plate_price': 5500},
    '160 220 2 1000': {'unit_price': 35.7, 'plate_price': 5500},
    '160 220 2 1500': {'unit_price': 26.9, 'plate_price': 5500},
    '160 220 2 2000': {'unit_price': 21.9, 'plate_price': 5500},
    '160 220 2 2500': {'unit_price': 19.7, 'plate_price': 5500},
    '160 220 2 3000': {'unit_price': 17.5, 'plate_price': 5500},

    '225 305 2 100': {'unit_price': 321.9, 'plate_price': 5500},
    '225 305 2 200': {'unit_price': 161, 'plate_price': 5500},
    '225 305 2 300': {'unit_price': 107.3, 'plate_price': 5500},
    '225 305 2 500': {'unit_price': 80.5, 'plate_price': 5500},
    '225 305 2 700': {'unit_price': 64.4, 'plate_price': 5500},
    '225 305 2 1000': {'unit_price': 37.5, 'plate_price': 5500},
    '225 305 2 1500': {'unit_price': 29.4, 'plate_price': 5500},
    '225 305 2 2000': {'unit_price': 24.4, 'plate_price': 5500},
    '225 305 2 2500': {'unit_price': 22, 'plate_price': 5500},
    '225 305 2 3000': {'unit_price': 20, 'plate_price': 5500},
}


def get_unit_price(options, extra):
    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    quantity = options['quantity']  # 注文数
    color_num = options['color_num']  # 色数
    key = "{} {} {} {}".format(width, height, color_num, quantity)
    try:
        unit_price = prices[key]['unit_price']
    except KeyError:
        raise ValidationError("Invalid parameter")
    return Decimal(unit_price)


def get_plate_price(options):
    """版代
    """
    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    quantity = options['quantity']  # 注文数
    color_num = options['color_num']  # 色数
    key = "{} {} {} {}".format(width, height, color_num, quantity)
    try:
        plate_price = prices[key]['plate_price']
    except KeyError:
        raise ValidationError("Invalid parameter")
    return Decimal(plate_price)


def get_mold_price(options):
    """木型代
    """
    return 0


def get_shipping_price(options):
    return Decimal(0)
