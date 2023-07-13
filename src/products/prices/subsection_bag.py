from django.core.exceptions import ValidationError
from functools import reduce
from decimal import Decimal, getcontext

getcontext().prec = 10


def get_unit_price(options, extra):
    # NOW IT'S A CONTACT ONLY PRODUCT

    v = 0.8  # 出来高数量調整率
    accuracy = 2

    # options
    color_num = Decimal(options['color_num'])
    height = Decimal(options['size']['height'])
    width = Decimal(options['size']['width'])
    quantity = Decimal(options['quantity'])
    material = Decimal(options['material'])

    # フルカラー
    if color_num < 0:
        color_num = 5

    # price params
    print_up = Decimal(extra['print_unit_price'])  # 印刷単価
    least_print_up = Decimal(extra['least_print_unit_price'])  # 最低印刷単価の担保

    # listed price params
    unit_price = [Decimal(_) for _ in [0.8, 1, 0.4]]
    thickness = [Decimal(_) for _ in [12, 7, 30]]
    loss = [Decimal(_) for _ in [0.02, 0.01]]
    laminate_unit_price = [Decimal(_) for _ in [6, 5]]
    laminate_loss = [Decimal(_) for _ in [0.03, 0.03]]

    # material
    if material == 'normal':
        c_m, c_mp = 0, 0
    elif material == 'mattepet':
        c_m, c_mp = 0, 1.6
    elif material == 'highmatte':
        c_m, c_mp = 0.006, 0
    else:
        raise ValidationError("Invalid material.")

    # x
    x = 2 * width

    # t: 面付け
    t_0 = (1000 - 20) // x
    t_1 = max(t_0, 1)

    # p: 印刷
    p_0 = Decimal(0.0015) * (t_1 * x + 20) + print_up
    p_1 = max(p_0, least_print_up)

    # r_all: ロス率
    r_all = 1
    for l in loss:
        r_all *= (1 - l)
    if laminate_loss:
        for l in loss:
            r_all *= (1 - l)

    # ラミネート工程も含めた全ロス
    all_loss = [1 + _ for _ in loss[:1]] + \
               [1 + _ for _ in laminate_loss] + \
               [1 + _ for _ in loss[1:]]

    # n: 出来高（ロスも含めた実際作られる部数）
    n_8000 = int((80 * t_1 * r_all) // 1) * 100
    n_6000 = int((60 * t_1 * r_all) // 1) * 100
    n_4000 = int((40 * t_1 * r_all) // 1) * 100
    n_2000 = int((20 * t_1 * r_all) // 1) * 100

    # y
    y_base = Decimal(0)
    c_m = material
    for i, (_u, _t) in enumerate(zip(unit_price, thickness)):
        if i == 0:
            y_base += _u * (_t + c_m) * t_1 * x * reduce(lambda _, __: _ * __, all_loss[i:])
        else:
            y_base += _u * _t * t_1 * x * reduce(lambda _, __: _ * __, all_loss[i:])
    for i, lup in enumerate(laminate_unit_price):
        y_base += (t_1 * x + 20) * lup * reduce(lambda _, __: _ * __, all_loss[1 + i:])
    y_base += ((p_1 * color_num) + ((t_1 * x + 20) * c_m)) * 1000 * reduce(lambda _, __: _ * __, all_loss)
    y_base += 2000 * (1 + loss[1])
    y_base = y_base / t_0

    # q: 出来高数量調整
    q = quantity / Decimal(v)

    # y_q: 最終算出単価
    y_q = 0
    if q >= n_8000:
        y = y_base
        y_q = y * (n_8000 + n_2000 * (round(q * 4 / n_8000) - 4)) / q
    elif n_8000 > q >= n_6000:
        y = y_base
        n = n_8000
        y_q = (y * n) / q
    elif n_6000 > q >= n_4000:
        y = y_base * Decimal(1.03)
        n = n_6000
        y_q = (y * n) / q
    elif n_4000 > q >= n_2000:
        y = y_base * Decimal(1.03) * Decimal(1.03)
        n = n_4000
        y_q = (y * n) / q
    elif n_2000 > q:
        y = y_base * Decimal(1.03) * Decimal(1.03) * Decimal(1.27)
        n = n_2000
        y_q = (y * n) / q
    return round(y_q, accuracy)


def get_plate_price(options):
    color_num = Decimal(options['color_num'])
    # フルカラー
    if color_num < 0:
        color_num = 5
    if color_num < 0:  # フルカラー
        return 15000 * 5
    return 15000 * color_num


def get_mold_price(options):
    return Decimal(0)


def get_shipping_price(options):
    return Decimal(0)
