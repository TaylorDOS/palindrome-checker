from abc import ABC, abstractmethod

class PalindromeChecker(ABC):
    """Abstract base class for palindrome checkers."""
    @abstractmethod
    def is_palindrome(self, data):
        pass

class StringPalindromeChecker(PalindromeChecker):
    """Checks if a given string is a palindrome after cleaning it."""
    def is_palindrome(self, data: str) -> bool:
        filtered_data = ''.join(c.lower() for c in data if c.isalnum())
        return filtered_data == filtered_data[::-1]

class IntegerPalindromeChecker(PalindromeChecker):
    """Checks if a given integer is a palindrome without string conversion."""
    def is_palindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10

class PalindromeFactory:
    """Factory class to return the appropriate palindrome checker."""
    @staticmethod
    def get_checker(data):
        if isinstance(data, str):
            return StringPalindromeChecker()
        elif isinstance(data, int):
            return IntegerPalindromeChecker()
        else:
            raise ValueError("Unsupported data type")