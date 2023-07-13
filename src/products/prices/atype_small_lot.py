from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext


getcontext().prec = 10


prices = {
    # width depth height print_area_num design_num quantity
    '250 210 120 1 1 100': {'unit_price': 58.4, 'plate_price': 10000},
    '250 210 120 1 1 200': {'unit_price': 58.4, 'plate_price': 10000},
    '250 210 120 1 1 300': {'unit_price': 58.4, 'plate_price': 10000},
    '250 190 190 1 1 100': {'unit_price': 69.5, 'plate_price': 10000},
    '250 190 190 1 1 200': {'unit_price': 69.5, 'plate_price': 10000},
    '250 190 190 1 1 300': {'unit_price': 69.5, 'plate_price': 10000},
    '310 220 150 1 1 100': {'unit_price': 58.3, 'plate_price': 10000},
    '310 220 150 1 1 200': {'unit_price': 51.7, 'plate_price': 10000},
    '310 220 150 1 1 300': {'unit_price': 51.4, 'plate_price': 10000},
    '400 200 100 1 1 100': {'unit_price': 57.6, 'plate_price': 10000},
    '400 200 100 1 1 200': {'unit_price': 51.6, 'plate_price': 10000},
    '400 200 100 1 1 300': {'unit_price': 51.3, 'plate_price': 10000},
    '350 300 250 1 1 100': {'unit_price': 106.7, 'plate_price': 10000},
    '350 300 250 1 1 200': {'unit_price': 106.7, 'plate_price': 10000},
    '350 300 250 1 1 300': {'unit_price': 106.7, 'plate_price': 10000},
    '435 310 230 1 1 100': {'unit_price': 134.5, 'plate_price': 10000},
    '435 310 230 1 1 200': {'unit_price': 134.5, 'plate_price': 10000},
    '435 310 230 1 1 300': {'unit_price': 134.5, 'plate_price': 10000},

    '250 210 120 2 1 100': {'unit_price': 75.0, 'plate_price': 10000},
    '250 210 120 2 1 200': {'unit_price': 75.0, 'plate_price': 10000},
    '250 210 120 2 1 300': {'unit_price': 75.0, 'plate_price': 10000},
    '250 190 190 2 1 100': {'unit_price': 86.2, 'plate_price': 10000},
    '250 190 190 2 1 200': {'unit_price': 86.2, 'plate_price': 10000},
    '250 190 190 2 1 300': {'unit_price': 86.2, 'plate_price': 10000},
    '310 220 150 2 1 100': {'unit_price': 79.8, 'plate_price': 10000},
    '310 220 150 2 1 200': {'unit_price': 79.8, 'plate_price': 10000},
    '310 220 150 2 1 300': {'unit_price': 79.8, 'plate_price': 10000},
    '400 200 100 2 1 100': {'unit_price': 76.4, 'plate_price': 10000},
    '400 200 100 2 1 200': {'unit_price': 76.4, 'plate_price': 10000},
    '400 200 100 2 1 300': {'unit_price': 76.4, 'plate_price': 10000},
    '350 300 250 2 1 100': {'unit_price': 123.4, 'plate_price': 10000},
    '350 300 250 2 1 200': {'unit_price': 123.4, 'plate_price': 10000},
    '350 300 250 2 1 300': {'unit_price': 123.4, 'plate_price': 10000},
    '435 310 230 2 1 100': {'unit_price': 151.2, 'plate_price': 10000},
    '435 310 230 2 1 200': {'unit_price': 151.2, 'plate_price': 10000},
    '435 310 230 2 1 300': {'unit_price': 151.2, 'plate_price': 10000},

    '250 210 120 2 2 100': {'unit_price': 75.0, 'plate_price': 20000},
    '250 210 120 2 2 200': {'unit_price': 75.0, 'plate_price': 20000},
    '250 210 120 2 2 300': {'unit_price': 75.0, 'plate_price': 20000},
    '250 190 190 2 2 100': {'unit_price': 86.2, 'plate_price': 20000},
    '250 190 190 2 2 200': {'unit_price': 86.2, 'plate_price': 20000},
    '250 190 190 2 2 300': {'unit_price': 86.2, 'plate_price': 20000},
    '310 220 150 2 2 100': {'unit_price': 79.8, 'plate_price': 20000},
    '310 220 150 2 2 200': {'unit_price': 79.8, 'plate_price': 20000},
    '310 220 150 2 2 300': {'unit_price': 79.8, 'plate_price': 20000},
    '400 200 100 2 2 100': {'unit_price': 76.4, 'plate_price': 20000},
    '400 200 100 2 2 200': {'unit_price': 76.4, 'plate_price': 20000},
    '400 200 100 2 2 300': {'unit_price': 76.4, 'plate_price': 20000},
    '350 300 250 2 2 100': {'unit_price': 123.4, 'plate_price': 20000},
    '350 300 250 2 2 200': {'unit_price': 123.4, 'plate_price': 20000},
    '350 300 250 2 2 300': {'unit_price': 123.4, 'plate_price': 20000},
    '435 310 230 2 2 100': {'unit_price': 151.2, 'plate_price': 20000},
    '435 310 230 2 2 200': {'unit_price': 151.2, 'plate_price': 20000},
    '435 310 230 2 2 300': {'unit_price': 151.2, 'plate_price': 20000},
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
