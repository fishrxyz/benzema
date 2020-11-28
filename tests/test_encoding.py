import pytest
from benzema.encoder import Encoder


test_string = "Hatem Ben Arfa"
test_dict = {
    "name": "Hatem Ben Arfa",
    "age": 33,
    "clubs": ["NUFC", "OL", "OM"]
}
test_list = ["Ben Arfa", "Benzema", "Mahrez", "Aouar"]
test_int = 23


def test_encode_wrong_type():
    t = tuple()
    err = f'[error] Cannot encode object of type {type(t).__name__}'
    with pytest.raises(TypeError) as exc:
        Encoder(t).encode()

    assert err == str(exc.value)


def test_encode_from_string():
    encoded_string = Encoder(test_string).encode()
    expected_result = b'14:Hatem Ben Arfa'
    assert isinstance(encoded_string, bytes)
    assert encoded_string == expected_result


def test_encode_from_empty_string():
    encoded_string = Encoder('').encode()
    expected_result = b'0:'
    assert isinstance(encoded_string, bytes)
    assert encoded_string == expected_result


def test_encode_from_dict():
    encoded_dict = Encoder(test_dict).encode()
    expected_result = b'd4:name14:Hatem Ben Arfa3:agei33e5:clubsl4:NUFC2:OL2:OMee'  # noqa E501
    assert isinstance(encoded_dict, bytearray)
    assert encoded_dict == expected_result


def test_encode_from_empty_dict():
    encoded_dict = Encoder({}).encode()
    expected_result = b'de'
    assert isinstance(encoded_dict, bytearray)
    assert encoded_dict == expected_result


def test_encode_from_list():
    encoded_list = Encoder(test_list).encode()
    expected_result = b'l8:Ben Arfa7:Benzema6:Mahrez5:Aouare'
    assert isinstance(encoded_list, bytearray)
    assert encoded_list == expected_result


def test_encode_from_empty_list():
    encoded_list = Encoder([]).encode()
    expected_result = b'le'
    assert isinstance(encoded_list, bytearray)
    assert encoded_list == expected_result


def test_encode_from_int():
    encoded_int = Encoder(test_int).encode()
    expected_result = b'i23e'
    assert isinstance(encoded_int, bytes)
    assert encoded_int == expected_result


def test_encode_from_bytes():
    pass
