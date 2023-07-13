from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext
from math import ceil


getcontext().prec = 10


prices = {
    # width depth height print_area_num design_num quantity
    '165 120 30 1 1 50': {'unit_price': 167.5, 'plate_price': 13000},
    '165 120 30 1 1 100': {'unit_price': 125.7, 'plate_price': 13000},
    '165 120 30 1 1 200': {'unit_price': 97.2, 'plate_price': 13000},
    '165 120 30 1 1 300': {'unit_price': 84.0, 'plate_price': 13000},
    '195 140 30 1 1 50': {'unit_price': 167.5, 'plate_price': 13000},
    '195 140 30 1 1 100': {'unit_price': 125.7, 'plate_price': 13000},
    '195 140 30 1 1 200': {'unit_price': 97.2, 'plate_price': 13000},
    '195 140 30 1 1 300': {'unit_price': 84.0, 'plate_price': 13000},
    '220 160 30 1 1 50': {'unit_price': 167.5, 'plate_price': 13000},
    '220 160 30 1 1 100': {'unit_price': 125.7, 'plate_price': 13000},
    '220 160 30 1 1 200': {'unit_price': 97.2, 'plate_price': 13000},
    '220 160 30 1 1 300': {'unit_price': 84.0, 'plate_price': 13000},
    '275 200 30 1 1 50': {'unit_price': 195.0, 'plate_price': 13000},
    '275 200 30 1 1 100': {'unit_price': 150.7, 'plate_price': 13000},
    '275 200 30 1 1 200': {'unit_price': 122.9, 'plate_price': 13000},
    '275 200 30 1 1 300': {'unit_price': 102.8, 'plate_price': 13000},
    '310 225 30 1 1 50': {'unit_price': 195.0, 'plate_price': 13000},
    '310 225 30 1 1 100': {'unit_price': 150.7, 'plate_price': 13000},
    '310 225 30 1 1 200': {'unit_price': 122.9, 'plate_price': 13000},
    '310 225 30 1 1 300': {'unit_price': 102.8, 'plate_price': 13000},

    '165 120 30 2 1 50': {'unit_price': 186.3, 'plate_price': 13000},
    '165 120 30 2 1 100': {'unit_price': 144.4, 'plate_price': 13000},
    '165 120 30 2 1 200': {'unit_price': 116.0, 'plate_price': 13000},
    '165 120 30 2 1 300': {'unit_price': 102.8, 'plate_price': 13000},
    '195 140 30 2 1 50': {'unit_price': 186.3, 'plate_price': 13000},
    '195 140 30 2 1 100': {'unit_price': 144.4, 'plate_price': 13000},
    '195 140 30 2 1 200': {'unit_price': 116.0, 'plate_price': 13000},
    '195 140 30 2 1 300': {'unit_price': 102.8, 'plate_price': 13000},
    '220 160 30 2 1 50': {'unit_price': 186.3, 'plate_price': 13000},
    '220 160 30 2 1 100': {'unit_price': 144.4, 'plate_price': 13000},
    '220 160 30 2 1 200': {'unit_price': 116.0, 'plate_price': 13000},
    '220 160 30 2 1 300': {'unit_price': 102.8, 'plate_price': 13000},
    '275 200 30 2 1 50': {'unit_price': 213.8, 'plate_price': 13000},
    '275 200 30 2 1 100': {'unit_price': 169.4, 'plate_price': 13000},
    '275 200 30 2 1 200': {'unit_price': 141.6, 'plate_price': 13000},
    '275 200 30 2 1 300': {'unit_price': 121.5, 'plate_price': 13000},
    '310 225 30 2 1 50': {'unit_price': 213.8, 'plate_price': 13000},
    '310 225 30 2 1 100': {'unit_price': 169.4, 'plate_price': 13000},
    '310 225 30 2 1 200': {'unit_price': 141.6, 'plate_price': 13000},
    '310 225 30 2 1 300': {'unit_price': 121.5, 'plate_price': 13000},

    '165 120 30 2 2 50': {'unit_price': 186.3, 'plate_price': 26000},
    '165 120 30 2 2 100': {'unit_price': 144.4, 'plate_price': 26000},
    '165 120 30 2 2 200': {'unit_price': 116.0, 'plate_price': 26000},
    '165 120 30 2 2 300': {'unit_price': 102.8, 'plate_price': 26000},
    '195 140 30 2 2 50': {'unit_price': 186.3, 'plate_price': 26000},
    '195 140 30 2 2 100': {'unit_price': 144.4, 'plate_price': 26000},
    '195 140 30 2 2 200': {'unit_price': 116.0, 'plate_price': 26000},
    '195 140 30 2 2 300': {'unit_price': 102.8, 'plate_price': 26000},
    '220 160 30 2 2 50': {'unit_price': 186.3, 'plate_price': 26000},
    '220 160 30 2 2 100': {'unit_price': 144.4, 'plate_price': 26000},
    '220 160 30 2 2 200': {'unit_price': 116.0, 'plate_price': 26000},
    '220 160 30 2 2 300': {'unit_price': 102.8, 'plate_price': 26000},
    '275 200 30 2 2 50': {'unit_price': 213.8, 'plate_price': 26000},
    '275 200 30 2 2 100': {'unit_price': 169.4, 'plate_price': 26000},
    '275 200 30 2 2 200': {'unit_price': 141.6, 'plate_price': 26000},
    '275 200 30 2 2 300': {'unit_price': 121.5, 'plate_price': 26000},
    '310 225 30 2 2 50': {'unit_price': 213.8, 'plate_price': 26000},
    '310 225 30 2 2 100': {'unit_price': 169.4, 'plate_price': 26000},
    '310 225 30 2 2 200': {'unit_price': 141.6, 'plate_price': 26000},
    '310 225 30 2 2 300': {'unit_price': 121.5, 'plate_price': 26000},
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
