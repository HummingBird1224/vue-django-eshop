from django.core.exceptions import ValidationError
import re


def validate_tel(val):
    tel = re.sub("\\D", "", val)
    tel = tel.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
    if len(tel) not in [10, 11]:
        raise ValidationError("有効な電話番号を入力してください。")
    elif tel[0] != '0':
        raise ValidationError("有効な電話番号を入力してください。")
    elif tel[:2] == '00':
        raise ValidationError("有効な電話番号を入力してください。")


def validate_postal_code(val):
    code = re.sub("\\D", "", val)
    code = code.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
    if len(code) != 7:
        raise ValidationError("有効な郵便番号を入力してください。")
    return code[:3] + '-' + code[3:]
