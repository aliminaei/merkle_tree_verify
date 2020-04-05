import unittest
import main

class TestMain(unittest.TestCase):

    def test_verify_hash(self):
        self.assertFalse(main.verify_hash("", "", ""))


if __name__ == "__main__":
    unittest.main()