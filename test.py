import pytest

def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5  # This test should pass
    assert add(-1, 1) == 0  # This test should pa