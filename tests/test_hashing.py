import unittest
from src.hashing import hash_string

class TestHashing(unittest.TestCase):
    def test_sha256(self):
        self.assertEqual(hash_string("hello", "sha256"),
                             "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824")
        
    def test_md5(self):
        result = hash_string("hello", "md5")
        self.assertEqual(result, "5d41402abc4b2a76b9719d911017c592")

if __name__ == "__main__":
    unittest.main()