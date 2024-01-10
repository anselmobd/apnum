import pytest
from apnum import IntExp
from decimal import Decimal


def test_intexp_init():
    # valid values
    assert_values = [
        ("123e0", 123),
        ("123e3", 123000),
        ("-123e0", -123),
        ("-123e3", -123000),
        ("123e-1", 12.3),
        ("123456789e-7", 12.3456789),
        ("123e-5", 0.00123),
        ("123e2", 12300.),
        ("-123e-1", -12.3),
        ("-123456789e-7", -12.3456789),
        ("-123e-5", -0.00123),
        ("-123e2", -12300.),
        ("123e48", 1.23e50),
        ("-123e48", -1.23e50),
        ("1000000000001e-3", Decimal("1000000000.001")),
        ("-1000000000001e-3", Decimal("-1000000000.001")),
        ("1e9", Decimal("1000000000")),
        ("-1e9", Decimal("-1000000000")),
        ("1e9", "1000000000"),
        ("-1e9", "-1000000000"),
        ("123e-2", IntExp(1.23)),
        ("123e0", IntExp(1.23, 2)),
    ]
    for value, param in assert_values:
        print(value, type(param), param)
        assert value == str(IntExp(param))

    # invalid float
    with pytest.raises(ValueError):
        IntExp(-1.23e500)


def test_apnum_add():
    n1 = IntExp(1.23)
    n2 = IntExp(23.4)
    print(n1)
    print(n2)
    n1 += n2
    print(n1)
    assert "2463e-2" == str(n1)
    n1 = IntExp(1.23)
    n2 = IntExp(23.4)
    print(n1)
    print(n2)
    n2 += n1
    print(n2)
    assert "2463e-2" == str(n2)


def test_apnum_sub():
    n1 = IntExp(1.23)
    n2 = IntExp(23.4)
    print(n1)
    print(n2)
    n1 -= n2
    print(n1)
    assert "-2217e-2" == str(n1)
    n1 = IntExp(1.23)
    n2 = IntExp(23.4)
    print(n1)
    print(n2)
    n2 -= n1
    print(n2)
    assert "2217e-2" == str(n2)
