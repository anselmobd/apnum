import math
from decimal import Decimal


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
            self.optimize()

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

        return significand, exponent

    def optimize(self):
        while self.significand and self.significand % 10 == 0:
            self.significand //= 10
            self.exponent += 1

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
        added = IntExp(
            self.significand + other.significand,
            self.exponent,
        )
        self.optimize()
        added.optimize()
        return added

    def __sub__(self, other):
        self.equalizes_exponents(other)
        subs = IntExp(
            self.significand - other.significand,
            self.exponent,
        )
        self.optimize()
        subs.optimize()
        return subs
