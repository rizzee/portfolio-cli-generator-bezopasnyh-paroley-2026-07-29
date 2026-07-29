import unittest
from password_generator import generate_password
from pathlib import Path


class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        length = 12
        password = generate_password(length, 'mixed')
        self.assertEqual(len(password), length)

    def test_letters_only(self):
        password = generate_password(10, 'letters')
        self.assertTrue(password.isalpha())

    def test_numbers_only(self):
        password = generate_password(8, 'numbers')
        self.assertTrue(password.isdigit())

    def test_mixed_chars(self):
        password = generate_password(15, 'mixed')
        self.assertTrue(any(c.isalpha() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))


if __name__ == '__main__':
    unittest.main()
