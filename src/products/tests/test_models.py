from django.core.management import call_command
from django.test import TestCase
from django.core.exceptions import ValidationError

from products.models import Product


class ProductExtraInfoTestCase(TestCase):

    def setUp(self):
        Product.objects.create(name='テープ付きOPP袋', slug='tape-opp-bag')
        Product.objects.create(name='ジップ付き透明袋-圧着あり', slug='zip-clear-pressbag')
        Product.objects.create(name='ジップ付き透明袋-圧着なし', slug='zip-clear-bag')
        Product.objects.create(name='前透明アルミ袋', slug='aluminum-clear-bag')
        Product.objects.create(name='ジップ付き前透明アルミ袋', slug='zip-aluminum-clear-bag')
        Product.objects.create(name='ジップ付き不透明アルミ袋', slug='zip-aluminum-bag')
        Product.objects.create(name='テープ付き不透明袋', slug='tape-bag')
        Product.objects.create(name='ジップ付きアルミスタンド袋', slug='zip-aluminum-stand')
        Product.objects.create(name='ボックスパウチ', slug='aluminum-pouche')
        Product.objects.create(name='小分け袋', slug='subsection-bag')
        Product.objects.create(name='梱包箱N式', slug='ntype-corrugated')
        Product.objects.create(name='配送箱N式', slug='ntype-mailer')
        Product.objects.create(name='配送箱(A式/みかん箱)', slug='atype')
        Product.objects.create(name='ポスト投函箱(たとう式)', slug='ttype')
        Product.objects.create(name='フタ付き箱(C式)', slug='ctype')
        Product.objects.create(name='梱包箱 - カスタムカット付き', slug='ntype-custominsert')
        Product.objects.create(name='B式組み立て底', slug='folding-carton')
        Product.objects.create(name='BASE限定デザイン袋', slug='base-original')
        Product.objects.create(name='配送箱(A式)', slug='base-atype')
        Product.objects.create(name='配送箱(A式/みかん箱) - 無地', slug='base-atype-plain')
        Product.objects.create(name='梱包箱N式', slug='base-ntype-corrugated')
        Product.objects.create(name='配送箱(A式)-小ロット', slug='base-atype-smalllot')
        Product.objects.create(name='配送箱N式', slug='base-ntype-mailer')
        Product.objects.create(name='たとう式', slug='base-ttype')
        Product.objects.create(name='テープ付きOPP袋', slug='base-tape-opp-bag')
        Product.objects.create(name='ジップ付き袋', slug='base-zip-bag')
        Product.objects.create(name='ジップ付き前透明アルミ袋', slug='base-zip-aluminum-clear-bag')
        Product.objects.create(name='テープ付き不透明袋', slug='base-tape-bag')
        Product.objects.create(name='ジップ付き不透明アルミ袋', slug='base-zip-aluminum-bag')
        Product.objects.create(name='ジップ付きアルミスタンド袋', slug='base-zip-aluminum-stand')
        Product.objects.create(name='持ち手付きクラフト紙袋', slug='base-handle-craft-paperbag')
        Product.objects.create(name='持ち手付きホワイト紙袋', slug='base-handle-white-paperbag')
        Product.objects.create(name='テープ付きOPP袋 - 小ロット', slug='tape-opp-bag-small-lot')
        Product.objects.create(name='ジップ付き前透明アルミ袋 - 小ロット', slug='zip-aluminum-clear-bag-small-lot')
        Product.objects.create(name='ジップ付き透明袋（圧着なし） - 小ロット', slug='zip-clear-bag-small-lot')
        Product.objects.create(name='ジップ付きアルミスタンド袋 - 小ロット', slug='zip-aluminum-stand-small-lot')
        Product.objects.create(name='ジップ付き不透明アルミ袋 - 小ロット', slug='zip-aluminum-bag-small-lot')
        Product.objects.create(name='テープ付き不透明袋 - 小ロット', slug='tape-bag-small-lot')
        Product.objects.create(name='配送箱(A式/みかん箱) - 小ロット', slug='atype-small-lot')
        Product.objects.create(name='配送箱N式 - 小ロット', slug='ntype-mailer-small-lot')
        Product.objects.create(name='梱包箱N式 - 小ロット', slug='ntype-corrugated-small-lot')
        Product.objects.create(name='ポスト投函箱(たとう式) - 小ロット', slug='ttype-small-lot')
        Product.objects.create(name='配送箱(A式/みかん箱)', slug='colorme-atype')
        Product.objects.create(name='配送箱(A式/みかん箱) - 無地', slug='colorme-atype-plain')
        Product.objects.create(name='梱包箱N式', slug='colorme-ntype-corrugated')
        Product.objects.create(name='配送箱N式', slug='colorme-ntype-mailer')
        Product.objects.create(name='たとう式', slug='colorme-ttype')
        Product.objects.create(name='テープ付きOPP袋', slug='colorme-tape-opp-bag')
        Product.objects.create(name='ジップ付き袋', slug='colorme-zip-clear-bag')
        Product.objects.create(name='ジップ付き前透明アルミ袋', slug='colorme-zip-aluminum-clear-bag')
        Product.objects.create(name='テープ付き不透明袋', slug='colorme-tape-bag')
        Product.objects.create(name='ジップ付き不透明アルミ袋', slug='colorme-zip-aluminum-bag')
        Product.objects.create(name='ジップ付きアルミスタンド袋', slug='colorme-zip-aluminum-stand')
        Product.objects.create(name='持ち手付きクラフト紙袋', slug='colorme-handle-craft-paperbag')
        Product.objects.create(name='持ち手付きホワイト紙袋', slug='colorme-handle-white-paperbag')
        Product.objects.create(name='配送箱(A式)', slug='fujilogi-atype-small-lot')
        Product.objects.create(name='テープ付きOPP袋', slug='fujilogi-tape-opp-bag')
        Product.objects.create(name='ジップ付き袋', slug='fujilogi-zip-bag')
        Product.objects.create(name='配送箱(A式/みかん箱) - 無地', slug='atype-plain')
        # Product.objects.create(name='配送箱(A式/みかん箱)', slug='futureshop-atype')
        # Product.objects.create(name='配送箱(A式/みかん箱) - 無地', slug='futureshop-atype-plain')
        # Product.objects.create(name='梱包箱N式', slug='futureshop-ntype-corrugated')
        # Product.objects.create(name='配送箱N式', slug='futureshop-ntype-mailer')
        # Product.objects.create(name='たとう式', slug='futureshop-ttype')
        # Product.objects.create(name='テープ付きOPP袋', slug='futureshop-tape-opp-bag')
        # Product.objects.create(name='ジップ付き袋', slug='futureshop-zip-clear-bag')
        # Product.objects.create(name='ジップ付き前透明アルミ袋', slug='futureshop-zip-aluminum-clear-bag')
        # Product.objects.create(name='テープ付き不透明袋', slug='futureshop-tape-bag')
        # Product.objects.create(name='ジップ付き不透明アルミ袋', slug='futureshop-zip-aluminum-bag')
        # Product.objects.create(name='ジップ付きアルミスタンド袋', slug='futureshop-zip-aluminum-stand')
        # Product.objects.create(name='持ち手付きクラフト紙袋', slug='futureshop-handle-craft-paperbag')
        # Product.objects.create(name='持ち手付きホワイト紙袋', slug='futureshop-handle-white-paperbag')
        call_command('import_extra_data')

    def test_all_products(self):
        fields = [
            'contact_required',
            'sample_order',
            'small_lot_availability',
            'min_ordering_quantity',
            'max_ordering_quantity',
            'estimated_shipping_date',
            'is_design_unnecessary',
            'is_easy_draft_available',
            'can_select_original_size',
            'print_area',
            'notes',
            'example',
            'size_limit',
            'shipping_area',
            'required_fields',
        ]

        products = Product.objects.all()
        for product in products:
            for field in fields:
                if field not in product.extra_info:
                    raise ValidationError("Fields unsatisfied. Product: {}, Field: {}.".format(product.slug, field))




