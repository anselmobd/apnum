import math
from decimal import Decimal


class Num:

    def __init__(self, value, i_value=None) -> None:
        self.significand = 0
        self.exponent = 0
        self.i_significand = 0
        self.i_exponent = 0

        if isinstance(value, int):
            self.significand = value
            self.exponent = 0

        elif isinstance(value, float):
            if math.isnan(value) or math.isinf(value):
                raise ValueError
            value_str = f"{value:.15e}"
            num_str, exp_str = value_str.split("e")
            self.exponent = int(exp_str)
            num_str_int, num_str_frac = num_str.split(".")
            num_int = list(num_str_int)
            num_frac = list(num_str_frac.rstrip("0"))
            while num_frac:
                num_int.append(num_frac[0])
                num_frac.pop(0)
                self.exponent -= 1
            self.significand = int(''.join(num_int))

        elif isinstance(value, str):
            value = Decimal(value)

        if isinstance(value, Decimal):
            (sign, digits, self.exponent) = Decimal(value).as_tuple()
            self.significand = int("".join(map(str,digits)))
            if sign:
                self.significand *= -1

        while self.significand and self.significand % 10 == 0:
            self.significand //= 10
            self.exponent += 1

    def __str__(self) -> str:
        return f"{self.significand}e{self.exponent}i{self.i_significand}e{self.i_exponent}"


if __name__ == '__main__':
    print(Num(123))
    print(Num(123000))
    print(Num(-123))
    print(Num(-123000))
    print(Num(12.3))
    print(Num(12.3456789))
    print(Num(0.00123))
    print(Num(12300.))
    print(Num(-12.3))
    print(Num(-12.3456789))
    print(Num(-0.00123))
    print(Num(-12300.))
    print(Num(1.23e50))
    print(Num(-1.23e50))
    # print(Num(-1.23e500))
    print(Num(Decimal("1000000000.001")))
    print(Num(Decimal("-1000000000.001")))
    print(Num(Decimal("1000000000")))
    print(Num(Decimal("-1000000000")))
    print(Num("-1000000000"))
