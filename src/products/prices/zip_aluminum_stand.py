from django.core.exceptions import ValidationError
from functools import reduce
from decimal import Decimal, getcontext
from math import floor, ceil


getcontext().prec = 10


def get_unit_price(options, extra):

    v = 1.0  # 出来高数量調整率
    accuracy = 2
    rough = Decimal(0.2)

    # options
    height = Decimal(options['size']['height'])
    width = Decimal(options['size']['width'])
    depth = Decimal(options['size']['depth'])
    color_num = Decimal(options['color_num'])
    quantity = Decimal(options['quantity'])
    material = options['material']

    # フルカラー
    if color_num < 0:
        color_num = 5

    # listed price params
    unit_price = [Decimal(_) for _ in [0.8, 1, 0.4]]
    thickness = [Decimal(_) for _ in [12, 7, 60]]
    loss = [Decimal(_) for _ in [0.02, 0.01, 0.03]]
    laminate_unit_price = [Decimal(_) for _ in [6, 5]]
    laminate_loss = [Decimal(_) for _ in [0.03, 0.03]]
    if width >= 200:
        thickness[2] = Decimal(80)
    else:
        thickness[2] = Decimal(60)

    # material
    if material == 'normal':
        c_m, c_mp = 0, 0
    elif material == 'mattepet':
        c_m, c_mp = 0, Decimal(2.8)
    elif material == 'highmatte':
        c_m, c_mp = Decimal(0.006), 0
    else:
        raise ValidationError("Invalid material.")

    # x
    x = 2 * height + depth

    # t: 面付け
    t_0 = floor((630 - 40) / x)
    t_1 = 2 if t_0 >= 2 else 1

    # p: 印刷
    p_0 = Decimal(0.0015) * (t_1 * x + 20) + Decimal(0.9)
    p_t = Decimal(1.6)
    p_1 = max(p_0, p_t)

    # s: 製袋
    s_0 = Decimal(0.037) * width
    s_t = Decimal(4)
    s_1 = max(s_0, s_t)

    # r_all: ロス率
    r_all = 1
    for _l in loss:
        r_all *= (1 - _l)
    for _l in laminate_loss:
        r_all *= (1 - _l)

    # n: 出来高（ロスも含めた実際作られる部数）
    n_8000 = floor(80000 / width * t_1 * r_all) * 100
    n_6000 = floor(60000 / width * t_1 * (r_all - Decimal(0.04))) * 100
    n_4000 = floor(40000 / width * t_1 * (r_all - Decimal(0.04))) * 100
    n_2000 = floor(20000 / width * t_1 * (r_all - Decimal(0.12))) * 100

    # y
    y_base = Decimal(0)
    all_loss = [1 + _ for _ in loss[:1]] + \
               [1 + _ for _ in laminate_loss] + \
               [1 + _ for _ in loss[1:]]
    for i, (_u, _t) in enumerate(zip(unit_price, thickness)):
        if i == 0:
            y_base += _u * c_mp * _t * t_1 * x * reduce(lambda _, __: _ * __, all_loss[i:])
        else:
            y_base += _u * _t * t_1 * x * reduce(lambda _, __: _ * __, all_loss[i:])
    for i, lup in enumerate(laminate_unit_price):
        y_base += (t_1 * x + 40) * lup * reduce(lambda _, __: _ * __, all_loss[1 + i:])
    y_base += (p_1 * color_num + (t_1 * x + 20) * c_m) * 1000 * reduce(lambda _, __: _ * __, all_loss)
    y_base += 1000 * (1 + loss[1]) * (1 + loss[2])
    y_base += s_1 * floor(1000000 * t_1 / width) * (1 + loss[2])
    y_base = y_base * 8 / n_8000

    # q: 出来高数量調整
    q = quantity / Decimal(v)

    # y_q: 最終算出単価
    if q > n_8000:
        s_q = ceil(4 * q / n_8000) * n_8000 * y_base / 4
    elif n_8000 >= q > n_6000:
        s_q = y_base * n_8000
    elif n_6000 >= q > n_4000:
        s_q = y_base * Decimal(1.03) * n_6000
    elif n_4000 >= q > n_2000:
        s_q = y_base * Decimal(1.03) * Decimal(1.03) * n_4000
    elif q >= 3000:
        s_q = y_base * Decimal(1.03) * Decimal(1.03) * Decimal(1.27) * n_2000
    else:
        raise ValidationError("Quantity is too small")
    # 粗利 1000単位で切り上げ
    s_rough = -(-(s_q / (1 - rough)) // 1000) * 1000 + Decimal(0.1) * quantity
    return round(s_rough / quantity, 1)


def get_plate_price(options):
    color_num = Decimal(options['color_num'])
    if color_num < 0:  # フルカラー
        return 15000 * 5
    return 15000 * color_num


def get_mold_price(options):
    return Decimal(0)


def get_shipping_price(options):
    return Decimal(0)
