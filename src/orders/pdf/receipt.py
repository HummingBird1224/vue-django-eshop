from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
import os
from datetime import datetime


GENSHIN = os.path.join(os.path.dirname(__file__), 'fonts/GenShinGothic-Regular.ttf')
GENSHINB = os.path.join(os.path.dirname(__file__), 'fonts/GenShinGothic-P-Bold.ttf')
pdfmetrics.registerFont(TTFont('GenShinGothic', GENSHIN))
pdfmetrics.registerFont(TTFont('GenShinGothicBold', GENSHINB))


def draw_header(canvas):
    """ Draws the invoice header """
    canvas.setStrokeColorRGB(0.8, 0.8, 0.8)
    canvas.setFillColorRGB(0.2, 0.2, 0.2)
    canvas.setFont('GenShinGothic', 20)
    canvas.drawString(1* cm, -1.5 * cm, '領収書')
    canvas.setFont('GenShinGothic', 8)
    canvas.drawString(17 * cm, -1.2 * cm, '再発行日：{}'.format(datetime.today().strftime("%Y/%m/%d")))
    canvas.setLineWidth(2)
    canvas.line(1 * cm, -2.5 * cm, 20 * cm, -2.5 * cm)


def draw_address(canvas, item):
    """ Draws the business address """

    logo = os.path.join(os.path.dirname(__file__), 'imgs/icon.jpg')
    canvas.drawInlineImage(logo, 15 * cm, -4.5 * cm, 48, 30)

    canvas.setFont('GenShinGothic', 12)
    textobject = canvas.beginText(12 * cm, -5.5 * cm)
    textobject.textLine('福岡パッケージ株式会社')
    canvas.drawText(textobject)

    business_details = (
        '〒160-0022'
        '東京都新宿区新宿3丁目5-6 417',
        'support@canal.ink',
    )
    canvas.setFont('GenShinGothic', 10, leading=14)
    textobject = canvas.beginText(12 * cm, -6.2 * cm)
    for line in business_details:
        textobject.textLine(line)
    canvas.drawText(textobject)


def draw_footer(canvas):
    pass


