from django.test import TestCase
from django.core.exceptions import ValidationError
from . import (
    # flatbag
    tape_opp_bag,
    zip_clear_bag,
    zip_clear_pressbag,
    zip_aluminum_bag,
    zip_aluminum_stand,
    aluminum_pouche,
    subsection_bag,
    # cardboard
    ntype_corrugated,
    ntype_mailer,
    atype,
    ttype,
    # paperbox
    folding_carton,
)
import json


class PriceTestCase(TestCase):

    def setup(self):
        pass

    def test_tape_opp_bag_estimation(self):
        print()
        for q in range(10000, 10201, 100):
            val = {'color_num': 2,
                   'height': 305,
                   'width': 225,
                   'quantity': q}
            try:
                price = tape_opp_bag.get_unit_price(val, {})
                print('tape_opp_bag: {} (quantity - {})'.format(price, q))
            except ValidationError:
                print('validation error: quantity - {}'.format(q))

    def test_zip_clear_pressbag_estimation(self):
        val = {'color_num': 3,
               'height': 210,
               'width': 180,
               'quantity': 20000}
        price = zip_clear_pressbag.get_unit_price(val, {})
        print()
        print('zip_clear_pressbag: ', price)

    def test_zip_clear_bag_estimation(self):
        val = {'color_num': 1,
               'height': 240,
               'width': 170,
               'quantity': 900}
        price = zip_clear_bag.get_unit_price(val, {})
        print()
        print('zip_clear_bag: ', price)

    def test_zip_aluminum_bag_estimation(self):
        val = {'color_num': 3,
               'height': 210,
               'width': 180,
               'quantity': 20000,
               'material': 'mattepet'}
        price = zip_aluminum_bag.get_unit_price(val, {})
        print()
        print('zip_aluminum_bag: ', price)

    def test_zip_aluminum_stand_estimation(self):
        val = {'color_num': 3,
               'height': 310,
               'width': 250,
               'depth': 100,
               'quantity': 10000,
               'material': 'mattepet'}
        price = zip_aluminum_stand.get_unit_price(val, {})
        print()
        print('zip_aluminum_stand: ', price)

    def test_ntype_corrugated_estimation(self):
        val = {'color_num': 3,
               'height': 80,
               'width': 220,
               'depth': 140,
               'quantity': 10000,
               'surface_material': 'white',
               'surface_process': 'mattevarnish'}
        price = ntype_corrugated.get_unit_price(val, {})
        print()
        print('ntype_corrugated: ', price)

    def test_ntype_mailer_estimation(self):
        val = {'color_num': 3,
               'height': 100,
               'width': 350,
               'depth': 270,
               'quantity': 10000,
               'surface_material': 'white'}
        price = ntype_mailer.get_unit_price(val, {})
        print()
        print('ntype_mailer: ', price)

    def test_atype_estimation(self):
        val = {'color_num': 3,
               'height': 160,
               'width': 350,
               'depth': 250,
               'quantity': 10000,
               'surface_material': 'white'}
        price = atype.get_unit_price(val, {})
        print()
        print('atype: ', price)

    def test_ttype_estimation(self):
        val = {'color_num': 3,
               'height': 25,
               'width': 300,
               'depth': 220,
               'quantity': 10000,
               'surface_material': 'white'}
        price = ttype.get_unit_price(val, {})
        print()
        print('ttype: ', price)

    def test_folding_carton_estimation(self):
        val = {'color_num': 3,
               'height': 200,
               'width': 40,
               'depth': 40,
               'quantity': 10000,
               'outside': ['A', 'B'],
               'inside': ['A', 'B'],
               'surface_material': 'ivory',
               'surface_process': 'mattepp',
               'emboss': 'emboss',
               'special_print': 'gold',
               'bottom': 'caramel'}
        price = folding_carton.get_unit_price(val, {})
        print()
        print('folding carton: ', price)
