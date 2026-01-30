import unittest
from app import instruction

class TestApp(unittest.TestCase):
    def test_instruction(self):
        self.assertEqual(instruction(), "result")

if __name__ == "__main__":
    unittest.main()