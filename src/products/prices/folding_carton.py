from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext
from math import ceil, floor


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
    surface_material = options['surface_material']  # 表面生地
    surface_process = options['surface_process']  # 表面加工
    emboss = options['emboss']  # エンボス/デボス
    special_print = options['special_print']  # 特殊印刷
    bottom = options['bottom']  # 底
    inside = options['print_area_inside']  # 内側印刷面
    outside = options['print_area_outside']  # 外側印刷面

    # フルカラー
    if color_num < 0:
        color_num = 5

    # w, h, s: 展開図幅、縦、面積
    w = (2 * width) + (2 * depth) + 20
    t = min(height, 20)
    if bottom == 'onetouch':
        h = height + (Decimal(1.7) * depth) + 2 * t + 10
    elif bottom == 'caramel':
        h = height + (Decimal(2) * depth) + 2 * t + 10
    s = w * h

    # a
    # OBSOLETE
    # if 2 * h - depth < 1100:
    #     a = min(floor(800 / min(w, 2 * h - depth)) * floor(1100 / max(w, 2 * h - depth)), 8)
    # else:
    #     a = 1
    # a_0
    if bottom == 'onetouch':
        _h2 = 2 * h - (depth / 2 + t)
        _h3 = 3 * h - (depth / 2 + t)
        _h4 = 4 * h - (depth + 2 * t)
        if _h2 >= 800:
            h_800 = 1
        elif _h2 < 800 and _h3 >= 800:
            h_800 = 2
        elif _h3 < 800 and _h4 >= 800:
            h_800 = 3
        elif _h4 < 800:
            h_800 = 4
        else:
            raise ValidationError("Invalid H_p800.")
        if _h2 >= 1100:
            h_1100 = 1
        elif _h2 < 1100 and _h3 >= 1100:
            h_1100 = 2
        elif _h3 < 1100 and _h4 >= 1100:
            h_1100 = 3
        elif _h4 < 1100:
            h_1100 = 4
        else:
            raise ValidationError("Invalid H_p1100.")
        a_0 = max(floor(1100 / w) * h_800, floor(800 / w) * h_1100, 8)
    elif bottom == 'caramel':
        a_0 = max(floor(1100 / w) * (floor((800 - h) / (h - (depth / 2 + t))) + 1),
                  floor(800 / w) * (floor((1100 - h) / (h - (depth / 2 + t))) + 1),
                  8)
    # a
    if a_0 == 1:
        a = 1
    elif a_0 in [2, 3]:
        a = 2
    elif a_0 in [4, 5]:
        a = 4
    elif a_0 in [6, 7]:
        a = 6
    else:
        a = 8

    # r: 原紙シート数
    r = max(ceil(quantity / (100 * a)) + 1, 3)

    # s_n: シート数
    # OBSOLETE
    # if r % 3 == 0:
    #     s_n = 100 * Decimal(r) / 3
    # else:
    #     s_n = 100 * Decimal(r) / 2
    if a == 8:
        s_n = quantity / 8 + 100
    elif a == 6 or a == 4:
        s_n = quantity / 2 + 100
    else:
        s_n = quantity + 100

    # 素材
    if surface_material == 'normal':
        p_paper = 100
    elif surface_material == 'ivory':
        p_paper = 190
    else:
        raise ValidationError("Invalid surface material")

    if color_num == -1:  # フルカラー
        p_print = max(ceil(s_n / 1000) - 2, 0) * 1000 + 30000
    else:
        p_print = (max(ceil(s_n / 1000) - 2, 0) * 1000 + 15000) * color_num

    # TODO: print_areaから出す
    if len(inside) > 0 and len(outside) > 0:
        a_print = 2
    else:
        a_print = 1

    # 加工
    if surface_process == 'op':
        # p_s = max(12 * Decimal(s_n), 6000)
        p_s = max(12 * Decimal(s_n), 10000)
    elif surface_process == 'mattepp':
        # p_s = max(30 * Decimal(s_n), 9000)
        p_s = max(30 * Decimal(s_n), 20000)
    else:
        raise ValidationError("Invalid surface process")

    if a != 8:
        p_c = max(Decimal(3.25) * quantity + 3750, 10000)
    else:
        p_c = max(Decimal(3) * quantity + 7500, 10000)

    if bottom == 'onetouch':
        p_g = max(4 * quantity + 7500, 14000)
    elif bottom == 'caramel':
        p_g = max(quantity + 7500, 12500)

    # TODO: not `none` -> != 'gold'...
    if emboss == 'none' and special_print == 'none':
        p_f = 0
    else:
        p_f = max(7 * quantity, 10000)

    p_pack = ceil(quantity / (100 * max(floor(250000 / s), 1))) * 150
    p_l = ceil(quantity / (100 * max(floor(250000 / s), 1))) * 100 + 2500

    p_1 = 31 * r * p_paper + 500 * r + a_print * p_print + p_s + p_c + p_g + p_pack + p_l + p_f
    p_0 = Decimal(1.15) * p_1 / quantity

    # 粗利
    return round(round(p_0, accuracy) / (1 - rough) + Decimal(.05), 1)


