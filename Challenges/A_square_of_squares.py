
# Task
# Given an integral number, determine if it's a square number:
# In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
# The tests will always use some integral number, so don't worry about that in dynamic typed languages.
import math

def is_square(number):
    return number > -1 and math.sqrt(number) % 1 == 0;

     