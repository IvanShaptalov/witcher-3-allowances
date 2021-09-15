import hashlib
import hmac

from payment import constant


def sign_form_data(key: str, data: dict) -> str:
    if data:
        sorted_data = sorted(data.items())
    else:
        sorted_data = {}

    msg = ''.join(
        str(v) for k, v in sorted_data
        if not isinstance(v, (dict, list, type(None)))
    )
    msg = msg.lower()

    return hmac.new(key.encode(), msg.encode(), hashlib.sha512).hexdigest()


def prepare_dictionary_to_sign(dictionary: dict):
    allowed_dict = {}
    for k, v in dictionary.items():
        if k in constant.allowed_keys:
            allowed_dict[k] = v[0]
    return allowed_dict
