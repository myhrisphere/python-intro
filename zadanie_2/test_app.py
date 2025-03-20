import unittest
from app import is_valid_email, rectangle_area, filter_even_numbers, convert_date_format, is_palindrome

class TestApp(unittest.TestCase):

    def setUp(self):
        # Przygotowanie danych testowych
        self.valid_emails = ["test@example.com", "user.name@domain.co", "valid123@mail.org"]
        self.invalid_emails = ["invalid@", "user@.com", "missing@domain"]
        self.date_samples = [("12/05/2022", "2022-05-12"), ("01/01/2000", "2000-01-01")]

    # Testy dla funkcji is_valid_email
    def test_valid_emails(self):
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_invalid_emails(self):
        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

    # Testy dla funkcji rectangle_area
    def test_rectangle_area_valid(self):
        self.assertEqual(rectangle_area(5, 4), 20)
        self.assertEqual(rectangle_area(10, 10), 100)

    def test_rectangle_area_invalid(self):
        with self.assertRaises(ValueError):
            rectangle_area(-1, 5)
        with self.assertRaises(ValueError):
            rectangle_area(0, 3)

    # Testy dla funkcji filter_even_numbers
    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(filter_even_numbers([]), [])

    def test_filter_even_numbers_with_invalid_data(self):
        self.assertEqual(filter_even_numbers([1, "two", 3, 4.5, 6]), [6])

    # Testy dla funkcji convert_date_format
    def test_convert_date_format_valid(self):
        for date_str, expected in self.date_samples:
            with self.subTest(date_str=date_str):
                self.assertEqual(convert_date_format(date_str), expected)

    def test_convert_date_format_invalid(self):
        with self.assertRaises(ValueError):
            convert_date_format("32/01/2022")
        with self.assertRaises(ValueError):
            convert_date_format("2022/01/01")

    # Testy dla funkcji is_palindrome
    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("racecar"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("test case"))

if __name__ == '__main__':
    unittest.main()
