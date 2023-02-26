# unicode-range-calc

Calculates what ranges of Unicode characters are used in a set of files.

Created to find out what Unicode ranges to use when creating a Font Asset for TextMesh Pro.

## Usage Example

```
# Note that the result is printed in brackets so that you don't miss any invisible characters

$ python3 unicode-range-calc.py \
  --format characters \
  examples/lorem_latin.txt examples/lorem_cyrillic.txt
[ ,.EHLQabcdehilmnopqrstuvДЕИЛабвгдеилмнопрстуфхця]

$ python3 unicode-range-calc.py \
  --format characters \
  --ignore-chars " ,." \
  examples/lorem_latin.txt examples/lorem_cyrillic.txt
[EHLQabcdehilmnopqrstuvДЕИЛабвгдеилмнопрстуфхця]

$ python3 unicode-range-calc.py \
  --format characters \
  --ignore-chars " ,." \
  --require-chars "ABCDEFGHIJKLMNOPQRSTUVWXYZ@{}" \
  examples/lorem_latin.txt examples/lorem_cyrillic.txt
[@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdehilmnopqrstuv{}ДЕИЛабвгдеилмнопрстуфхця]
```