def get_plate_price(options):
    """版代
    """
    color_num = Decimal(options['color_num'])
    special_print = options['special_print']
    emboss = options['emboss']
    if color_num < 0:  # フルカラー
        price = 15000 * 5
    else:
        price = 15000 * color_num
    if emboss != 'none':
        price += 11000
    if special_print != 'none':
        price += 11000
    return ceil(price)


def get_mold_price(options):
    """木型代
    """
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    depth = Decimal(options['size']['depth'])  # 奥行き(縦)
    bottom = options['bottom']  # 底

    # w, h, s: 展開図幅、縦、面積
    w = (2 * width) + (2 * depth) + 20
    t = max(height, 20)
    if bottom == 'onetouch':
        # h = height + (Decimal(1.7) * depth) + 2 * t + 10
        h = height + (Decimal(1.7) * depth) + 20 + 10
    elif bottom == 'caramel':
        # h = height + (Decimal(2) * depth) + 2 * t + 10
        h = height + (Decimal(2) * depth) + 20 + 10
    # a_0
    if bottom == 'onetouch':
        _h2 = 2 * h - (depth / 2 + t)
        _h3 = 3 * h - (depth / 2 + t)
        _h4 = 4 * h - (depth + 2 * t)
        if _h2 >= 800:
            h_800 = 1
        elif _h2 < 800 and _h3 >= 800:
            h_800 = 2
        elif _h3 < 800 and _h4 >= 800:
            h_800 = 3
        elif _h4 < 800:
            h_800 = 4
        else:
            raise ValidationError("Invalid H_p800.")
        if _h2 >= 1100:
            h_1100 = 1
        elif _h2 < 1100 and _h3 >= 1100:
            h_1100 = 2
        elif _h3 < 1100 and _h4 >= 1100:
            h_1100 = 3
        elif _h4 < 1100:
            h_1100 = 4
        else:
            raise ValidationError("Invalid H_p1100.")
        a_0 = max(floor(1100 / w) * h_800, floor(800 / w) * h_1100, 8)
    elif bottom == 'caramel':
        a_0 = max(floor(1100 / w) * (floor((800 - h) / (h - (depth / 2 + t))) + 1),
                  floor(800 / w) * (floor((1100 - h) / (h - (depth / 2 + t))) + 1),
                  8)
    # a
    if a_0 == 1:
        a = 1
    elif a_0 in [2, 3]:
        a = 2
    elif a_0 in [4, 5]:
        a = 4
    elif a_0 in [6, 7]:
        a = 6
    else:
        a = 8
    if a in [1, 2]:
        m_p = 1
    elif a in [4, 6]:
        m_p = 2
    else:
        m_p = 4
    return ceil((w + h) * 30 / 100) * 100 * m_p


def get_shipping_price(options):
    return Decimal(0)
