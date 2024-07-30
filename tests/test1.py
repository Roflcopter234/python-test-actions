import pytest
from src.helper import matmul, matmul2


@pytest.fixture
def test1_input1():
    A = [
        [1, 2],
        [3, 4]
    ]

    return A

@pytest.fixture
def test1_input2():
    B = [
        [5, 6],
        [7, 8]
    ]

    return B

@pytest.fixture
def test1_output():
    expected = [
        [19, 22],
        [43, 50]
    ]

    return expected


def test_matmul_simple(test1_input1, test1_input2, test1_output):
    assert matmul(test1_input1, test1_input2) == test1_output


def test_matmul_numpy(test1_input1, test1_input2, test1_output):
    assert matmul2(test1_input1, test1_input2) == test1_output