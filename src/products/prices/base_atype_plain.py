from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext


getcontext().prec = 10


prices = {
    # width depth height quantity
    '250 210 120 50': {'unit_price': 57},
    '250 210 120 100': {'unit_price': 36},
    '250 210 120 150': {'unit_price': 27},
    '250 210 120 200': {'unit_price': 27},
    '250 210 120 300': {'unit_price': 27},

    '250 190 190 50': {'unit_price': 57},
    '250 190 190 100': {'unit_price': 36},
    '250 190 190 150': {'unit_price': 27},
    '250 190 190 200': {'unit_price': 27},
    '250 190 190 300': {'unit_price': 27},

    '310 220 150 50': {'unit_price': 64},
    '310 220 150 100': {'unit_price': 42},
    '310 220 150 150': {'unit_price': 39.3},
    '310 220 150 200': {'unit_price': 37.1},
    '310 220 150 300': {'unit_price': 37.1},

    '400 200 100 50': {'unit_price': 64},
    '400 200 100 100': {'unit_price': 42},
    '400 200 100 150': {'unit_price': 42},
    '400 200 100 200': {'unit_price': 42},
    '400 200 100 300': {'unit_price': 42},

    '350 300 250 50': {'unit_price': 73},
    '350 300 250 100': {'unit_price': 72.5},
    '350 300 250 150': {'unit_price': 72.5},
    '350 300 250 200': {'unit_price': 72.5},
    '350 300 250 300': {'unit_price': 72.5},

    '435 310 230 50': {'unit_price': 73},
    '435 310 230 100': {'unit_price': 72.7},
    '435 310 230 150': {'unit_price': 72.7},
    '435 310 230 200': {'unit_price': 72.7},
    '435 310 230 300': {'unit_price': 72.7},

    '470 330 275 50': {'unit_price': 139.9},
    '470 330 275 100': {'unit_price': 138.7},
    '470 330 275 150': {'unit_price': 96},
    '470 330 275 200': {'unit_price': 88},
    '470 330 275 300': {'unit_price': 81.4},
}


def get_unit_price(options, extra):
    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    depth = Decimal(options['size']['depth'])  # 奥行き(縦)
    quantity = Decimal(options['quantity'])  # 注文数

    key = "{} {} {} {}".format(width, depth, height, quantity)
    try:
        unit_price = prices[key]['unit_price']
    except KeyError:
        raise ValidationError("Invalid parameter")
    return round(Decimal(unit_price), 2)


def get_plate_price(options):
    """版代
    """
    return Decimal(0)


def get_mold_price(options):
    """木型代
    """
    return Decimal(0)


def get_shipping_price(options):
    return Decimal(0)
