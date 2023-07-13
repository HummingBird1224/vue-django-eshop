import csv
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from products.prices import (
    # flatbag
    aluminum_pouche,
    tape_opp_bag,
    zip_clear_bag,
    zip_clear_pressbag,
    zip_aluminum_bag,
    zip_aluminum_stand,
    # cardboard
    ntype_corrugated,
    ntype_mailer,
    atype,
    ttype,
    # paperbox
    folding_carton,
)


# TODO: ./commands/csv/下に商品ごとに出したいデータのcsvを作る
class Command(BaseCommand):
    help = 'Export price list as a csv file.'

    def add_arguments(self, parser):
        parser.add_argument('-o', '--output', required=True, type=str)

    def handle(self, *args, **kwargs):
        products = [
            # flatbag
            'tape_opp_bag',
            'zip_clear_bag',
            'zip_clear_pressbag',
            'zip_aluminum_bag',
            'zip_aluminum_stand',
            # cardboard
            'ntype_corrugated',
            'ntype_mailer',
            'atype',
            'ttype',
            # paperbox
            'folding_carton',
        ]

        with open(kwargs['output'], 'w', newline='') as csvfile:
            fieldnames = ['name', 'condition']
            for _ in range(100, 30001, 100):
                fieldnames.append(str(_))
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            self.test_tape_opp_bag_estimation(writer)
            self.test_zip_clear_pressbag_estimation(writer)
            self.test_zip_clear_bag_estimation(writer)
            self.test_zip_aluminum_bag_estimation(writer)
            self.test_zip_aluminum_stand_estimation(writer)
            self.test_aluminum_pouche_estimation(writer)
            self.test_ntype_corrugated_estimation(writer)
            self.test_ntype_mailer_estimation(writer)
            self.test_atype_estimation(writer)
            self.test_ttype_estimation(writer)
            self.test_folding_carton_estimation(writer)

    def test_tape_opp_bag_estimation(self, writer):
        conditions = [
            {'color_num': 1, 'height': 305, 'width': 225},
            {'color_num': 1, 'height': 220, 'width': 160},
            {'color_num': 1, 'height': 155, 'width': 110},
            {'color_num': 1, 'height': 370, 'width': 250},
            {'color_num': 1, 'height': 400, 'width': 300},
            {'color_num': 1, 'height': 550, 'width': 400},
            {'color_num': 1, 'height': 305, 'width': 225},
            {'color_num': 1, 'height': 220, 'width': 160},
            {'color_num': 1, 'height': 155, 'width': 110},
        ]
        for cond in conditions:
            res = {
                'name': 'tape_opp_bag',
                'condition': 'color_num: {}, height: {}, width: {},'.format(cond['color_num'], cond['height'], cond['width'])
            }
            start_from = 100 if cond['color_num'] in [1, 2] else 3000
            for q in range(start_from, 30001, 100):
                val = {'color_num': cond['color_num'],
                       'height': cond['height'],
                       'width': cond['width'],
                       'quantity': q}
                try:
                    price = tape_opp_bag._get_unit_price(val, {})
                    res[str(q)] = price
                except ValidationError:
                    res[str(q)] = 'quantity too small'
            writer.writerow(res)

    def test_zip_clear_pressbag_estimation(self, writer):
        conditions = [
            {'color_num': 1, 'height': 210, 'width': 180},
            {'color_num': 1, 'height': 265, 'width': 190},
            {'color_num': 2, 'height': 210, 'width': 180},
            {'color_num': 2, 'height': 265, 'width': 190},
            {'color_num': 3, 'height': 210, 'width': 180},
            {'color_num': 3, 'height': 265, 'width': 190},
            {'color_num': 4, 'height': 210, 'width': 180},
            {'color_num': 4, 'height': 265, 'width': 190},
            {'color_num': 1, 'height': 160, 'width': 140},
            {'color_num': 2, 'height': 160, 'width': 140},
            {'color_num': 3, 'height': 160, 'width': 140},
            {'color_num': 4, 'height': 160, 'width': 140},
        ]
        for cond in conditions:
            res = {
                'name': 'zip_clear_pressbag',
                'condition': 'color_num: {}, height: {}, width: {},'.format(cond['color_num'], cond['height'], cond['width'])
            }
            for q in range(3000, 30001, 100):
                val = {'color_num': cond['color_num'],
                       'height': cond['height'],
                       'width': cond['width'],
                       'quantity': q}
                try:
                    price = zip_clear_pressbag._get_unit_price(val, {})
                    res[str(q)] = price
                except ValidationError:
                    res[str(q)] = 'quantity too small'
            writer.writerow(res)

    def test_zip_clear_bag_estimation(self, writer):
        conditions = [
            {'color_num': 1, 'height': 140, 'width': 100},
            {'color_num': 1, 'height': 170, 'width': 120},
            {'color_num': 1, 'height': 240, 'width': 170},
            {'color_num': 1, 'height': 340, 'width': 240},
            {'color_num': 1, 'height': 480, 'width': 340},
            {'color_num': 2, 'height': 140, 'width': 100},
            {'color_num': 2, 'height': 170, 'width': 120},
            {'color_num': 2, 'height': 240, 'width': 170},
            {'color_num': 2, 'height': 340, 'width': 240},
            {'color_num': 2, 'height': 480, 'width': 340},
            {'color_num': 3, 'height': 140, 'width': 100},
            {'color_num': 3, 'height': 170, 'width': 120},
            {'color_num': 3, 'height': 240, 'width': 170},
            {'color_num': 3, 'height': 340, 'width': 240},
            {'color_num': 3, 'height': 480, 'width': 340},
            {'color_num': 4, 'height': 140, 'width': 100},
            {'color_num': 4, 'height': 170, 'width': 120},
            {'color_num': 4, 'height': 240, 'width': 170},
            {'color_num': 4, 'height': 340, 'width': 240},
            {'color_num': 4, 'height': 480, 'width': 340},
            {'color_num': -1, 'height': 140, 'width': 100},
            {'color_num': -1, 'height': 170, 'width': 120},
            {'color_num': -1, 'height': 240, 'width': 170},
            {'color_num': -1, 'height': 340, 'width': 240},
            {'color_num': -1, 'height': 480, 'width': 340},
        ]
        for cond in conditions:
            res = {
                'name': 'zip_clear_bag',
                'condition': 'color_num: {}, height: {}, width: {},'.format(cond['color_num'], cond['height'], cond['width'])
            }
            start_from = 100 if cond['color_num'] in [1] else 3000
            for q in range(start_from, 30001, 100):
                val = {'color_num': cond['color_num'],
                       'height': cond['height'],
                       'width': cond['width'],
                       'quantity': q}
                try:
                    price = zip_clear_bag._get_unit_price(val, {})
                    res[str(q)] = price
                except ValidationError:
                    res[str(q)] = 'quantity too small'
            writer.writerow(res)

    def test_zip_aluminum_bag_estimation(self, writer):
        conditions = [
            {'color_num': 1, 'height': 210, 'width': 180, 'material': 'normal'},
            {'color_num': 1, 'height': 265, 'width': 190, 'material': 'normal'},
            {'color_num': 1, 'height': 210, 'width': 180, 'material': 'mattepet'},
            {'color_num': 1, 'height': 265, 'width': 190, 'material': 'mattepet'},
            {'color_num': 1, 'height': 210, 'width': 180, 'material': 'highmatte'},
            {'color_num': 1, 'height': 265, 'width': 190, 'material': 'highmatte'},
            {'color_num': 2, 'height': 210, 'width': 180, 'material': 'normal'},
            {'color_num': 2, 'height': 265, 'width': 190, 'material': 'normal'},
            {'color_num': 2, 'height': 210, 'width': 180, 'material': 'mattepet'},
            {'color_num': 2, 'height': 265, 'width': 190, 'material': 'mattepet'},
            {'color_num': 2, 'height': 210, 'width': 180, 'material': 'highmatte'},
            {'color_num': 2, 'height': 265, 'width': 190, 'material': 'highmatte'},
            {'color_num': 3, 'height': 210, 'width': 180, 'material': 'normal'},
            {'color_num': 3, 'height': 265, 'width': 190, 'material': 'normal'},
            {'color_num': 3, 'height': 210, 'width': 180, 'material': 'mattepet'},
            {'color_num': 3, 'height': 265, 'width': 190, 'material': 'mattepet'},
            {'color_num': 3, 'height': 210, 'width': 180, 'material': 'highmatte'},
            {'color_num': 3, 'height': 265, 'width': 190, 'material': 'highmatte'},
            {'color_num': 1, 'height': 160, 'width': 140, 'material': 'mattepet'},
            {'color_num': 2, 'height': 160, 'width': 140, 'material': 'mattepet'},
            {'color_num': 3, 'height': 160, 'width': 140, 'material': 'mattepet'},
            {'color_num': 4, 'height': 160, 'width': 140, 'material': 'mattepet'},
        ]
        for cond in conditions:
            res = {
                'name': 'zip_aluminum_bag',
                'condition': 'color_num: {}, height: {}, width: {}, material: {}'.format(
                    cond['color_num'],
                    cond['height'],
                    cond['width'],
                    cond['material'],
                )
            }
            for q in range(3000, 30001, 100):
                val = {'color_num': cond['color_num'],
                       'height': cond['height'],
                       'width': cond['width'],
                       'material': cond['material'],
                       'quantity': q}
                try:
                    price = zip_aluminum_bag._get_unit_price(val, {})
                    res[str(q)] = price
                except ValidationError:
                    res[str(q)] = 'quantity too small'
            writer.writerow(res)

    def test_zip_aluminum_stand_estimation(self, writer):
        conditions = [
            {'color_num': 1, 'height': 310, 'width': 250, 'depth': 100,'material': 'normal'},
            {'color_num': 1, 'height': 220, 'width': 160, 'depth': 74,'material': 'normal'},
            {'color_num': 1, 'height': 200, 'width': 120, 'depth': 70,'material': 'normal'},
            {'color_num': 1, 'height': 310, 'width': 250, 'depth': 100, 'material': 'mattepet'},
            {'color_num': 1, 'height': 220, 'width': 160, 'depth': 74, 'material': 'mattepet'},
            {'color_num': 1, 'height': 200, 'width': 120, 'depth': 70, 'material': 'mattepet'},
            {'color_num': 1, 'height': 310, 'width': 250, 'depth': 100, 'material': 'highmatte'},
            {'color_num': 1, 'height': 220, 'width': 160, 'depth': 74, 'material': 'highmatte'},
            {'color_num': 1, 'height': 200, 'width': 120, 'depth': 70, 'material': 'highmatte'},
            {'color_num': 2, 'height': 310, 'width': 250, 'depth': 100, 'material': 'normal'},
            {'color_num': 2, 'height': 220, 'width': 160, 'depth': 74, 'material': 'normal'},
            {'color_num': 2, 'height': 200, 'width': 120, 'depth': 70, 'material': 'normal'},
            {'color_num': 2, 'height': 310, 'width': 250, 'depth': 100, 'material': 'mattepet'},
            {'color_num': 2, 'height': 220, 'width': 160, 'depth': 74, 'material': 'mattepet'},
            {'color_num': 2, 'height': 200, 'width': 120, 'depth': 70, 'material': 'mattepet'},
            {'color_num': 2, 'height': 310, 'width': 250, 'depth': 100, 'material': 'highmatte'},
            {'color_num': 2, 'height': 220, 'width': 160, 'depth': 74, 'material': 'highmatte'},
            {'color_num': 2, 'height': 200, 'width': 120, 'depth': 70, 'material': 'highmatte'},
            {'color_num': 3, 'height': 310, 'width': 250, 'depth': 100, 'material': 'normal'},
            {'color_num': 3, 'height': 220, 'width': 160, 'depth': 74, 'material': 'normal'},
            {'color_num': 3, 'height': 200, 'width': 120, 'depth': 70, 'material': 'normal'},
            {'color_num': 3, 'height': 310, 'width': 250, 'depth': 100, 'material': 'mattepet'},
            {'color_num': 3, 'height': 220, 'width': 160, 'depth': 74, 'material': 'mattepet'},
            {'color_num': 3, 'height': 200, 'width': 120, 'depth': 70, 'material': 'mattepet'},
            {'color_num': 3, 'height': 310, 'width': 250, 'depth': 100, 'material': 'highmatte'},
            {'color_num': 3, 'height': 220, 'width': 160, 'depth': 74, 'material': 'highmatte'},
            {'color_num': 3, 'height': 200, 'width': 120, 'depth': 70, 'material': 'highmatte'},
            {'color_num': 3, 'height': 310, 'width': 250, 'depth': 100, 'material': 'normal'},
            {'color_num': 4, 'height': 220, 'width': 160, 'depth': 74, 'material': 'normal'},
            {'color_num': 4, 'height': 200, 'width': 120, 'depth': 70, 'material': 'normal'},
            {'color_num': 4, 'height': 310, 'width': 250, 'depth': 100, 'material': 'mattepet'},
            {'color_num': 4, 'height': 220, 'width': 160, 'depth': 74, 'material': 'mattepet'},
            {'color_num': 4, 'height': 200, 'width': 120, 'depth': 70, 'material': 'mattepet'},
            {'color_num': 4, 'height': 310, 'width': 250, 'depth': 100, 'material': 'highmatte'},
            {'color_num': 4, 'height': 220, 'width': 160, 'depth': 74, 'material': 'highmatte'},
            {'color_num': 4, 'height': 200, 'width': 120, 'depth': 70, 'material': 'highmatte'},
            {'color_num': 4, 'height': 310, 'width': 250, 'depth': 100, 'material': 'normal'},
            {'color_num': -1, 'height': 220, 'width': 160, 'depth': 74, 'material': 'normal'},
            {'color_num': -1, 'height': 200, 'width': 120, 'depth': 70, 'material': 'normal'},
            {'color_num': -1, 'height': 310, 'width': 250, 'depth': 100, 'material': 'mattepet'},
            {'color_num': -1, 'height': 220, 'width': 160, 'depth': 74, 'material': 'mattepet'},
            {'color_num': -1, 'height': 200, 'width': 120, 'depth': 70, 'material': 'mattepet'},
            {'color_num': -1, 'height': 310, 'width': 250, 'depth': 100, 'material': 'highmatte'},
            {'color_num': -1, 'height': 220, 'width': 160, 'depth': 74, 'material': 'highmatte'},
            {'color_num': -1, 'height': 200, 'width': 120, 'depth': 70, 'material': 'highmatte'},
        ]
        for cond in conditions:
            res = {
                'name': 'zip_aluminum_stand',
                'condition': 'color_num: {}, height: {}, width: {}, depth: {}, material: {}'.format(
                    cond['color_num'],
                    cond['height'],
                    cond['width'],
                    cond['depth'],
                    cond['material'],
                )
            }
            for q in range(3000, 30001, 100):
                val = {'color_num': cond['color_num'],
                       'height': cond['height'],
                       'width': cond['width'],
                       'depth': cond['depth'],
                       'material': cond['material'],
                       'quantity': q}
                try:
                    price = zip_aluminum_stand._get_unit_price(val, {})
                    res[str(q)] = price
                except ValidationError:
                    res[str(q)] = 'quantity too small'
            writer.writerow(res)

    def test_aluminum_pouche_estimation(self, writer):
        conditions = [
            {'color_num': 1, 'height': 310, 'width': 220, 'depth': 140,'material': 'normal'},
            {'color_num': 1, 'height': 220, 'width': 160, 'depth': 90,'material': 'normal'},
            {'color_num': 1, 'height': 200, 'width': 120, 'depth': 60,'material': 'normal'},
            {'color_num': 1, 'height': 310, 'width': 220, 'depth': 140, 'material': 'mattepet'},
            {'color_num': 1, 'height': 220, 'width': 160, 'depth': 90, 'material': 'mattepet'},
            {'color_num': 1, 'height': 200, 'width': 120, 'depth': 60, 'material': 'mattepet'},
            {'color_num': 1, 'height': 310, 'width': 220, 'depth': 140, 'material': 'highmatte'},
            {'color_num': 1, 'height': 220, 'width': 160, 'depth': 90, 'material': 'highmatte'},
            {'color_num': 1, 'height': 200, 'width': 120, 'depth': 60, 'material': 'highmatte'},
            {'color_num': 2, 'height': 310, 'width': 220, 'depth': 140, 'material': 'normal'},
            {'color_num': 2, 'height': 220, 'width': 160, 'depth': 90, 'material': 'normal'},
            {'color_num': 2, 'height': 200, 'width': 120, 'depth': 60, 'material': 'normal'},
            {'color_num': 2, 'height': 310, 'width': 220, 'depth': 140, 'material': 'mattepet'},
            {'color_num': 2, 'height': 220, 'width': 160, 'depth': 90, 'material': 'mattepet'},
            {'color_num': 2, 'height': 200, 'width': 120, 'depth': 60, 'material': 'mattepet'},
            {'color_num': 2, 'height': 310, 'width': 220, 'depth': 140, 'material': 'highmatte'},
            {'color_num': 2, 'height': 220, 'width': 160, 'depth': 90, 'material': 'highmatte'},
            {'color_num': 2, 'height': 200, 'width': 120, 'depth': 60, 'material': 'highmatte'},
            {'color_num': 3, 'height': 310, 'width': 220, 'depth': 140, 'material': 'normal'},
            {'color_num': 3, 'height': 220, 'width': 160, 'depth': 90, 'material': 'normal'},
            {'color_num': 3, 'height': 200, 'width': 120, 'depth': 60, 'material': 'normal'},
            {'color_num': 3, 'height': 310, 'width': 220, 'depth': 140, 'material': 'mattepet'},
            {'color_num': 3, 'height': 220, 'width': 160, 'depth': 90, 'material': 'mattepet'},
            {'color_num': 3, 'height': 200, 'width': 120, 'depth': 60, 'material': 'mattepet'},
            {'color_num': 3, 'height': 310, 'width': 220, 'depth': 140, 'material': 'highmatte'},
            {'color_num': 3, 'height': 220, 'width': 160, 'depth': 90, 'material': 'highmatte'},
            {'color_num': 3, 'height': 200, 'width': 120, 'depth': 60, 'material': 'highmatte'},
            {'color_num': 3, 'height': 310, 'width': 220, 'depth': 140, 'material': 'normal'},
            {'color_num': 4, 'height': 220, 'width': 160, 'depth': 90, 'material': 'normal'},
            {'color_num': 4, 'height': 200, 'width': 120, 'depth': 60, 'material': 'normal'},
            {'color_num': 4, 'height': 310, 'width': 220, 'depth': 140, 'material': 'mattepet'},
            {'color_num': 4, 'height': 220, 'width': 160, 'depth': 90, 'material': 'mattepet'},
            {'color_num': 4, 'height': 200, 'width': 120, 'depth': 60, 'material': 'mattepet'},
            {'color_num': 4, 'height': 310, 'width': 220, 'depth': 140, 'material': 'highmatte'},
            {'color_num': 4, 'height': 220, 'width': 160, 'depth': 90, 'material': 'highmatte'},
            {'color_num': 4, 'height': 200, 'width': 120, 'depth': 60, 'material': 'highmatte'},
            {'color_num': 4, 'height': 310, 'width': 220, 'depth': 140, 'material': 'normal'},
            {'color_num': -1, 'height': 220, 'width': 160, 'depth':904, 'material': 'normal'},
            {'color_num': -1, 'height': 200, 'width': 120, 'depth':670, 'material': 'normal'},
            {'color_num': -1, 'height': 310, 'width': 220, 'depth': 140, 'material': 'mattepet'},
            {'color_num': -1, 'height': 220, 'width': 160, 'depth': 90, 'material': 'mattepet'},
            {'color_num': -1, 'height': 200, 'width': 120, 'depth': 60, 'material': 'mattepet'},
            {'color_num': -1, 'height': 310, 'width': 220, 'depth': 140, 'material': 'highmatte'},
            {'color_num': -1, 'height': 220, 'width': 160, 'depth': 90, 'material': 'highmatte'},
            {'color_num': -1, 'height': 200, 'width': 120, 'depth': 60, 'material': 'highmatte'},
        ]
        for cond in conditions:
            res = {
                'name': 'aluminum_pouche',
                'condition': 'color_num: {}, height: {}, width: {}, depth: {}, material: {}'.format(
                    cond['color_num'],
                    cond['height'],
                    cond['width'],
                    cond['depth'],
                    cond['material'],
                )
            }
            for q in range(3000, 30001, 100):
                val = {'color_num': cond['color_num'],
                       'height': cond['height'],
                       'width': cond['width'],
                       'depth': cond['depth'],
                       'material': cond['material'],
                       'quantity': q}
                try:
                    price = aluminum_pouche._get_unit_price(val, {})
                    res[str(q)] = price
                except ValidationError:
                    res[str(q)] = 'quantity too small'
            writer.writerow(res)

    def test_ntype_corrugated_estimation(self, writer):
        conditions = [
            {'color_num': 1, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 1, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 1, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'laminating', 'surface_process': 'mattevarnish'},
            {'color_num': 1, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'laminating', 'surface_process': 'mattevarnish'},
            {'color_num': 1, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'laminating', 'surface_process': 'mattepp'},
            {'color_num': 1, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'laminating', 'surface_process': 'mattepp'},
            {'color_num': 2, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'laminating', 'surface_process': 'mattevarnish'},
            {'color_num': 2, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'laminating', 'surface_process': 'mattevarnish'},
            {'color_num': 2, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'laminating', 'surface_process': 'mattepp'},
            {'color_num': 2, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'laminating', 'surface_process': 'mattepp'},
            {'color_num': 3, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 3, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 3, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 3, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 3, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'laminating', 'surface_process': 'mattevarnish'},
            {'color_num': 3, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'laminating', 'surface_process': 'mattevarnish'},
            {'color_num': 3, 'height': 80, 'width': 220, 'depth': 140,
             'surface_material': 'laminating', 'surface_process': 'mattepp'},
            {'color_num': 3, 'height': 40, 'width': 260, 'depth': 200,
             'surface_material': 'laminating', 'surface_process': 'mattepp'},
        ]
        for cond in conditions:
            res = {
                'name': 'ntype_corrugated',
                'condition': 'color_num: {}, height: {}, width: {}, depth: {}, surface_material: {}, surface_process: {}'.format(
                    cond['color_num'],
                    cond['height'],
                    cond['width'],
                    cond['depth'],
                    cond['surface_material'],
                    cond['surface_process'],
                )
            }
            for q in range(100, 30001, 100):
                val = {'color_num': cond['color_num'],
                       'height': cond['height'],
                       'width': cond['width'],
                       'depth': cond['depth'],
                       'surface_material': cond['surface_material'],
                       'surface_process': cond['surface_process'],
                       'quantity': q}
                try:
                    price = ntype_corrugated._get_unit_price(val, {})
                    res[str(q)] = price
                except ValidationError as e:
                    res[str(q)] = 'quantity too small'
            writer.writerow(res)

    def test_ntype_mailer_estimation(self, writer):
        conditions = [
            {'color_num': 1, 'height': 100, 'width': 350, 'depth': 270,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 50, 'width': 250, 'depth': 220,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 100, 'width': 350, 'depth': 270,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 1, 'height': 50, 'width': 250, 'depth': 220,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 100, 'width': 350, 'depth': 270,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 50, 'width': 250, 'depth': 220,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 100, 'width': 350, 'depth': 270,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 50, 'width': 250, 'depth': 220,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 3, 'height': 100, 'width': 350, 'depth': 270,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 3, 'height': 50, 'width': 250, 'depth': 220,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 3, 'height': 100, 'width': 350, 'depth': 270,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 3, 'height': 50, 'width': 250, 'depth': 220,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 4, 'height': 100, 'width': 350, 'depth': 270,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 4, 'height': 50, 'width': 250, 'depth': 220,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 4, 'height': 100, 'width': 350, 'depth': 270,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 4, 'height': 50, 'width': 250, 'depth': 220,
             'surface_material': 'white', 'surface_process': 'none'},
        ]
        for cond in conditions:
            res = {
                'name': 'ntype_mailer',
                'condition': 'color_num: {}, height: {}, width: {}, depth: {}, surface_material: {}'.format(
                    cond['color_num'],
                    cond['height'],
                    cond['width'],
                    cond['depth'],
                    cond['surface_material'],
                )
            }
            for q in range(100, 30001, 100):
                val = {'color_num': cond['color_num'],
                       'height': cond['height'],
                       'width': cond['width'],
                       'depth': cond['depth'],
                       'surface_material': cond['surface_material'],
                       'surface_process': cond['surface_process'],
                       'quantity': q}
                try:
                    price = ntype_mailer._get_unit_price(val, {})
                    res[str(q)] = price
                except ValidationError:
                    res[str(q)] = 'quantity too small'
            writer.writerow(res)

    def test_atype_estimation(self, writer):
        conditions = [
            {'color_num': 1, 'height': 120, 'width': 270, 'depth': 200,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 120, 'width': 270, 'depth': 200,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 160, 'width': 350, 'depth': 250,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 300, 'width': 380, 'depth': 280,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 500, 'width': 550, 'depth': 500,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 390, 'width': 450, 'depth': 340,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 350, 'width': 610, 'depth': 410,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 120, 'width': 270, 'depth': 200,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 1, 'height': 160, 'width': 350, 'depth': 250,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 1, 'height': 300, 'width': 380, 'depth': 280,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 1, 'height': 500, 'width': 550, 'depth': 500,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 1, 'height': 390, 'width': 450, 'depth': 340,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 1, 'height': 350, 'width': 610, 'depth': 410,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 120, 'width': 270, 'depth': 200,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 160, 'width': 350, 'depth': 250,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 300, 'width': 380, 'depth': 280,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 500, 'width': 550, 'depth': 500,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 390, 'width': 450, 'depth': 340,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 350, 'width': 610, 'depth': 410,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 120, 'width': 270, 'depth': 200,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 160, 'width': 350, 'depth': 250,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 300, 'width': 380, 'depth': 280,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 500, 'width': 550, 'depth': 500,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 390, 'width': 450, 'depth': 340,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 350, 'width': 610, 'depth': 410,
             'surface_material': 'white', 'surface_process': 'none'},
        ]
        for cond in conditions:
            res = {
                'name': 'atype',
                'condition': 'color_num: {}, height: {}, width: {}, depth: {}, surface_material: {}'.format(
                    cond['color_num'],
                    cond['height'],
                    cond['width'],
                    cond['depth'],
                    cond['surface_material'],
                )
            }
            for q in range(100, 30001, 100):
                val = {'color_num': cond['color_num'],
                       'height': cond['height'],
                       'width': cond['width'],
                       'depth': cond['depth'],
                       'surface_material': cond['surface_material'],
                       'surface_process': cond['surface_process'],
                       'quantity': q}
                try:
                    price = atype._get_unit_price(val, {})
                    res[str(q)] = price
                except ValidationError as e:
                    print(e)
                    res[str(q)] = 'quantity too small'
            writer.writerow(res)

    def test_ttype_estimation(self, writer):
        conditions = [
            {'color_num': 1, 'height': 30, 'width': 340, 'depth': 250,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 25, 'width': 220, 'depth': 160,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 25, 'width': 160, 'depth': 115,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 25, 'width': 300, 'depth': 220,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 1, 'height': 30, 'width': 340, 'depth': 250,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 1, 'height': 25, 'width': 220, 'depth': 160,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 1, 'height': 25, 'width': 160, 'depth': 115,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 1, 'height': 25, 'width': 300, 'depth': 220,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 30, 'width': 340, 'depth': 250,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 25, 'width': 220, 'depth': 160,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 25, 'width': 160, 'depth': 115,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 25, 'width': 300, 'depth': 220,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 2, 'height': 30, 'width': 340, 'depth': 250,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 25, 'width': 220, 'depth': 160,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 25, 'width': 160, 'depth': 115,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 2, 'height': 25, 'width': 300, 'depth': 220,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 3, 'height': 30, 'width': 340, 'depth': 250,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 3, 'height': 25, 'width': 220, 'depth': 160,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 3, 'height': 25, 'width': 160, 'depth': 115,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 3, 'height': 25, 'width': 300, 'depth': 220,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 3, 'height': 30, 'width': 340, 'depth': 250,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 3, 'height': 25, 'width': 220, 'depth': 160,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 3, 'height': 25, 'width': 160, 'depth': 115,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 3, 'height': 25, 'width': 300, 'depth': 220,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 4, 'height': 30, 'width': 340, 'depth': 250,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 4, 'height': 25, 'width': 220, 'depth': 160,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 4, 'height': 25, 'width': 160, 'depth': 115,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 4, 'height': 25, 'width': 300, 'depth': 220,
             'surface_material': 'normal', 'surface_process': 'none'},
            {'color_num': 4, 'height': 30, 'width': 340, 'depth': 250,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 4, 'height': 25, 'width': 220, 'depth': 160,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 4, 'height': 25, 'width': 160, 'depth': 115,
             'surface_material': 'white', 'surface_process': 'none'},
            {'color_num': 4, 'height': 25, 'width': 300, 'depth': 220,
             'surface_material': 'white', 'surface_process': 'none'},
        ]
        for cond in conditions:
            res = {
                'name': 'ttype',
                'condition': 'color_num: {}, height: {}, width: {}, depth: {}, surface_material: {}'.format(
                    cond['color_num'],
                    cond['height'],
                    cond['width'],
                    cond['depth'],
                    cond['surface_material'],
                )
            }
            for q in range(100, 30001, 100):
                val = {'color_num': cond['color_num'],
                       'height': cond['height'],
                       'width': cond['width'],
                       'depth': cond['depth'],
                       'surface_material': cond['surface_material'],
                       'surface_process': cond['surface_process'],
                       'quantity': q}
                try:
                    price = ttype._get_unit_price(val, {})
                    res[str(q)] = price
                except ValidationError as e:
                    print(e)
                    res[str(q)] = 'quantity too small'
            writer.writerow(res)

    def test_folding_carton_estimation(self, writer):
        conditions = [
            {'color_num': 1, 'height': 80, 'width': 80, 'depth': 160,
             'surface_material': 'normal', 'surface_process': 'op',
             'emboss': 'none', 'special_print': 'none', 'bottom': 'caramel'},
            {'color_num': 2, 'height': 80, 'width': 80, 'depth': 160,
             'surface_material': 'normal', 'surface_process': 'op',
             'emboss': 'none', 'special_print': 'none', 'bottom': 'caramel'},
            {'color_num': 3, 'height': 80, 'width': 80, 'depth': 160,
             'surface_material': 'normal', 'surface_process': 'op',
             'emboss': 'none', 'special_print': 'none', 'bottom': 'caramel'},
            {'color_num': 4, 'height': 80, 'width': 80, 'depth': 160,
             'surface_material': 'normal', 'surface_process': 'op',
             'emboss': 'none', 'special_print': 'none', 'bottom': 'caramel'},
            {'color_num': -1, 'height': 80, 'width': 80, 'depth': 160,
             'surface_material': 'normal', 'surface_process': 'op',
             'emboss': 'none', 'special_print': 'none', 'bottom': 'caramel'},
            {'color_num': 1, 'height': 40, 'width': 40, 'depth': 150,
             'surface_material': 'ivory', 'surface_process': 'op',
             'emboss': 'none', 'special_print': 'none', 'bottom': 'onetouch'},
            {'color_num': 2, 'height': 40, 'width': 40, 'depth': 150,
             'surface_material': 'ivory', 'surface_process': 'op',
             'emboss': 'none', 'special_print': 'none', 'bottom': 'onetouch'},
            {'color_num': 3, 'height': 40, 'width': 40, 'depth': 150,
             'surface_material': 'ivory', 'surface_process': 'op',
             'emboss': 'none', 'special_print': 'none', 'bottom': 'onetouch'},
            {'color_num': 4, 'height': 40, 'width': 40, 'depth': 150,
             'surface_material': 'ivory', 'surface_process': 'op',
             'emboss': 'none', 'special_print': 'none', 'bottom': 'onetouch'},
            {'color_num': -1, 'height': 40, 'width': 40, 'depth': 150,
             'surface_material': 'ivory', 'surface_process': 'op',
             'emboss': 'none', 'special_print': 'none', 'bottom': 'onetouch'},
        ]
        for cond in conditions:
            res = {
                'name': 'folding_carton',
                'condition': 'color_num: {}, height: {}, width: {}, depth: {}, surface_material: {}, surface_process: {}, emboss: {}, special_print: {}, bottom: {}'.format(
                                 cond['color_num'],
                                 cond['height'],
                                 cond['width'],
                                 cond['depth'],
                                 cond['surface_material'],
                                 cond['surface_process'],
                                 cond['emboss'],
                                 cond['special_print'],
                                 cond['bottom'],
                             )
            }
            for q in range(100, 30001, 100):
                val = {'color_num': cond['color_num'],
                       'height': cond['height'],
                       'width': cond['width'],
                       'depth': cond['depth'],
                       'quantity': q,
                       'outside': ['A', 'B'],
                       'inside': [],
                       'surface_material': cond['surface_material'],
                       'surface_process': cond['surface_process'],
                       'emboss': cond['emboss'],
                       'special_print': cond['special_print'],
                       'bottom': cond['bottom']}
                try:
                    price = folding_carton._get_unit_price(val, {})
                    res[str(q)] = price
                except ValidationError:
                    res[str(q)] = 'quantity too small'
            # writer.writerow(res)
