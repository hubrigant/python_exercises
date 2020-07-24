#!/usr/bin/env python3

"""
    W3Schools Python Exercises
    Exercise 1, method 2
    24 July 2020
    Jon Williams
"""

"""
Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
"""

text = ("Twinkle, twinkle, little star,",
        "How I wonder what you are!",
		"Up above the world so high,",
		"Like a diamond in the sky.",
        "Twinkle, twinkle, little star,",
        "How I wonder what you are")

for line in text:
    if line[0] is 'H':
        leader = "	"
    elif line[0] is 'U' or line[0] is 'L':
        leader = "	" * 2
    else:
        leader = ""
    print("{}{}".format(leader, line))
