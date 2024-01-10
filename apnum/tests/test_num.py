import pytest
from apnum import Num
from decimal import Decimal


def test_num_init():
    # valid values
    assert_values = [
        ("123e0i0e0", 123),
        ("123e3i0e0", 123000),
        ("-123e0i0e0", -123),
        ("-123e3i0e0", -123000),
        ("123e-1i0e0", 12.3),
        ("123456789e-7i0e0", 12.3456789),
        ("123e-5i0e0", 0.00123),
        ("123e2i0e0", 12300.),
        ("-123e-1i0e0", -12.3),
        ("-123456789e-7i0e0", -12.3456789),
        ("-123e-5i0e0", -0.00123),
        ("-123e2i0e0", -12300.),
        ("123e48i0e0", 1.23e50),
        ("-123e48i0e0", -1.23e50),
        ("1000000000001e-3i0e0", Decimal("1000000000.001")),
        ("-1000000000001e-3i0e0", Decimal("-1000000000.001")),
        ("1e9i0e0", Decimal("1000000000")),
        ("-1e9i0e0", Decimal("-1000000000")),
        ("1e9i0e0", "1000000000"),
        ("-1e9i0e0", "-1000000000"),
        ("123e-2i234e-1", Num(1.23, 23.4)),
    ]
    for value, param in assert_values:
        print(value, type(param), param)
        assert value == str(Num(param))

    # invalid float
    with pytest.raises(ValueError):
        Num(-1.23e500)

    # valid "i" component
    assert "-123e3i-123456789e-7" == str(Num(-123000, -12.3456789))


def test_num_add():
    n1 = Num(1.23, 23.4)
    n2 = Num(23.4, 1.23)
    print(n1)
    print(n2)
    n1 += n2
    print(n1)
    assert "2463e-2i2463e-2" == str(n1)
    n1 = Num(1.23, 23.4)
    n2 = Num(23.4, 1.23)
    print(n1)
    print(n2)
    n2 += n1
    print(n2)
    assert "2463e-2i2463e-2" == str(n2)


def test_num_sub():
    n1 = Num(1.23, 23.4)
    n2 = Num(23.4, 1.23)
    print(n1)
    print(n2)
    n1 -= n2
    print(n1)
    assert "-2217e-2i2217e-2" == str(n1)
    n1 = Num(1.23, 23.4)
    n2 = Num(23.4, 1.23)
    print(n1)
    print(n2)
    n2 -= n1
    print(n2)
    assert "2217e-2i-2217e-2" == str(n2)
