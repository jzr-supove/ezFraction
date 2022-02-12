import math
import operator
from typing import Tuple, Union, List


class Fraction:
    rounding: int = 5
    decimal:  float
    _frac:    List[int]

    def __init__(self, number: Union[float, str], reduce: bool = True, rounding: int = 5):
        self.decimal = float(number)
        self.rounding = rounding
        self._frac = self._to_frac(self.decimal)
        if reduce:
            self.reduce()

    @classmethod
    def create(cls, numerator: int, denominator: int):
        obj = cls.__new__(cls)
        obj.decimal = numerator / denominator
        obj._frac = [int(numerator), int(denominator)]
        return obj

    @property
    def numerator(self):
        return self._frac[0]

    @property
    def denominator(self):
        return self._frac[1]

    @property
    def tuple(self):
        return tuple(self._frac)

    @staticmethod
    def lcm(x, y):
        return abs(x * y) // math.gcd(x, y)

    def _to_frac(self, number: float) -> List[int]:
        int_part = int(number)
        float_part = round(number - int_part, self.rounding)

        if float_part == 0:
            return [int_part, 1]

        fp_len = 0
        while float_part // 1 != float_part:
            float_part = round(float_part * 10, self.rounding)
            fp_len += 1

        multiplier = 10 ** fp_len
        return [round(number * multiplier), multiplier]

    def reduce(self, new_obj: bool = False):
        # gcd = 1
        # for i in range(2, min(map(lambda x: x if (x >= 0) else -x, self._frac))):
        #     if not sum(map(lambda x: x % i, self._frac)):
        #         gcd = i

        gcd = math.gcd(*self._frac)
        reduced = [int(f / gcd) for f in self._frac]

        if new_obj:
            return self.create(*reduced)

        self._frac = reduced
        return self

    def enlarge(self, multiplier: int = 2, new_obj: bool = False):
        if new_obj:
            return self.create(self._frac[0] * multiplier, self._frac[1] * multiplier)

        self._frac[0] *= multiplier
        self._frac[1] *= multiplier
        return self

    def with_denominator(self, value: int, rounding: int = 2, to_str: bool = False) -> Union[str, Tuple[float, int]]:
        numerator = round(self._frac[0] / self._frac[1] * value, rounding)

        if to_str:
            return f"{numerator}/{value}"

        return numerator, value

    def with_numerator(self, value: int, rounding: int = 2, to_str: bool = False) -> Union[str, Tuple[int, float]]:
        denominator = round(value / self._frac[0] / self._frac[1], rounding)

        if to_str:
            return f"{value}/{denominator}"

        return value, denominator

    def __add__(self, other, op=operator.add):

        if isinstance(other, Fraction):
            no, do = other._frac
            ns, ds = self._frac
            lc = self.lcm(ds, do)

            return self.create(op(ns * (lc/ds), no * (lc/do)), lc).reduce()
        
        elif isinstance(other, float):
            no, do = self._to_frac(other)
            ns, ds = self._frac
            lc = self.lcm(ds, do)

            return self.create(op(ns * (lc/ds), no * (lc/do)), lc)
        
        elif isinstance(other, int):
            return self.create(op(self.numerator, other * self.denominator),
                               self.denominator)

        else:
            raise TypeError(f"Unsupported type {type(other)}")

    def __sub__(self, other):
        return self.__add__(other, operator.sub)

    def __mul__(self, other, flip=False):

        if not isinstance(other, (Fraction, float, int)):
            raise TypeError(f"Unsupported type {type(other)}")

        ns, ds = self._frac
        no, do = other._frac if type(other) is Fraction else self._to_frac(other)
        if flip:
            no, do = do, no

        res = [ns * no, ds * do]
        gcd = math.gcd(*res)
        return self.create(*[f // gcd for f in res])

    def __truediv__(self, other):
        return self.__mul__(other, flip=True)

    def __str__(self):
        return f"{self._frac[0]}/{self._frac[1]}"

    def __format__(self, format_spec):
        return str(self.__str__()).__format__(format_spec)
