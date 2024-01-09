import pytest
from apnum import Num
from decimal import Decimal


def test_apnum_init():
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
    ]
    for value, param in assert_values:
        assert value == str(Num(param))

    with pytest.raises(ValueError):
        Num(-1.23e500)

