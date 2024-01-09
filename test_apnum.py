import pytest
from apnum import Num
from decimal import Decimal


def test_apnum_init():
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
        ("123e-2i234e-1q", Num(1.23, 23.4)),
    ]
    for value, param in assert_values:
        print(value, type(param), param)
        assert value == str(Num(param))

    # invalid float
    with pytest.raises(ValueError):
        Num(-1.23e500)

    # valid "i" component
    assert "-123e3i-123456789e-7" == str(Num(-123000, -12.3456789))


def test_apnum_tuple():
    n1 = Num(1.23, 23.4)
    t1 = n1.as_tuple()
    n2 = Num().from_tuple(t1)
    t2 = n2.as_tuple()
    assert t1 == t2
