# ezFraction

[![Downloads total](https://pepy.tech/badge/ezfraction)](https://pepy.tech/project/ezFraction)
[![Downloads monthly](https://img.shields.io/pypi/dm/ezfraction.svg)](https://pypi.python.org/pypi/ezFraction)
[![PyPi Package Version](https://img.shields.io/pypi/v/ezfraction.svg)](https://pypi.python.org/pypi/ezFraction)
[![PyPi status](https://img.shields.io/pypi/status/ezfraction.svg)](https://pypi.python.org/pypi/ezFraction)
[![Supported python versions](https://img.shields.io/pypi/pyversions/ezfraction.svg)](https://pypi.python.org/pypi/ezFraction)
[![Github issues](https://img.shields.io/github/issues/goodeejay/ezfraction.svg)](https://github.com/goodeejay/ezfraction/issues)
[![MIT License](https://img.shields.io/pypi/l/ezfraction.svg)](https://opensource.org/licenses/MIT)

**ezFraction** is a custom Python module for working with fractions. 

## Installation

From PyPI:

    pip install ezFraction

From source:

    git clone https://github.com/GooDeeJaY/ezFraction.git
    cd ezFraction
    python -m pip install .

## Usage

Importing and initialization:

```python3
from ezFraction import Fraction

# passing string
Fraction("3.14")        # 157/50

# passing float
Fraction(1.24)          # 31/25

# passing int
Fraction(567)           # 567/1

# passing fraction
Fraction(28, 3)         # 28/3
```

Properties:

```python3
frac = Fraction(4.6)

# Properties
print(frac)             # 23/5
print(frac.decimal)     # 4.6
print(frac.numerator)   # 23
print(frac.denominator) # 5
print(frac.tuple)       # (23, 5)
```

By default fractions will be rounded to 5 decimal places, if you want more or less precision you can set different rounding or even switch off the rounding:

```python3
print(Fraction(3.14))                   # 333333/100000
print(Fraction(3.14, rounding=None))    # 4166666666666667/1250000000000000
```

When initializing `Fraction`, we can set `reduce` to `False` in order to get unreduced fraction:

```python3
print(Fraction(18.5))                   # 37/2
print(Fraction(18.5, reduce=False))     # 185/10
```

Also, there are `.reduce()` and `.enlarge()` methods that perform actions that their name tells. Both methods have `new_obj` parameter which is used to create new `Fraction` instances rather than applying methods to themselves. Apart from `.reduce()`, `.enlarge()` accepts one additional argument `multiplier` that is used to set the different multiplier for enlargement rather than 2 (default).

```python3
frac = Fraction(20.5) 
print(frac)                         # 41/2
print(frac.enlarge())               # 82/4
print(frac.enlarge(multiplier=3))   # 246/12
frac2 = frac.reduce(new_obj=True)
print(frac2, frac)                  # 41/2 246/12
```

You can use `.with_denominator()` method in order to set custom denominator:

```python3
frac = Fraction(0.32)                               # 8/25
custom = frac.with_denominator(35, to_str=True)     # 11.2/35
```

Since this creates an invalid fraction, conversion will not be saved in Fraction instances but rather will be returned as a tuple (default) or string. Also, there is a `.with_numerator()` method that does the same thing but with a numerator.

These methods can be useful when comparing fractions with others. For example, we have fractions 8/25 and 9/35, telling which one is greater by glance is not so easy. So here comes the aid of `.with_denominator()` method by which we convert 8/25 to 11.2/35. 
Now it is easy to tell that 11.2/35 is greater than 9/35

Last but not least, you can perform arithmetic operations with Fraction objects:

```python3
frac1 = Fraction(0.48)      # 12/25
frac2 = Fraction(1.52)      # 38/25

print(frac1 + frac2)        # 2/1
print(frac1 - frac2)        # -26/25
print(frac1 * frac2)        # 456/625
print(frac1 / frac2)        # 6/19
```
