import pytest
from benzema.decoder import Decoder
from collections import OrderedDict


test_string = b'14:Hatem Ben Arfa'
test_int = b'i23e'
test_dict = b'd4:name14:Hatem Ben Arfa3:agei33e5:clubsl4:NUFC2:OLeee'
test_list = b'l8:Ben Arfa7:Benzema6:Mahrez5:Aouare'


def test_decode_wrong_type():
    s = "Real Madrid CF"
    err = f'[error] Cannot decode payload. Expected bytes, got {type(s).__name__}'  # noqa E501
    with pytest.raises(TypeError) as exc:
        Decoder(s).decode()

    assert err == str(exc.value)


def test_decode_to_string():
    decoded_string = Decoder(test_string).decode()
    expected_result = b'Hatem Ben Arfa'
    assert isinstance(decoded_string, bytes)
    assert decoded_string == expected_result


def test_decode_to_empty_string():
    decoded_string = Decoder(b'0:').decode()
    expected_result = b''
    assert isinstance(decoded_string, bytes)
    assert decoded_string == expected_result


def test_decode_to_dict():
    decoded_dict = Decoder(test_dict).decode()
    expected_result = OrderedDict({
        b"name": b"Hatem Ben Arfa",
        b"age": 33,
        b"clubs": [b'NUFC', b'OL']
    })
    assert isinstance(decoded_dict, OrderedDict)
    assert decoded_dict == expected_result


def test_decode_to_empty_dict():
    decoded_dict = Decoder(b'de').decode()
    expected_result = OrderedDict({})
    assert isinstance(decoded_dict, OrderedDict)
    assert decoded_dict == expected_result


def test_decode_to_list():
    decoded_list = Decoder(test_list).decode()
    expected_result = [b'Ben Arfa', b'Benzema', b'Mahrez', b'Aouar']
    assert isinstance(decoded_list, list)
    assert decoded_list == expected_result


def test_decode_to_empty_list():
    decoded_list = Decoder(b'le').decode()
    expected_result = []
    assert isinstance(decoded_list, list)
    assert decoded_list == expected_result


def test_decode_to_int():
    decoded_int = Decoder(test_int).decode()
    expected_result = 23
    assert isinstance(decoded_int, int)
    assert decoded_int == expected_result
