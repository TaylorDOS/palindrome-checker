import unittest
from src.palindrome import StringPalindromeChecker, IntegerPalindromeChecker, PalindromeFactory

class TestPalindrome(unittest.TestCase):
    """Unit tests for palindrome checkers."""
    
    def setUp(self):
        """Set up instances of palindrome checkers before each test."""
        self.string_checker = StringPalindromeChecker()
        self.int_checker = IntegerPalindromeChecker()
    
    def test_string_palindromes(self):
        """Test palindrome functionality for strings."""
        self.assertTrue(self.string_checker.is_palindrome("Was it a car or a cat I saw?"))
        self.assertFalse(self.string_checker.is_palindrome("Hello World"))
        self.assertTrue(self.string_checker.is_palindrome("!?"))
    
    def test_integer_palindromes(self):
        """Test palindrome functionality for integers."""
        self.assertTrue(self.int_checker.is_palindrome(121))
        self.assertFalse(self.int_checker.is_palindrome(-121))
        self.assertFalse(self.int_checker.is_palindrome(10))
    
    def test_factory(self):
        """Test the factory class returns correct instances."""
        self.assertIsInstance(PalindromeFactory.get_checker("hello"), StringPalindromeChecker)
        self.assertIsInstance(PalindromeFactory.get_checker(12321), IntegerPalindromeChecker)
        with self.assertRaises(ValueError):
            PalindromeFactory.get_checker(12.34)

if __name__ == "__main__":
    unittest.main()