from .intexp import IntExp
from .num import Num


if __name__ == '__main__':  # pragma: no cover
    print(Num(123))
    print(Num(123, 2))
    print(Num(-123, -2))
    print(Num(1.23, 4))
    print(Num(1.23, 1))
    print(IntExp(123))
    print(IntExp(123, 2))
    print(IntExp(-123, -2))
    print(IntExp(1.23, 4))
    print(IntExp(1.23, 1))

