#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:i} is positive")
elif number == 0:
    print(f"{number:i} is zero")
else number < 0:
    print(f"{number:i} is negative")

