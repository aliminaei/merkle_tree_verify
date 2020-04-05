import unittest
import main

class TestMain(unittest.TestCase):

    def test_load_timestamp_list_from_file(self):
        with self.assertRaises(ValueError):
            main.load_timestamp_list_from_file("")

        with self.assertRaises(ValueError):
            main.load_timestamp_list_from_file("./bag/timestamp2.json")

        with self.assertRaises(IOError):
            main.load_timestamp_list_from_file("./bag/timestamp3.json")

        self.assertIsInstance(main.load_timestamp_list_from_file("./bag/timestamp.json"), list)

    def test_verify_hash(self):
        self.assertFalse(main.verify_hash("", "", ""))


if __name__ == "__main__":
    unittest.main()