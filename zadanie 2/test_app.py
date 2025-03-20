import unittest
from app import is_valid_email, rectangle_area, filter_even_numbers, format_date, is_palindrome

class TestApp(unittest.TestCase):

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("invalid-email"))
        self.assertFalse(is_valid_email("test@.com"))

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertRaises(ValueError, rectangle_area, -2, 3)
        self.assertEqual(rectangle_area(0, 5), 0)

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(filter_even_numbers([]), [])
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])

    def test_format_date(self):
        self.assertEqual(format_date("2025-03-20"), "20.03.2025")
        self.assertRaises(ValueError, format_date, "20-03-2025")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Ala"))
        self.assertFalse(is_palindrome("Python"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

if __name__ == '__main__':
    unittest.main()
