from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext


getcontext().prec = 10


prices = {
    # width depth height print_area_num design_num quantity
    '210 180 100 200': {'unit_price': 217.5, 'plate_price': 16000},
    '210 180 100 400': {'unit_price': 148.2, 'plate_price': 16000},
    '210 180 100 600': {'unit_price': 79.4, 'plate_price': 16000},
    '210 180 100 800': {'unit_price': 65.4, 'plate_price': 16000},
    '210 180 100 1000': {'unit_price': 55.7, 'plate_price': 16000},

    '250 200 120 200': {'unit_price': 218.8, 'plate_price': 16000},
    '250 200 120 400': {'unit_price': 149.4, 'plate_price': 16000},
    '250 200 120 600': {'unit_price': 80.7, 'plate_price': 16000},
    '250 200 120 800': {'unit_price': 66.6, 'plate_price': 16000},
    '250 200 120 1000': {'unit_price': 56.9, 'plate_price': 16000},

    '230 220 60 200': {'unit_price': 221.3, 'plate_price': 16000},
    '230 220 60 400': {'unit_price': 151.3, 'plate_price': 16000},
    '230 220 60 600': {'unit_price': 81.9, 'plate_price': 16000},
    '230 220 60 800': {'unit_price': 68.2, 'plate_price': 16000},
    '230 220 60 1000': {'unit_price': 58.8, 'plate_price': 16000},

    '300 220 100 200': {'unit_price': 221.3, 'plate_price': 16000},
    '300 220 100 400': {'unit_price': 151.3, 'plate_price': 16000},
    '300 220 100 600': {'unit_price': 81.9, 'plate_price': 16000},
    '300 220 100 800': {'unit_price': 68.2, 'plate_price': 16000},
    '300 220 100 1000': {'unit_price': 58.8, 'plate_price': 16000},

    '310 260 60 200': {'unit_price': 222.5, 'plate_price': 16000},
    '310 260 60 400': {'unit_price': 152.5, 'plate_price': 16000},
    '310 260 60 600': {'unit_price': 83.2, 'plate_price': 16000},
    '310 260 60 800': {'unit_price': 69.4, 'plate_price': 16000},
    '310 260 60 1000': {'unit_price': 60.0, 'plate_price': 16000},

    '330 260 110 200': {'unit_price': 221.3, 'plate_price': 16000},
    '330 260 110 400': {'unit_price': 151.3, 'plate_price': 16000},
    '330 260 110 600': {'unit_price': 81.9, 'plate_price': 16000},
    '330 260 110 800': {'unit_price': 68.2, 'plate_price': 16000},
    '330 260 110 1000': {'unit_price': 58.8, 'plate_price': 16000},
}


def get_unit_price(options, extra):
    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    depth = Decimal(options['size']['depth'])  # 奥行き(縦)
    quantity = Decimal(options['quantity'])  # 注文数

    key = "{} {} {} {}".format(height, width, depth, quantity)
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

    key = "{} {} {} {}".format(height, width, depth, quantity)
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
