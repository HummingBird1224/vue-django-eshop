from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext
from math import ceil


getcontext().prec = 10


prices = {
    # width depth height print_area_num design_num quantity
    '235 176 25 1 1 50': {'unit_price': 65.0, 'plate_price': 13000},
    '235 176 25 1 1 100': {'unit_price': 60.7, 'plate_price': 13000},
    '235 176 25 1 1 200': {'unit_price': 57.2, 'plate_price': 13000},
    '235 176 25 1 1 300': {'unit_price': 56.1, 'plate_price': 13000},
    '310 228 25 1 1 50': {'unit_price': 85.0, 'plate_price': 13000},
    '310 228 25 1 1 100': {'unit_price': 73.2, 'plate_price': 13000},
    '310 228 25 1 1 200': {'unit_price': 62.2, 'plate_price': 13000},
    '310 228 25 1 1 300': {'unit_price': 61.1, 'plate_price': 13000},
    '335 248 30 1 1 50': {'unit_price': 95.0, 'plate_price': 13000},
    '335 248 30 1 1 100': {'unit_price': 79.4, 'plate_price': 13000},
    '335 248 30 1 1 200': {'unit_price': 71.0, 'plate_price': 13000},
    '335 248 30 1 1 300': {'unit_price': 69.8, 'plate_price': 13000},

    '235 176 25 2 1 50': {'unit_price': 83.8, 'plate_price': 13000},
    '235 176 25 2 1 100': {'unit_price': 79.4, 'plate_price': 13000},
    '235 176 25 2 1 200': {'unit_price': 76.0, 'plate_price': 13000},
    '235 176 25 2 1 300': {'unit_price': 74.8, 'plate_price': 13000},
    '310 228 25 2 1 50': {'unit_price': 103.8, 'plate_price': 13000},
    '310 228 25 2 1 100': {'unit_price': 91.9, 'plate_price': 13000},
    '310 228 25 2 1 200': {'unit_price': 81.0, 'plate_price': 13000},
    '310 228 25 2 1 300': {'unit_price': 79.8, 'plate_price': 13000},
    '335 248 30 2 1 50': {'unit_price': 113.8, 'plate_price': 13000},
    '335 248 30 2 1 100': {'unit_price': 98.2, 'plate_price': 13000},
    '335 248 30 2 1 200': {'unit_price': 89.7, 'plate_price': 13000},
    '335 248 30 2 1 300': {'unit_price': 88.6, 'plate_price': 13000},

    '235 176 25 2 2 50': {'unit_price': 83.8, 'plate_price': 26000},
    '235 176 25 2 2 100': {'unit_price': 79.4, 'plate_price': 26000},
    '235 176 25 2 2 200': {'unit_price': 76.0, 'plate_price': 26000},
    '235 176 25 2 2 300': {'unit_price': 74.8, 'plate_price': 26000},
    '310 228 25 2 2 50': {'unit_price': 103.8, 'plate_price': 26000},
    '310 228 25 2 2 100': {'unit_price': 91.9, 'plate_price': 26000},
    '310 228 25 2 2 200': {'unit_price': 81.0, 'plate_price': 26000},
    '310 228 25 2 2 300': {'unit_price': 79.8, 'plate_price': 26000},
    '335 248 30 2 2 50': {'unit_price': 113.8, 'plate_price': 26000},
    '335 248 30 2 2 100': {'unit_price': 98.2, 'plate_price': 26000},
    '335 248 30 2 2 200': {'unit_price': 89.7, 'plate_price': 26000},
    '335 248 30 2 2 300': {'unit_price': 88.6, 'plate_price': 26000},
}


def get_unit_price(options, extra):
    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    depth = Decimal(options['size']['depth'])  # 奥行き(縦)
    quantity = Decimal(options['quantity'])  # 注文数
    print_area_num = Decimal(options['print_area_num'])
    design_num = options['design_num']  # 表面生地

    key = "{} {} {} {} {} {}".format(width, depth, height, print_area_num, design_num, quantity)
    try:
        unit_price = prices[key]['unit_price']
    except KeyError:
        raise ValidationError("Invalid parameter")
    return round(Decimal(unit_price), 2)


def get_plate_price(options):
    """版代
    """
    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    depth = Decimal(options['size']['depth'])  # 奥行き(縦)
    quantity = Decimal(options['quantity'])  # 注文数
    print_area_num = Decimal(options['print_area_num'])
    design_num = options['design_num']  # 表面生地

    key = "{} {} {} {} {} {}".format(width, depth, height, print_area_num, design_num, quantity)
    try:
        plate_price = prices[key]['plate_price']
    except KeyError:
        raise ValidationError("Invalid parameter")
    return Decimal(plate_price)


def get_mold_price(options):
    """木型代
    """
    return Decimal(0)


def get_shipping_price(options):
    return Decimal(0)
