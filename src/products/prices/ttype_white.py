from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext
from math import ceil


getcontext().prec = 10


def get_unit_price(options, extra):

    accuracy = 2
    rough = Decimal(0.2)

    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    depth = Decimal(options['size']['depth'])  # 奥行き(縦)
    color_num = Decimal(options['color_num'])  # 色数
    quantity = Decimal(options['quantity'])  # 注文数
    surface_material = 'white'  # 表面生地

    # フルカラー
    if color_num < 0:
        color_num = 5

    f = 1.1

    # w, h, s: 展開図幅、縦、面積
    w = width + 2 * height + 43
    h = 2 * height + Decimal(2.75) * depth
    s = w * h

    # p: 表面素材
    if surface_material == 'craft':
        p = Decimal(0.000059)
    elif surface_material == 'white':
        p = Decimal(0.000066)
    else:
        raise ValidationError("Invalid surface material")

    # a: 注文総面積
    a = s * quantity

    # 固定費
    if quantity > 1000:
        b_0 = 28000 + 3000 * color_num
    else:
        b_0 = 28000

    if quantity < 1000:
        b_1 = Decimal(1.3) * b_0
    elif 1000 <= quantity <= 2000:
        b_1 = (Decimal(0.0011) * quantity + Decimal(0.2)) * b_0
    elif 2000 <= quantity <= 10000:
        b_1 = (Decimal(0.0007) * quantity + 1) * b_0
    else:
        b_1 = (Decimal(0.0004) * quantity + 4) * b_0

    if quantity < 300000 / h:
        p_0 = (300000 * p * w + b_1) / quantity
    else:
        p_0 = (a * p + b_1) / quantity

    # 粗利
    return round(round(p_0, accuracy) / (1 - rough) + Decimal(.05), 1)


def get_plate_price(options):
    """版代
    """
    color_num = Decimal(options['color_num'])
    # フルカラー
    if color_num < 0:
        color_num = 5
    print_area = Decimal(len(options['print_area_outside']))
    if print_area < 1:
        raise ValidationError("Print area must at least 1.")
    return color_num * (30000 + (print_area - 1) * 10000)


def get_mold_price(options):
    """木型代
    """
    height = Decimal(options['size']['height'])
    width = Decimal(options['size']['width'])
    depth = Decimal(options['size']['depth'])

    w = width + 2 * height + 43
    h = 2 * height + Decimal(2.75) * depth

    return ceil((w + h) * 80 / 100) * 100


def get_shipping_price(options):
    return Decimal(0)
