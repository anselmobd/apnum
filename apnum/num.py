import math
from decimal import Decimal
from pprint import pprint
from apnum.intexp import IntExp


class Num:

    def __init__(self, real_value=None, img_value=None) -> None:
        if isinstance(real_value, Num):
            self.real, self.img = real_value.real, real_value.img
        else:
            self.real = IntExp(real_value)
            self.img = IntExp(img_value)

    def __str__(self) -> str:
        return f"{self.real.significand}e{self.real.exponent}i{self.img.significand}e{self.img.exponent}"

    def __add__(self, other):
        return Num(
            self.real + other.real,
            self.img + other.img
        )
