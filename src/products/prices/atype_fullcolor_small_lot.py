from django.core.exceptions import ValidationError
from decimal import Decimal, getcontext, ROUND_CEILING
from math import ceil


getcontext().prec = 10

def get_unit_price(options, extra):

    # options
    height = Decimal(options['size']['height'])  # 高さ
    width = Decimal(options['size']['width'])  # 幅
    depth = Decimal(options['size']['depth'])  # 奥行き(縦)
    # color_num = Decimal(options['color_num']) # 色数
    # print_area_num = Decimal(options['print_area_num']) # 印刷面数
    # design_num = Decimal(options['design_num'])  # デザイン数
    quantity = Decimal(options['quantity'])  # 注文数
    surface_material = options['surface_material'] # 材質
    print_pattern = Decimal(options['print_pattern']) # 印刷範囲

    # 平米
    m = Decimal((2 * (width + depth) + 30) * (height + depth) / 1000000)

    # 紙代
    if surface_material == 'both_side_craft':
        p = m * 80
    elif surface_material == 'single_side_craft':
        p = m * 90
    else:
        raise ValidationError("Invalid surface material")

    # ロット総平米
    lm = m * quantity

    # FFG工賃
    if 0 <= lm < 40:
        ffg = 2500
    elif 40 <= lm <50:
        ffg = 4000
    elif 50<= lm < 75:
        ffg = 5000
    elif 75<= lm < 100:
        ffg = 6000
    elif 100<= lm < 150:
        ffg = 8000
    elif 150<= lm < 200:
        ffg = 10000
    elif 200<= lm < 300:
        ffg = 12000
    else :
        ffg = 14000

    # FFG工賃/枚
    ffg_1 = Decimal(ffg / quantity).quantize(Decimal('0.1'),rounding = ROUND_CEILING)

    # パス数
    if print_pattern == 1: # 側面のみ
        pasnum = ceil((height)/340)
    elif print_pattern == 2: # 側面上フラップ
        pasnum = ceil((height + Decimal(depth/2) )/340)
    else : # 全面
        pasnum = ceil((height + depth)/340)
    

    # デジタル時間
    digtime = Decimal((pasnum * 5 * quantity)/60)

    # デジタル加工賃
    if digtime <= 10:
        digpri = 10000
    else :
        digpri = Decimal((digtime - 10)*600 + 10000)

    dig_price = min(digpri, 43000)

    # デジタル加工賃/枚
    dig_price_1 = Decimal(dig_price / quantity)

    # インク代
    ink = pasnum * 7

    # 製品単価
    unit_price = Decimal(p + dig_price_1 + ink + ffg_1)

    # 運賃
    # 梱包箱サイズ
    pack_w = width + depth
    pack_l = depth + height

    pack_h_50 = 10*50
    pack_h_100 = 10*100

    # 50枚入りサイズ
    pack_50 = Decimal((pack_w + pack_l + pack_h_50) /10)
    # 100枚入りサイズ
    pack_100 = Decimal((pack_w + pack_l + pack_h_100) /10)

    # 50枚入り運賃
    if 0 <= pack_50 < 60:
        ship_50 = 900
    elif 60 <= pack_50 <140:
        ship_50 = 1000
    elif 140<= pack_50 < 160:
        ship_50 = 1300
    elif 160<= pack_50 < 170:
        ship_50 = 1700
    elif 170<= pack_50 < 180:
        ship_50 = 1900
    elif 180<= pack_50 < 200:
        ship_50 = 2300
    elif 200<= pack_50 < 220:
        ship_50 = 2700
    elif 220<= pack_50 < 240:
        ship_50 = 3500
    else :
        ship_50 = 4300
    
    # 100枚入り運賃
    if 0 <= pack_100 < 60:
        ship_100 = 900
    elif 60 <= pack_100 <140:
        ship_100 = 1000
    elif 140<= pack_100 < 160:
        ship_100 = 1300
    elif 160<= pack_100 < 170:
        ship_100 = 1700
    elif 170<= pack_100 < 180:
        ship_100 = 1900
    elif 180<= pack_100 < 200:
        ship_100 = 2300
    elif 200<= pack_100 < 220:
        ship_100 = 2700
    elif 220<= pack_100 < 240:
        ship_100 = 3500
    else :
        ship_100 = 4300
    
    # 福岡関東運賃（仮）
    kariship_50 = Decimal(ship_50/50)
    kariship_100 = Decimal(ship_100/100)

    ship = min(kariship_50, kariship_100)

    # 運賃込み単価
    return Decimal(unit_price + ship).quantize(Decimal('0.1'),rounding = ROUND_CEILING)


def get_plate_price(options):
    """版代
    """
    return Decimal(0)


def get_mold_price(options):
    """木型代
    """
    return Decimal(0)


def get_shipping_price(options):
    """配送料
    """
    return Decimal(0)
