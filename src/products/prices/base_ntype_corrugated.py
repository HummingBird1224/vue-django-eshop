from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext
from math import floor


getcontext().prec = 10


prices = {
    # width depth height print_area_num design_num quantity
    '150 150 50 1 1 50': {'unit_price': 167.5, 'plate_price': 13000},
    '150 150 50 1 1 100': {'unit_price': 125.7, 'plate_price': 13000},
    '150 150 50 1 1 200': {'unit_price': 97.2, 'plate_price': 13000},
    '150 150 50 1 1 300': {'unit_price': 84.0, 'plate_price': 13000},
    '165 100 35 1 1 50': {'unit_price': 167.5, 'plate_price': 13000},
    '165 100 35 1 1 100': {'unit_price': 125.7, 'plate_price': 13000},
    '165 100 35 1 1 200': {'unit_price': 97.2, 'plate_price': 13000},
    '165 100 35 1 1 300': {'unit_price': 84.0, 'plate_price': 13000},
    '190 135 35 1 1 50': {'unit_price': 167.5, 'plate_price': 13000},
    '190 135 35 1 1 100': {'unit_price': 125.7, 'plate_price': 13000},
    '190 135 35 1 1 200': {'unit_price': 97.2, 'plate_price': 13000},
    '190 135 35 1 1 300': {'unit_price': 84.0, 'plate_price': 13000},
    '235 165 45 1 1 50': {'unit_price': 195.0, 'plate_price': 13000},
    '235 165 45 1 1 100': {'unit_price': 150.7, 'plate_price': 13000},
    '235 165 45 1 1 200': {'unit_price': 122.9, 'plate_price': 13000},
    '235 165 45 1 1 300': {'unit_price': 102.8, 'plate_price': 13000},
    '250 100 50 1 1 50': {'unit_price': 182.5, 'plate_price': 13000},
    '250 100 50 1 1 100': {'unit_price': 138.2, 'plate_price': 13000},
    '250 100 50 1 1 200': {'unit_price': 110.4, 'plate_price': 13000},
    '250 100 50 1 1 300': {'unit_price': 96.5, 'plate_price': 13000},
    '275 200 60 1 1 50': {'unit_price': 207.5, 'plate_price': 13000},
    '275 200 60 1 1 100': {'unit_price': 164.4, 'plate_price': 13000},
    '275 200 60 1 1 200': {'unit_price': 135.4, 'plate_price': 13000},
    '275 200 60 1 1 300': {'unit_price': 109.0, 'plate_price': 13000},
    '285 135 70 1 1 50': {'unit_price': 195.0, 'plate_price': 13000},
    '285 135 70 1 1 100': {'unit_price': 150.7, 'plate_price': 13000},
    '285 135 70 1 1 200': {'unit_price': 122.9, 'plate_price': 13000},
    '285 135 70 1 1 300': {'unit_price': 102.8, 'plate_price': 13000},
    '330 230 40 1 1 50': {'unit_price': 207.5, 'plate_price': 13000},
    '330 230 40 1 1 100': {'unit_price': 164.4, 'plate_price': 13000},
    '330 230 40 1 1 200': {'unit_price': 135.4, 'plate_price': 13000},
    '330 230 40 1 1 300': {'unit_price': 109.0, 'plate_price': 13000},

    '150 150 50 2 1 50': {'unit_price': 186.3, 'plate_price': 13000},
    '150 150 50 2 1 100': {'unit_price': 144.4, 'plate_price': 13000},
    '150 150 50 2 1 200': {'unit_price': 116, 'plate_price': 13000},
    '150 150 50 2 1 300': {'unit_price': 102.8, 'plate_price': 13000},
    '165 100 35 2 1 50': {'unit_price': 186.3, 'plate_price': 13000},
    '165 100 35 2 1 100': {'unit_price': 144.4, 'plate_price': 13000},
    '165 100 35 2 1 200': {'unit_price': 116, 'plate_price': 13000},
    '165 100 35 2 1 300': {'unit_price': 102.8, 'plate_price': 13000},
    '190 135 35 2 1 50': {'unit_price': 186.3, 'plate_price': 13000},
    '190 135 35 2 1 100': {'unit_price': 144.4, 'plate_price': 13000},
    '190 135 35 2 1 200': {'unit_price': 116, 'plate_price': 13000},
    '190 135 35 2 1 300': {'unit_price': 102.8, 'plate_price': 13000},
    '235 165 45 2 1 50': {'unit_price': 213.8, 'plate_price': 13000},
    '235 165 45 2 1 100': {'unit_price': 169.4, 'plate_price': 13000},
    '235 165 45 2 1 200': {'unit_price': 141.6, 'plate_price': 13000},
    '235 165 45 2 1 300': {'unit_price': 121.5, 'plate_price': 13000},
    '250 100 50 2 1 50': {'unit_price': 201.3, 'plate_price': 13000},
    '250 100 50 2 1 100': {'unit_price': 156.9, 'plate_price': 13000},
    '250 100 50 2 1 200': {'unit_price': 129.1, 'plate_price': 13000},
    '250 100 50 2 1 300': {'unit_price': 115.3, 'plate_price': 13000},
    '275 200 60 2 1 50': {'unit_price': 226.3, 'plate_price': 13000},
    '275 200 60 2 1 100': {'unit_price': 183.2, 'plate_price': 13000},
    '275 200 60 2 1 200': {'unit_price': 154.1, 'plate_price': 13000},
    '275 200 60 2 1 300': {'unit_price': 127.8, 'plate_price': 13000},
    '285 135 70 2 1 50': {'unit_price': 213.8, 'plate_price': 13000},
    '285 135 70 2 1 100': {'unit_price': 169.4, 'plate_price': 13000},
    '285 135 70 2 1 200': {'unit_price': 141.6, 'plate_price': 13000},
    '285 135 70 2 1 300': {'unit_price': 121.5, 'plate_price': 13000},
    '330 230 40 2 1 50': {'unit_price': 226.3, 'plate_price': 26000},
    '330 230 40 2 1 100': {'unit_price': 183.2, 'plate_price': 26000},
    '330 230 40 2 1 200': {'unit_price': 154.1, 'plate_price': 26000},
    '330 230 40 2 1 300': {'unit_price': 127.8, 'plate_price': 26000},

    '150 150 50 2 2 50': {'unit_price':  186.3, 'plate_price': 26000},
    '150 150 50 2 2 100': {'unit_price': 144.4, 'plate_price': 26000},
    '150 150 50 2 2 200': {'unit_price': 116, 'plate_price': 26000},
    '150 150 50 2 2 300': {'unit_price': 102.8, 'plate_price': 26000},
    '165 100 35 2 2 50': {'unit_price': 186.3, 'plate_price': 26000},
    '165 100 35 2 2 100': {'unit_price': 144.4, 'plate_price': 26000},
    '165 100 35 2 2 200': {'unit_price': 116, 'plate_price': 26000},
    '165 100 35 2 2 300': {'unit_price': 102.8, 'plate_price': 26000},
    '190 135 35 2 2 50': {'unit_price': 186.3, 'plate_price': 26000},
    '190 135 35 2 2 100': {'unit_price': 144.4, 'plate_price': 26000},
    '190 135 35 2 2 200': {'unit_price': 116, 'plate_price': 26000},
    '190 135 35 2 2 300': {'unit_price': 102.8, 'plate_price': 26000},
    '235 165 45 2 2 50': {'unit_price': 213.8, 'plate_price': 26000},
    '235 165 45 2 2 100': {'unit_price': 169.4, 'plate_price': 26000},
    '235 165 45 2 2 200': {'unit_price': 141.6, 'plate_price': 26000},
    '235 165 45 2 2 300': {'unit_price': 121.5, 'plate_price': 26000},
    '250 100 50 2 2 50': {'unit_price': 201.3, 'plate_price': 26000},
    '250 100 50 2 2 100': {'unit_price': 156.9, 'plate_price': 26000},
    '250 100 50 2 2 200': {'unit_price': 129.1, 'plate_price': 26000},
    '250 100 50 2 2 300': {'unit_price': 115.3, 'plate_price': 26000},
    '275 200 60 2 2 50': {'unit_price': 226.3, 'plate_price': 26000},
    '275 200 60 2 2 100': {'unit_price': 183.2, 'plate_price': 26000},
    '275 200 60 2 2 200': {'unit_price': 154.1, 'plate_price': 26000},
    '275 200 60 2 2 300': {'unit_price': 127.8, 'plate_price': 26000},
    '285 135 70 2 2 50': {'unit_price':213.8, 'plate_price': 26000},
    '285 135 70 2 2 100': {'unit_price':169.4, 'plate_price': 26000},
    '285 135 70 2 2 200': {'unit_price':141.6, 'plate_price': 26000},
    '285 135 70 2 2 300': {'unit_price':121.5, 'plate_price': 26000},
    '330 230 40 2 2 50': {'unit_price': 226.3, 'plate_price': 26000},
    '330 230 40 2 2 100': {'unit_price': 183.2, 'plate_price': 26000},
    '330 230 40 2 2 200': {'unit_price': 154.1, 'plate_price': 26000},
    '330 230 40 2 2 300': {'unit_price': 127.8, 'plate_price': 26000},
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