def draw_pdf(buffer, item):
    """ Draws the invoice """
    canvas = Canvas(buffer, pagesize=A4)
    canvas.setTitle("領収書 | canal")
    canvas.translate(0, 29.7 * cm)
    # canvas.setFont('Helvetica', 10)

    canvas.saveState()
    draw_header(canvas)
    canvas.restoreState()

    canvas.saveState()
    draw_footer(canvas)
    canvas.restoreState()

    canvas.saveState()
    draw_address(canvas, item)
    canvas.restoreState()

    # Client name and address
    canvas.setFont('GenShinGothic', 12)
    textobject = canvas.beginText(5 * cm, -4.5 * cm)
    textobject.textLine('様')
    canvas.drawText(textobject)

    canvas.setStrokeColorRGB(0.9, 0.9, 0.9)
    canvas.setLineWidth(1)
    canvas.line(1 * cm, -4.5 * cm, 4.8 * cm, -4.5 * cm)

    canvas.setFont('GenShinGothicBold', 16)
    textobject = canvas.beginText(4 * cm, -7 * cm)
    textobject.textLine("¥ {:,}".format(item.total))
    canvas.drawText(textobject)
    canvas.setStrokeColorRGB(0.2, 0.2, 0.2)
    canvas.setLineWidth(1)
    canvas.line(1 * cm, -7.5 * cm, 10 * cm, -7.5 * cm)

    canvas.setFont('GenShinGothic', 7)
    textobject = canvas.beginText(1 * cm, -8 * cm)
    textobject.textLine('但し、商品代として上記金額を正に受領いたしました。')
    canvas.drawText(textobject)

    # Order info
    canvas.setFont('GenShinGothicBold', 12)
    textobject = canvas.beginText(1 * cm, -10.5 * cm)
    textobject.textLine('ご注文内容')
    canvas.drawText(textobject)

    canvas.setFont('GenShinGothic', 10, leading=14)
    textobject = canvas.beginText(1 * cm, -11.2 * cm)
    textobject.textLine("注文日　：{}".format(item.created_at.strftime("%Y/%m/%d")))
    textobject.textLine("注文番号：{}".format(item.ref_code))
    canvas.drawText(textobject)

    data = [['品目', '単価', '数量', '価格'], ]
    row_num = 7
    data.append([item.product_name, "{:,}円".format(item.unit_price), item.quantity, "{:,}円".format(item.product_total)])
    data.append(['版代', "{:,}円".format(item.plate_price), 1, "{:,}円".format(item.plate_price)])
    if item.mold_price:
        data.append(['木型代', "{:,}円".format(item.mold_price), 1, "{:,}円".format(item.mold_price)])
        row_num = 8
    data.append(['送料', "{:,}円".format(item.shipping_price), 1, "{:,}円".format(item.shipping_price)])

    data.append(['', '', '小計', '{:,} 円'.format(item.subtotal)])
    data.append(['', '', '消費税', '{:,} 円'.format(item.tax)])
    data.append(['', '', '合計(税込)', '{:,} 円'.format(item.total)])
    trans = item.order.get_transaction()
    if trans.type == 'credit_card':
        data.append(['', '', 'お支払い方法', 'クレジットカード'])
    elif trans.type == 'bank_transfer':
        data.append(['', '', 'お支払い方法', '銀行振込'])
    else:
        data.append(['', '', 'お支払い方法', 'クレジットカード'])
    rowHeights = [0.6 * cm, ] + [1 * cm for _ in range(row_num)]

    table = Table(data, colWidths=[10 * cm, 3 * cm, 3 * cm, 3 * cm], rowHeights=rowHeights)
    table.setStyle([
        ('FONT', (0, 0), (-1, -1), 'GenShinGothic'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), (0.2, 0.2, 0.2)),
        ('GRID', (0, 0), (-1, -5), 1, (0.95, 0.95, 0.95)),
        # ('GRID', (2, -3), (-1, -1), 1, (0.95, 0.95, 0.95)),
        ('LINEABOVE', (2, -2), (-1, -3), 1, (0.95, 0.95, 0.95)),
        ('LINEABOVE', (2, -3), (-1, -1), 1, (0.95, 0.95, 0.95)),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('BACKGROUND', (0, 0), (-1, 0), (0.85, 0.85, 0.85)),
        ('BACKGROUND', (0, 1), (-1, -5), (0.95, 0.95, 0.95)),
        ('LINEABOVE', (0, 1), (-1, -4), 1, (0.85, 0.85, 0.85)),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    tw, th, = table.wrapOn(canvas, 15 * cm, 19 * cm)
    table.drawOn(canvas, 1 * cm, -12 * cm - th)

    # Info
    canvas.setStrokeColorRGB(0.9, 0.9, 0.9)
    canvas.setLineWidth(1)
    canvas.line(1 * cm, -12.5 * cm - th, 20 * cm, -12.5 * cm - th)

    data = [['請求先住所', 'お届け先住所'], ]
    data.append([item.order.billing_address.get_full_name(),
                 item.delivery.get_full_name()])
    data.append([item.order.billing_address.get_full_address(),
                 item.delivery.get_full_address()])
    data.append(['〒' + item.order.billing_address.postal_code,
                 '〒' + item.delivery.postal_code])

    table = Table(data, colWidths=[10 * cm, 10 * cm],
                  rowHeights=[1.5 * cm, 1 * cm, 0.6 * cm, 0.6 * cm])
    table.setStyle([
        ('FONT', (0, 0), (-1, 1), 'GenShinGothicBold'),
        ('FONT', (0, 1), (-1, -1), 'GenShinGothic'),
        ('FONTSIZE', (0, 0), (-1, 1), 12),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), (0.2, 0.2, 0.2)),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ])
    tw2, th2, = table.wrapOn(canvas, 15 * cm, 19 * cm)
    table.drawOn(canvas, 1 * cm, -12.5 * cm - th - th2)

    canvas.setStrokeColorRGB(0.9, 0.9, 0.9)
    canvas.setLineWidth(1)
    canvas.line(1 * cm, -13.4 * cm - th - th2, 20 * cm, -13.4 * cm - th - th2)

    # Payment
    # canvas.setFont('GenShinGothicBold', 12)
    # textobject = canvas.beginText(1.2 * cm, -14.5 * cm - th - th2)
    # textobject.textLine('支払い情報')
    # canvas.drawText(textobject)

    canvas.showPage()
    canvas.save()


