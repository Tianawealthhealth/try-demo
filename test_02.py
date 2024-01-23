import pytest

def add_num(x):
    return x+1

def test_num():
    re = add_num(3)
    assert re == 4