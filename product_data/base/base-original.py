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
    'size_limit': {
        'height': {
            'min': 100,
            'max': 550,
        },
        'width': {
            'min': 100,
            'max': 610,
        },
    },
    'choosable_color': {
        'name': '印刷色',
        'value': "1色（白・黒・青・赤・緑）",
        'extra': '',
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
        'value': True,
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
    'size': {
        'name': 'サイズ',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'options': {
            '1': {
                'name': 'A3',
                'value': [
                    {'name': 'height', 'value': 420},
                    {'name': 'width', 'value': 300},
                ],
                'extra': '横300mm 縦420mm',
                'data': 'design_templates/',
                'image': 'img/external/base/size/base_original_a3.jpg'
            },
            '2': {
                'name': 'A5',
                'value': [
                    {'name': 'height', 'value': 210},
                    {'name': 'width', 'value': 150},
                ],
                'extra': '横150mm 縦210mm',
                'data': 'design_templates/',
                'image': 'img/external/base/size/base_original_a5.jpg'
            },
            '3': {
                'name': 'A6',
                'value': [
                    {'name': 'height', 'value': 150},
                    {'name': 'width', 'value': 105},
                ],
                'extra': '横105mm 縦150mm',
                'data': 'design_templates/',
                'image': 'img/external/base/size/base_original_a6.jpg'
            }
        }
    },
    'quantity': {
        'name': 'ロット数',
        'extra': '',
        'required': True,
        'default': '5',
        'image': '',
        'unit': '袋',
        'options': {
            '5': {'name': '50', 'value': 50},
            '10': {'name': '100', 'value': 100},
            '20': {'name': '200', 'value': 200},
            '30': {'name': '300', 'value': 300},
            '40': {'name': '400', 'value': 400},
            '50': {'name': '500', 'value': 500},
        },
    },
    'shipping_area': {
        'exclude': True,
        'prefectures': [
        ]
    }
}

print(json.dumps(data, indent=2, ensure_ascii=False))
