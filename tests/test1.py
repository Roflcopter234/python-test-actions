import pytest
from src.helper import matmul


def test_matmul_simple():
    A = [
        [1, 2],
        [3, 4]
    ]
    B = [
        [5, 6],
        [7, 8]
    ]
    expected = [
        [19, 22],
        [43, 50]
    ]
    assert matmul(A, B) == expected

