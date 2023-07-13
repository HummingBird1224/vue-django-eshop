from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext
from math import ceil


getcontext().prec = 10


def get_unit_price_normal(
        color_num,
        w,
        h,
        s,
        quantity,
        surface_material):

    # p: 表面素材
    if surface_material == 'craft':
        p = Decimal(0.000059)
    elif surface_material == 'white':
        p = Decimal(0.000066)
    else:
        raise ValidationError("Invalid surface material")

    # フルカラー
    if color_num < 0:
        color_num = 5

    # a: 注文総面積
    a = s * quantity

    # 固定費
    if quantity > 1000:
        b_0 = 40000 + 3000 * color_num
    else:
        b_0 = 40000

    if quantity < 1000:
        b_1 = Decimal(1.3) * b_0
    elif 1000 <= quantity <= 2000:
        b_1 = (Decimal(0.0011) * quantity + Decimal(0.2)) * b_0
    else:
        b_1 = (Decimal(0.0007) * quantity + 1) * b_0

    # 単価
    if quantity < 300000 / h:
        p_0 = (300000 * p * w + b_1) / quantity
    else:
        p_0 = (a * p + b_1) / quantity

    return p_0


def get_unit_price_laminating(
        color_num,
        s,
        quantity,
        surface_process):
    r = ceil(quantity / 100) + ceil((quantity - 1000) / 2000) + 3
    p_paper = 2000
    # p_print = max(3 * color_num * quantity + 20000, 8000 * color_num)
    if color_num < 0:  # full color
        p_print = max(ceil(quantity / 1000) - 2, 0) * 2000 + 35000
    else:
        p_print = (max(ceil(quantity / 1000) - 2, 0) * 2000 + 10000) * color_num
    if surface_process == 'mattevarnish':
        p_s = max(10 * quantity, 15000)
    elif surface_process == 'mattepp':
        p_s = max(28 * quantity, 20000)
    elif surface_process == 'none':
        p_s = max(10 * quantity, 15000)
    else:
        raise ValidationError("Invalid surface process")
    p_c = Decimal(2.25) * quantity + 26250
    p_g = ceil(62 * s) * quantity / 1000000 + 40000
    p_pack = max(ceil(quantity / 100) * 250 + 1500, 2000)
    p_1 = 2 * quantity + 5000
    p_0 = (r * p_paper + p_print + p_s + p_c + p_g + p_pack + p_1) / quantity
    return p_0


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
    surface_process = 'none'  # 表面加工

    # w, h, s: 展開図幅、縦、面積
    w = width + 4 * height + 31
    h = 2 * depth + 3 * height + 15
    s = w * h

    if surface_material == 'craft' or surface_material == 'white':
        p_0 = get_unit_price_normal(
            color_num,
            w,
            h,
            s,
            quantity,
            surface_material
        )
    elif surface_material == 'laminating':
        p_0 = get_unit_price_laminating(
            color_num,
            s,
            quantity,
            surface_process
        )
    else:
        raise ValidationError("Invalid surface material")
    # 粗利
    return round(round(p_0, accuracy) / (1 - rough) + Decimal(.05), 1)


def get_plate_price(options):
    """版代
    """
    surface_material = 'white'
    if surface_material == 'laminating':
        return 0
    color_num = Decimal(options['color_num'])
    if color_num < 0:
        color_num = 5
    print_area_num = Decimal(len(options['print_area_outside']))
    if print_area_num < 1:
        raise ValidationError("Print area must at least 1.")
    return color_num * (30000 + (print_area_num - 1) * 10000)


def get_mold_price(options):
    """木型代
    """
    height = Decimal(options['size']['height'])
    width = Decimal(options['size']['width'])
    depth = Decimal(options['size']['depth'])

    w = width + 4 * height + 31
    h = 2 * depth + 3 * height + 15
    d = ceil((w + h) * 80 / 100) * 100
    return d


def get_shipping_price(options):
    return Decimal(0)
