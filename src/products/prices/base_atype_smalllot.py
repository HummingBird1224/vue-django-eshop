from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext
from math import ceil, floor


getcontext().prec = 10

prices = {
    '250 210 120 1 100': {'unit_price': 46, 'plate_price': 6500},
    '250 210 120 1 200': {'unit_price': 46, 'plate_price': 6500},
    '250 210 120 1 300': {'unit_price': 46, 'plate_price': 6500},
    '310 220 150 1 100': {'unit_price': 56, 'plate_price': 6500},
    '310 220 150 1 200': {'unit_price': 56, 'plate_price': 6500},
    '310 220 150 1 300': {'unit_price': 56, 'plate_price': 6500},
    '350 300 250 1 100': {'unit_price': 85, 'plate_price': 6500},
    '350 300 250 1 200': {'unit_price': 85, 'plate_price': 6500},
    '350 300 250 1 300': {'unit_price': 85, 'plate_price': 6500},
    '250 210 120 2 100': {'unit_price': 61, 'plate_price': 6500},
    '250 210 120 2 200': {'unit_price': 61, 'plate_price': 6500},
    '250 210 120 2 300': {'unit_price': 61, 'plate_price': 6500},
    '310 220 150 2 100': {'unit_price': 71, 'plate_price': 6500},
    '310 220 150 2 200': {'unit_price': 71, 'plate_price': 6500},
    '310 220 150 2 300': {'unit_price': 71, 'plate_price': 6500},
    '350 300 250 2 100': {'unit_price': 100, 'plate_price': 6500},
    '350 300 250 2 200': {'unit_price': 100, 'plate_price': 6500},
    '350 300 250 2 300': {'unit_price': 100, 'plate_price': 6500},
}


def get_unit_price(options, extra):
    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    depth = Decimal(options['size']['depth'])  # 奥行き(縦)
    quantity = options['quantity']  # 注文数
    print_area = options['print_area']  # 印刷面
    key = "{} {} {} {} {}".format(width, depth, height, print_area, quantity)
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
    depth = Decimal(options['size']['depth'])  # 奥行き(縦)
    quantity = options['quantity']  # 注文数
    print_area = options['print_area']  # 印刷面
    key = "{} {} {} {} {}".format(width, depth, height, print_area, quantity)
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
