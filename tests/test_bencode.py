import pytest
from bittorrent.bencode import Decoder, Encoder

@pytest.mark.parametrize("data,expected", [("i17e", 17), ("i2e", 2)])
def test_decode_int(data, expected):
    assert Decoder(data).decode_int() == expected


@pytest.mark.parametrize("data,expected", [("2:hi", "hi"), ("4:test", "test")])
def test_decode_str(data, expected):
    assert Decoder(data).decode_string() == expected

#@pytest.mark.parametrize("data,expected", [("li1ei17ee", [1, 17])])
#def test_decode_list(data, expected):
#    assert Decoder(data).decode_list() == expected

@pytest.mark.parametrize("data,expected", [(123, "i123e"), ("hello", "5:hello")])
def test_encode_int_str(data, expected):
    assert Encoder(data).encode() == expected

lists = [([1, "hello", "hi", 23], "li1e5:hello2:hii23ee")]
@pytest.mark.parametrize("data,expected", lists)
def test_encode_lists(data, expected):
    assert Encoder(data).encode() == expected

dictionaries = {"integer":5, 8:"eight", "list": [1, "hi"], "dict": {1: 2}}
dict_expected = "d7:integeri5ei8e5:eight4:listli1e2:hie4:dictdi1ei2eee"
@pytest.mark.parametrize("data,expected", [(dictionaries, dict_expected)])
def test_encode_dict(data, expected):
    assert Encoder(data).encode() == expected
    








