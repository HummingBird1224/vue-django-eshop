import json

data = {
    'contact_required': {
        'name': 'お問い合わせ',
        'value': False,
        'extra': '',
        'image': '',
    },
    'sample_order': {
        'name': 'サンプル注文',
        'value': False,
        'extra': '',
        'image': '',
    },
    'small_lot_availability': {
        'name': '小ロット対応',
        'value': False,
        'extra': '',
        'image': '',
    },
    'min_ordering_quantity': {
        'name': '最小注文数',
        'value': -1,
        'extra': '',
        'image': '',
    },
    'max_ordering_quantity': {
        'name': '最大注文数',
        'value': -1,
        'extra': '',
        'image': '',
    },
    'estimated_shipping_date': {
        'name': '納期',
        'value': {
            'first': 14,
            'repeat': 7
        },
        'extra': {
            'first': 'データ確定後2週間',
            'repeat': '1週間',
        },
        'image': '',
    },
    'can_select_original_size': {
        'name': 'オリジナルサイズ',
        'value': False,
        'extra': '',
        'image': '',
    },
    'is_design_unnecessary': {
        'name': 'デザイン不要',
        'value': False,
        'extra': '',
        'image': '',
    },
    'is_easy_draft_available': {
        'name': 'カンタン入稿可能',
        'value': False,
    },
    'notes': {
        'name': '備考',
        'value': '',
        'extra': '',
        'image': '',
    },
    'size_limit': {
        'height': {
            'min': 140,
            'max': 500,
        },
        'width': {
            'min': 80,
            'max': 400,
        },
    },
    'choosable_color': {
        'name': '印刷色',
        'value': "1色（白・黒・青・赤・緑）",
        'extra': '',
        'image': '',
    },
    'size': {
        'name': 'サイズ',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'options': {
            '1': {
                'name': '小物用',
                'value': [
                    {'name': 'height', 'value': 140},
                    {'name': 'width', 'value': 100},
                ],
                'extra': '横100mm 縦140mm',
                'data': 'design_templates/',
                'image': 'img/external/base/size/zip_accessories.jpg'
            },
            '2': {
                'name': 'A6',
                'value': [
                    {'name': 'height', 'value': 170},
                    {'name': 'width', 'value': 120},
                ],
                'extra': '横120mm 縦170mm',
                'data': 'design_templates/',
                'image': 'img/external/base/size/zip_A6.jpg'
            },
            '3': {
                'name': 'A5',
                'value': [
                    {'name': 'height', 'value': 240},
                    {'name': 'width', 'value': 170},
                ],
                'extra': '横170mm 縦240mm',
                'data': 'design_templates/',
                'image': 'img/external/base/size/zip_A5.jpg'
            },
            '4': {
                'name': 'A4',
                'value': [
                    {'name': 'height', 'value': 340},
                    {'name': 'width', 'value': 240},
                ],
                'extra': '横240mm 縦340mm',
                'data': 'design_templates/',
                'image': 'img/external/base/size/zip_A4.jpg'
            },
            '5': {
                'name': 'A3',
                'value': [
                    {'name': 'height', 'value': 480},
                    {'name': 'width', 'value': 340},
                ],
                'extra': '横340mm 縦480mm',
                'data': 'design_templates/',
                'image': 'img/external/base/size/zip_A3.jpg'
            },
        }
    },
    'quantity': {
        'name': 'ロット数',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'unit': '袋',
        'options': {
            '1': {'name': '100', 'value': 100},
            '2': {'name': '200', 'value': 200},
            '3': {'name': '300', 'value': 300},
            '4': {'name': '500', 'value': 500},
            '5': {'name': '700', 'value': 700},
            '6': {'name': '1000', 'value': 1000},
            '7': {'name': '1500', 'value': 1500},
            '8': {'name': '2000', 'value': 2000},
            '9': {'name': '2500', 'value': 2500},
            '10': {'name': '3000', 'value': 3000},
        },
    },
    'shipping_area': {
        'exclude': True,
        'prefectures': [
        ]
    }
}

print(json.dumps(data, indent=2, ensure_ascii=False))
