from django.core.management.base import BaseCommand, CommandError
from products.models import Product
import json


class Command(BaseCommand):
    help = 'Import extra_info data from json files.'

    def add_arguments(self, parser):
        parser.add_argument('-s', '--slugs', nargs='+', type=str)

    def handle(self, *args, **kwargs):
        # SPECIFIC PRODUCT
        if kwargs['slugs']:
            for slug in kwargs['slugs']:
                try:
                    p = Product.objects.get(slug=slug)
                except Product.DoesNotExist:
                    raise CommandError("Product {} does not exist.".format(slug))
                try:
                    with open("../product_data/json/" + slug + ".json", 'r') as f:
                        j = json.loads(f.read())
                        p.extra_info = j
                        p.save()
                        self.stdout.write('Product: {} saved.'.format(slug))
                except FileNotFoundError:
                    raise CommandError("json file for {} not exist".format(slug))
        # ALL PRODUCTS
        else:
            for p in Product.objects.all():
                try:
                    with open("../product_data/json/" + p.slug + ".json", 'r') as f:
                        j = json.loads(f.read())
                        p.extra_info = j
                        p.save()
                        self.stdout.write('Product: {} saved.'.format(p.slug))
                except FileNotFoundError:
                    # raise CommandError("json file for {} not exist".format(p.slug))
                    print("***** json file for {} not exist".format(p.slug))
