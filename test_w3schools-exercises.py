import pytest
from w3schools_examples.w3schools_examples import q1m1

def TestAnswer1(self):
    correctAnswer1 = """
Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
    """

    assert q1m1(correctAnswer1) == correctAnswer1

