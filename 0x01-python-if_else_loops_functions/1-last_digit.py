#!/usr/bin/python3
import random

number = random.randint(-99999999, 99999999)

if number < 0:
    last_digit = -number % 10
    last_digit *= -1
else:
    last_digit = number % 10

if last_digit == 0:
    second_string = "and is 0"
elif last_digit < 6:
    second_string = "and is less than 6 and not 0"
elif last_digit > 5:
    second_string = "and is greater than 5"

print(f"Last digit of {number:d} is {last_digit:d} {second_string}")
