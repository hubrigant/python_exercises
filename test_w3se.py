import w3se

def test_Answer1():
    correctAnswer1 = """Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
    """
    correctAnswer2 = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!"

    assert w3se.q1m1(correctAnswer1) == correctAnswer1
    assert w3se.q1m2(correctAnswer2) == correctAnswer1
