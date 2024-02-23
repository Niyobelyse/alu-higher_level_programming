#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

nb = number

if nb >= 0:
    l = nb % 10
    if l > 5:
        print(f"Last digit of {nb} is {l} and is greater than 5")
    elif l == 0:
        print(f"Last digit of {nb} is {l} and is 0")
    elif l < 6:
        print(f"Last digit of {nb} is {l} and is less than 6 and not 0")
else:
    x = -nb % 10
    y = -x
    print(f"Last digit of {nb} is {y} and is less than 6 and not 0")
