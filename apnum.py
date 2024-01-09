import math
from decimal import Decimal
from pprint import pprint


class IntExp:

    def __init__(self, value=None, exp=None) -> None:
        if isinstance(value, IntExp):
            self.significand, self.exponent = value.significand, value.exponent
        else:
            self.significand, self.exponent = (
                self.value_to_signif_exp(value)
                if value
                else (0, 0)
            )
            if exp:
                self.exponent += exp

    def value_to_signif_exp(self, value):
        significand = 0
        exponent = 0

        if isinstance(value, str):
            value = Decimal(value)

        if isinstance(value, int):
            significand = value
            exponent = 0

        elif isinstance(value, float):
            if math.isnan(value) or math.isinf(value):
                raise ValueError
            value_str = f"{value:.15e}"
            signif_str, exp_str = value_str.split("e")
            exponent = int(exp_str)
            signif_str_int, signif_str_frac = signif_str.split(".")
            signif_int = list(signif_str_int)
            signif_frac = list(signif_str_frac.rstrip("0"))
            while signif_frac:
                signif_int.append(signif_frac[0])
                signif_frac.pop(0)
                exponent -= 1
            significand = int(''.join(signif_int))

        elif isinstance(value, Decimal):
            (sign, digits, exponent) = Decimal(value).as_tuple()
            significand = int("".join(map(str,digits)))
            if sign:
                significand *= -1

        while significand and significand % 10 == 0:
            significand //= 10
            exponent += 1
        return significand, exponent

    def __str__(self) -> str:
        return f"{self.significand}e{self.exponent}"

    def dec_exponent(self, dec):
        self.significand *= 10 ** dec
        self.exponent -= dec

    def equalizes_exponents(self, other):
        if self.exponent != other.exponent:
            if self.exponent > other.exponent:
                dec = self.exponent - other.exponent
                self.dec_exponent(dec)
            else:
                dec = other.exponent - self.exponent
                other.dec_exponent(dec)

    def __add__(self, other):
        self.equalizes_exponents(other)
        self.significand += other.significand
        return self


class Num:

    def __init__(self, real_value=0, img_value=None) -> None:
        if isinstance(real_value, Num):
            self.from_tuple(real_value.as_tuple())
        else:
            self.real_significand, self.real_exponent = self.value_to_signif_exp(real_value)
            self.img_significand, self.img_exponent = self.value_to_signif_exp(img_value)

    def value_to_signif_exp(self, value):
        significand = 0
        exponent = 0

        if not value:
            return significand, exponent

        if isinstance(value, str):
            value = Decimal(value)

        if isinstance(value, int):
            significand = value
            exponent = 0

        elif isinstance(value, float):
            if math.isnan(value) or math.isinf(value):
                raise ValueError
            value_str = f"{value:.15e}"
            signif_str, exp_str = value_str.split("e")
            exponent = int(exp_str)
            signif_str_int, signif_str_frac = signif_str.split(".")
            signif_int = list(signif_str_int)
            signif_frac = list(signif_str_frac.rstrip("0"))
            while signif_frac:
                signif_int.append(signif_frac[0])
                signif_frac.pop(0)
                exponent -= 1
            significand = int(''.join(signif_int))

        elif isinstance(value, Decimal):
            (sign, digits, exponent) = Decimal(value).as_tuple()
            significand = int("".join(map(str,digits)))
            if sign:
                significand *= -1

        while significand and significand % 10 == 0:
            significand //= 10
            exponent += 1

        return significand, exponent

    def as_tuple(self):
        return (
            self.real_significand,
            self.real_exponent,
            self.img_significand,
            self.img_exponent,
        )

    def from_tuple(self, tuple_):
        (
            real_significand,
            real_exponent,
            img_significand,
            img_exponent,
        ) = tuple_
        self.real_significand = real_significand
        self.real_exponent = real_exponent
        self.img_significand = img_significand
        self.img_exponent = img_exponent
        return self
       
    def __str__(self) -> str:
        return f"{self.real_significand}e{self.real_exponent}i{self.img_significand}e{self.img_exponent}"

    def dec_real_exponent(self, dec):
        self.real_significand *= 10 ** dec
        self.real_exponent -= dec

    def equalizes_real_exponents(self, other):
        if self.real_exponent != other.real_exponent:
            if self.real_exponent > other.real_exponent:
                dec = self.real_exponent - other.real_exponent
                self.dec_real_exponent(dec)
            else:
                dec = other.real_exponent - self.real_exponent
                other.dec_real_exponent(dec)

    def dec_img_exponent(self, dec):
        self.img_significand *= 10 ** dec
        self.img_exponent -= dec

    def equalizes_img_exponents(self, other):
        if self.img_exponent != other.img_exponent:
            if self.img_exponent > other.img_exponent:
                dec = self.img_exponent - other.img_exponent
                self.dec_img_exponent(dec)
            else:
                dec = other.img_exponent - self.img_exponent
                other.dec_img_exponent(dec)

    def __add__(self, other):
        self.equalizes_real_exponents(other)
        self.real_significand += other.real_significand
        self.equalizes_img_exponents(other)
        self.img_significand += other.img_significand
        return self


if __name__ == '__main__':  # pragma: no cover
    print(IntExp(123))
    print(IntExp(123, 2))
    print(IntExp(-123, -2))
    print(IntExp(1.23, 4))
    print(IntExp(1.23, 1))

