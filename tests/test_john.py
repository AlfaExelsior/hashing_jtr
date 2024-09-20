import unittest
from src.john_runner import create_password_file, run_john
import os

class TestJohnRunner(unittest.TestCase):

    def test_password_file_creation(self):
        create_password_file("test_passwords.txt")
        self.assertTrue(os.path.exists("test_passwords.txt"))

    def test_invalid_file(self):
        result = run_john("invalid_file.txt")
        self.assertIn("No such file or directory", result)

if __name__ == "__main__":
    unittest.main()