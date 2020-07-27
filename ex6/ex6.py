#!/usr/bin/env python3


"""
    W3Schools Python Exercises
    Exercise 5
    24 July 2020
    Jon Williams
"""

input_str = input("Input a comma-separated list of integers: ")
int_list = (int( x ) for x in input_str.split(',') for y in x.lstrip())

print(int_list)
print(int_list[0])
print(int_list[0,-1])
