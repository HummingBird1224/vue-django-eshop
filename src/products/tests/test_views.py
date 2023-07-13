from django.test import TestCase
from django.core.exceptions import ValidationError
from django.test import Client

from products.models import Product, ProductCategory


class ProductViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        root = ProductCategory.objects.create(name='root', slug='root', icon='')
        external = ProductCategory.objects.create(name='外部連携', slug='external', parent_category=root)
        flatbag = ProductCategory.objects.create(name='平袋', slug='flatbag', parent_category=root)
        cardboard = ProductCategory.objects.create(name='ダンボール', slug='cardboard', parent_category=root)
        paperbox = ProductCategory.objects.create(name='紙器', slug='paperbox', parent_category=root)

        smalllotflatbag = ProductCategory.objects.create(name='小ロット印刷', slug='small-lot-flatbag', parent_category=flatbag)
        innerbag = ProductCategory.objects.create(name='インナーバッグ', slug='innerbag', parent_category=flatbag)
        standbag = ProductCategory.objects.create(name='スタンド', slug='standbag', parent_category=flatbag)
        smallbag = ProductCategory.objects.create(name='小分け袋', slug='smallbag', parent_category=flatbag)
        aluminum = ProductCategory.objects.create(name='アルミ袋', slug='aluminum-bag', parent_category=flatbag)

        ProductCategory.objects.create(name='小ロット印刷', slug='small-lot-cardboard', parent_category=cardboard)
        mailbox = ProductCategory.objects.create(name='メール便対応', slug='mailbox', parent_category=cardboard)
        shipping = ProductCategory.objects.create(name='配送用', slug='shipping-cardboard', parent_category=cardboard)
        packaging = ProductCategory.objects.create(name='梱包/化粧箱', slug='packaging-box', parent_category=cardboard)

        base = ProductCategory.objects.create(name='BASE', slug='base', parent_category=external)
        colorme = ProductCategory.objects.create(name='COLORME', slug='colorme', parent_category=external)
        fujilogi = ProductCategory.objects.create(name='富士ロジテック', slug='fujilogi', parent_category=external)
        futureshop = ProductCategory.objects.create(name='FutureShop', slug='futureshop', parent_category=external)

        Product.objects.create(name='テープ付きOPP袋', slug='tape-opp-bag', category=innerbag)
        Product.objects.create(name='前透明アルミ袋', slug='aluminum-clear-bag', category=aluminum)
        Product.objects.create(name='ジップ付きアルミスタンド袋', slug='zip-aluminum-stand', category=standbag)
        Product.objects.create(name='小分け袋', slug='subsection-bag', category=smallbag)
        Product.objects.create(name='梱包箱N式', slug='ntype-corrugated', category=packaging)
        Product.objects.create(name='ポスト投函箱(たとう式)', slug='ttype', category=shipping)
        Product.objects.create(name='B式組み立て底', slug='folding-carton', category=paperbox)
        Product.objects.create(name='BASE限定デザイン袋', slug='base-original', category=base)
        Product.objects.create(name='テープ付きOPP袋 - 小ロット', slug='tape-opp-bag-small-lot', category=smalllotflatbag)
        Product.objects.create(name='配送箱(A式/みかん箱)', slug='colorme-atype', category=colorme)
        Product.objects.create(name='配送箱(A式)', slug='fujilogi-atype-small-lot', category=fujilogi)
        # Product.objects.create(name='配送箱(A式/みかん箱)', slug='futureshop-atype')

    def test_list_view(self):
        for category in ProductCategory.objects.all():
            res = self.client.get('/catalog/{}/'.format(category.slug))
            if category.get_parent_or_self().slug == 'external':
                self.assertEqual(res.status_code, 404)
            else:
                self.assertEqual(res.status_code, 200)

    def test_detail_view(self):
        for product in Product.objects.all():
            res = self.client.get('/catalog/{}/{}/'.format(product.category.slug, product.slug))
            if product.category.get_parent_or_self().slug == 'external':
                self.assertEqual(res.status_code, 404)
            else:
                self.assertEqual(res.status_code, 200)



