from typing import Union
from collections import OrderedDict
from .constants import EOT_IDENTIFIER


supported_types = Union[int, str, bytes, list, dict, OrderedDict]


class Encoder(object):

    """
        Encodes payload to the bencode format.
    """

    def __init__(self, payload: supported_types):
        self._payload = payload

    def encode(self) -> supported_types:
        return self._encode_payload(self._payload)

    def _encode_payload(self, payload):
        if isinstance(payload, str):
            return self._from_string(payload)
        elif isinstance(payload, int):
            return self._from_int(payload)
        elif isinstance(payload, list):
            return self._from_list(payload)
        elif isinstance(payload, bytes):
            return self._from_bytes(payload)
        elif isinstance(payload, dict) or isinstance(payload, OrderedDict):
            return self._from_dict(payload)
        else:
            data_type = type(payload).__name__
            err = f'[error] Cannot encode object of type {data_type}'
            raise TypeError(err)

    def _from_dict(self, _dict) -> bytearray:
        # we use a bytearray because it's impossible to
        # concatenate bytearray types to strings

        encoded_dict: bytearray = bytearray('d', 'utf-8')
        for key, value in _dict.items():
            k: Union[bytes, bytearray] = self._encode_payload(key)
            v: Union[bytes, bytearray] = self._encode_payload(value)

            encoded_dict += k
            encoded_dict += v

        encoded_dict += EOT_IDENTIFIER
        return encoded_dict

    def _from_list(self, _list) -> bytearray:
        # we use a bytearray because it's impossible to
        # concatenate bytearray types to strings

        encoded_list: bytearray = bytearray('l', 'utf-8')
        encoded_list += b''.join([
            self._encode_payload(_list[idx])
            for idx in range(len(_list))
        ])
        encoded_list += EOT_IDENTIFIER
        return encoded_list

    def _from_int(self, _int) -> bytes:
        return bytes(f'i{str(_int)}e', 'utf-8')

    def _from_string(self, string) -> bytes:
        return bytes(f'{len(string)}:{string}', 'utf-8')

    def _from_bytes(self, _bytes) -> bytearray:
        # copied from pieces.bencoding.Encoder
        result = bytearray()
        result += str.encode(str(len(_bytes)))
        result += b':'
        result += _bytes
        return result
