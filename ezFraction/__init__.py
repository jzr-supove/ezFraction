import math
import operator
from typing import Tuple, Union, List


class Fraction:
    rounding: int
    decimal:  float
    _frac:    List[int]

    def __init__(self, number: Union[float, int, str], denominator: Union[int, str] = None, reduce: bool = True, rounding: int = 5):
        self.rounding = rounding
        if denominator:
            self.decimal = int(number) / int(denominator)
            self._frac = [int(number), int(denominator)]
        else:
            self.decimal = float(number)
            self._frac = self._to_frac(self.decimal)
        if reduce:
            self.reduce()

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
        gcd = math.gcd(*self._frac)
        reduced = [f // gcd for f in self._frac]

        if new_obj:
            return Fraction(*reduced)

        self._frac = reduced
        return self

    def enlarge(self, multiplier: int = 2, new_obj: bool = False):
        if new_obj:
            return Fraction(self._frac[0] * multiplier, self._frac[1] * multiplier)

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
        
        if not isinstance(other, (Fraction, float, int)):
            raise TypeError(f"Unsupported type {type(other)}")

        ns, ds = self._frac
        no, do = other._frac if type(other) is Fraction else self._to_frac(other)
        lc = self.lcm(ds, do)

        return Fraction(op(ns * (lc/ds), no * (lc/do)), lc)

    def __sub__(self, other):
        return self.__add__(other, operator.sub)

    def __mul__(self, other, flip=False):

        if not isinstance(other, (Fraction, float, int)):
            raise TypeError(f"Unsupported type {type(other)}")

        ns, ds = self._frac
        no, do = other._frac if type(other) is Fraction else self._to_frac(other)
        if flip:
            no, do = do, no

        return Fraction(ns * no, ds * do)

    def __truediv__(self, other):
        return self.__mul__(other, flip=True)

    def __str__(self):
        return f"{self._frac[0]}/{self._frac[1]}"

    def __format__(self, format_spec):
        return str(self.__str__()).__format__(format_spec)
