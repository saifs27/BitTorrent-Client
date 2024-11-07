import pytest
import sys
from bittorrent.bencode import Decoder

@pytest.mark.parametrize("data,expected", [("i17e", 17), ("i2e", 2)])
def test_decode_int(data, expected):
    assert Decoder(data).decode_int() == expected


@pytest.mark.parametrize("data,expected", [("2:hi", "hi"), ("4:test", "tes")])
def test_decode_str(data, expected):
    assert Decoder(data).decode_string() == expected








