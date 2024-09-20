import unittest
from src.kali_commands import run_kali_command

class TestKaliCommands(unittest.TestCase):
    def test_ls(self):
        result = run_kali_command("ls")
        self.assertIn("src", result)

if __name__ == "__main__":
    unittest.main()