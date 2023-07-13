from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext
from math import floor


getcontext().prec = 10


def get_unit_price(options, extra):

    accuracy = 2
    rough = Decimal(0.15)

    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    depth = Decimal(options['size']['depth'])  # 奥行き(縦)
    color_num = Decimal(options['color_num'])
    quantity = Decimal(options['quantity'])  # 注文数
    surface_material = 'white'  # 表面生地

    # フルカラー
    if color_num < 0:
        color_num = 5

    o = width + height + depth
    t = 90  # 厚み基準値

    # f
    # f = 5 if o <= t else 3
    f = 5  # 今は一旦5

    # a
    (a_1, a_2, a_3, a_4) = (6, 3, 9, 4) if f == 5 else (3, 1, 8, 1)

    # w, h, s: 展開図幅、縦、面積
    w = max(750, 2 * (width - 2 * f) + 2 * (depth - 2 * f) + 3 * a_1 + a_2 + 40)
    h_0 = (depth - 2 * f) + a_1 + a_4 + (height - 4 * f) + a_3 + 10
    # 面付数
    m_1000 = 1000 - floor(1000 / h_0) * h_0
    m_1100 = 1100 - floor(1100 / h_0) * h_0
    m_1200 = 1200 - floor(1200 / h_0) * h_0
    m_1300 = 1300 - floor(1300 / h_0) * h_0
    m_1400 = 1400 - floor(1400 / h_0) * h_0

    if h_0 >= 1000:
        h = Decimal(h_0)
    elif min(m_1000, m_1100, m_1200, m_1300, m_1400) == m_1000:
        h = Decimal(1000 / floor(1000 / h_0))
    elif min(m_1000, m_1100, m_1200, m_1300, m_1400) == m_1100:
        h = Decimal(1100 / floor(1100 / h_0))
    elif min(m_1000, m_1100, m_1200, m_1300, m_1400) == m_1200:
        h = Decimal(1200 / floor(1200 / h_0))
    elif min(m_1000, m_1100, m_1200, m_1300, m_1400) == m_1300:
        h = Decimal(1300 / floor(1300 / h_0))
    else:
        h = Decimal(1400 / floor(1400 / h_0))

    s = w * h

    # t_0: 流れ方向長さ
    t_0 = w * quantity / 1000

    # 印刷色数の考慮
    c = 1 if color_num > 0 else 0

    # p: 表面素材
    if surface_material == 'craft':
        p = Decimal(0.000059)
    elif surface_material == 'white':
        p = Decimal(0.000066)
    else:
        raise ValidationError("Invalid surface material")

    # a: 注文総面積
    a = s * quantity

    # 固定費のベース金額
    if s < 1100000:
        b_150 = 6000
    elif 1100000 <= s <= 2200000:
        b_150 = 12000
    else:
        b_150 = 18000

    if s > 1100000:
        b_500 = 12000 + 4000 * c
    else:
        b_500 = 8000 + 4000 * c

    if quantity < 150:
        b = b_150
    elif quantity < 500:
        b = b_500
    else:
        b = max(12000, b_500)

    # 固定費
    if quantity <= 200 or a < 100000000:
        b_0 = b
    elif 100000000 <= a < 500000000:
        b_0 = b * Decimal(1.2)
    elif 500000000 <= a < 2000000000:
        b_0 = b * Decimal(1.3)
    else:
        b_0 = b * Decimal(1.8)

    # 単価
    p_0 = (a * p + max(Decimal(b_0), 7 * quantity)) / quantity

    # 白ダンのとき
    if surface_material == 'white':
        if quantity < 300000 / w:
            p_0 = (300000 * Decimal(0.000066) * h + b_0) / quantity
    # 粗利
    return round(round(p_0, accuracy) / (1 - rough) + Decimal(.05), 1)


def get_plate_price(options):
    """版代
    """
    color_num = Decimal(options['color_num'])
    # フルカラー
    if color_num < 0:
        color_num = 5

    print_area_num = Decimal(len(options['print_area_outside']))
    if print_area_num < 1:
        raise ValidationError("Print area must at least 1.")

    return color_num * (30000 + (print_area_num - 1) * 10000)


def get_mold_price(options):
    """木型代
    """
    return Decimal(0)


def get_shipping_price(options):
    return Decimal(0)
