# Palindrome Checker

This project provides a **Python-based palindrome checker** for both **strings** and **integers**.  
It follows **clean code principles**, utilizes **design patterns**, and includes **unit tests**.

## Features
- Checks if a **string** is a palindrome (ignores case & non-alphanumeric characters).
- Checks if an **integer** is a palindrome **without converting to a string**.
- Uses **Factory Design Pattern** for extensibility.
- Includes **unit tests** to ensure correctness.
- Follows **Python best practices**.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/TaylorDOS/palindrome-checker.git
   cd palindrome-checker
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
## Usage
### **Checking Palindromes**
```python
from src.palindrome import PalindromeFactory

checker = PalindromeFactory.get_checker("Was it a car or a cat I saw?")
print(checker.is_palindrome("Was it a car or a cat I saw?"))  # Output: True

checker = PalindromeFactory.get_checker(121)
print(checker.is_palindrome(121))  # Output: True
```

## Running Tests
Run unit tests to ensure everything works correctly:
```bash
python -m unittest discover tests
```

Expected Output:
```bash
OK
```

---

## Project Structure
```
palindrome-checker/
│── src/                   # Source code
│   ├── palindrome.py      # Palindrome checking logic
│── tests/                 # Unit tests
│   ├── test_palindrome.py # Test cases
│── .gitignore             # Ignore unnecessary files
│── README.md              # Documentation
```

## License
This project is licensed under the **MIT License**.  
Feel free to modify and use it!

## Contact
For any questions or issues, feel free to reach out!

- GitHub: [TaylorDOS](https://github.com/TaylorDOS)
- Email: haoyi2@hotmail.com