from typing import Union, Optional
from collections import OrderedDict
from .constants import (
    DICT_IDENTIFIER, INT_IDENTIFIER,
    LIST_IDENTIFIER, STRING_DELIMITER,
    EOT_IDENTIFIER
)


class Decoder(object):

    """
        Decodes a bencoded object into
        its corresponding python representation.
    """

    def __init__(self, payload: bytes):

        if not isinstance(payload, bytes):
            _type = type(payload).__name__
            err = f'[error] Cannot decode payload. Expected bytes, got {_type}'
            raise TypeError(err)

        self._payload: bytes = payload
        self._index: int = 0

    def decode(self):
        char: Optional[bytes] = self._opening_char

        if char == DICT_IDENTIFIER:
            self._index += 1
            return self._to_dict()
        elif char == INT_IDENTIFIER:
            self._index += 1
            return self._to_int()
        elif char == LIST_IDENTIFIER:
            self._index += 1
            return self._to_list()
        elif char is None:
            return
        elif char in b'0123456789':
            return self._to_string()

    def _to_dict(self) -> OrderedDict:

        # Note: an OrderedDict is being used in this case because we need
        # the 'info' dictionaries to be identical in order to produce the
        # correct sha1 hash that will be used to make a request to the tracker.

        _dict: OrderedDict = OrderedDict()

        # loop through the payload until we reach 'e'
        while self._payload[self._index: self._index + 1] != EOT_IDENTIFIER:
            # decode whatever is at that index
            key: bytes = self.decode()
            value: bytes = self.decode()

            # populate the final list
            _dict[key] = value

        # when we're done, increment the index.
        # if it's bigger or equal to the length of the payload
        # the next call to self._opening_char will return None
        # and the program will exit
        self._index += 1
        return _dict

    def _to_list(self) -> list:
        _list: list = []
        # loop through the payload until we reach 'e'
        while self._payload[self._index:self._index+1] != EOT_IDENTIFIER:
            # decode whatever is at that index
            element: bytes = self.decode()

            # populate the final list
            _list.append(element)

        # when we're done, increment the index.
        # if it's bigger or equal to the length of the payload
        # the next call to self._opening_char will return None
        # and the program will exit

        self._index += 1
        return _list

    def _to_int(self) -> int:
        # access EOT_IDENTIFIER (ie 'e')
        end_token_index: int = self._payload.index(EOT_IDENTIFIER, self._index)

        # read whatever is between 'i' and 'e' and cast that to an int
        _int: int = int(self._payload[self._index:end_token_index])

        # update index to start after EOT_IDENTIFIER
        self._index = end_token_index + 1

        return _int

    def _to_string(self) -> bytes:
        # get index of delimiter
        str_delim_idx: int = self._payload.index(STRING_DELIMITER, self._index)

        # number of characters to read
        chars_to_read: int = int(self._payload[self._index:str_delim_idx])

        # set the starting index at delimiter + 1 (ie the char after :)
        start_index = str_delim_idx + 1

        # read `char_to_read` characters starting from delimiter index
        data: bytes = self._payload[start_index:start_index + chars_to_read]

        # update index to start at end of string
        self._index = start_index + chars_to_read

        return data

    @property
    def _opening_char(self) -> Union[bytes, None]:
        if self._index >= len(self._payload):
            # we've reached the end of the payload
            return None
        return self._payload[self._index:self._index + 1]
