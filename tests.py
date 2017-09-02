import pytest
from validator import check_args, InvalidInput


@check_args(a='int', b='int')
def fn1(a, b):
    return a + b


@check_args(a='int')  # invalid function
def fn2(a, b):
    return a + b


def test_valid():
    assert fn1(a=2, b=3) == 5
    assert fn1(2, 3) == 5


@pytest.mark.xfail(raises=InvalidInput)
def test_invalid():
    with pytest.raises(InvalidInput):
        fn2(a=2, b=3)

    with pytest.raises(InvalidInput):
        fn1(a='test', b=3)

    with pytest.raises(InvalidInput):
        fn1(a=None, b=3)

    with pytest.raises(InvalidInput):
        fn1(a=1.1, b=3)
