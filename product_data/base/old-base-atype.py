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
            'first': 21,
            'repeat': 21
        },
        'extra': {
            'first': 'データ確定後2~3週間',
            'repeat': 'データ確定後2~3週間',
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
    'size': {
        'name': 'サイズ',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'options': {
            '1': {
                'name': '60サイズ',
                'value': [
                    {'name': 'height', 'value': 120},
                    {'name': 'width', 'value': 250},
                    {'name': 'depth', 'value': 210},
                ],
                'extra': '横250mm 縦210mm 高さ120mm',
                'data': 'design_templates/',
                'image': 'img/external/base/size/cardbox_60.jpg'
            },
            '2': {
                'name': '80サイズ',
                'value': [
                    {'name': 'height', 'value': 150},
                    {'name': 'width', 'value': 310},
                    {'name': 'depth', 'value': 220},
                ],
                'extra': '横310mm 縦220mm 高さ150mm',
                'data': 'design_templates/',
                'image': 'img/external/base/size/cardbox_80.jpg'
            },
            '3': {
                'name': '100サイズ',
                'value': [
                    {'name': 'height', 'value': 250},
                    {'name': 'width', 'value': 350},
                    {'name': 'depth', 'value': 300},
                ],
                'extra': '横350mm 縦300mm 高さ250mm',
                'data': 'design_templates/',
                'image': 'img/external/base/size/cardbox_100.jpg'
            },
        }
    },
    'quantity': {
        'name': 'ロット数',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'unit': '箱',
        'options': {
            '1': {'name': '100', 'value': 100},
            '2': {'name': '300', 'value': 300},
            '3': {'name': '500', 'value': 500},
            '4': {'name': '1,000', 'value': 1000},
        },
    },
    'print_area': {
        'name': '印刷面数',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'options': {
            '1': {
                'name': '１面',
                'value': 1,
                'extra': '',
                'image': ''
            },
            '2': {
                'name': '２面',
                'value': 2,
                'extra': '',
                'image': ''
            },
        },
    },
    'shipping_area': {
        'exclude': False,
        'prefectures': [
            '東京',
            '神奈川',
            '静岡',
            '埼玉',
            '千葉',
        ]
    }
}

print(json.dumps(data, indent=2, ensure_ascii=False))
