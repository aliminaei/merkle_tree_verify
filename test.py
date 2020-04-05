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

    def test_parse_timestamp(self):
        # Invalid/Empty operator
        node = [
          "",
          "",
          "e3be16e996ecf573979ca58498c50029"
        ]
        with self.assertRaises(ValueError):
            main.parse_timestamp(node)

        # Invalid/Unsopprted operator
        node = [
          "1234",
          "",
          "e3be16e996ecf573979ca58498c50029"
        ]
        with self.assertRaises(ValueError):
            main.parse_timestamp(node)

        # Missing field in Timestamp
        node = [
          "sha256",
          "1234",
        ]
        with self.assertRaises(ValueError):
            main.parse_timestamp(node)

        # Extra field in Timestamp
        node = [
          "sha256",
          "1234",
          "1234",
          "1234"
        ]
        with self.assertRaises(ValueError):
            main.parse_timestamp(node)

        # Empty prefix and postfix
        node = [
          "sha256",
          "",
          ""
        ]
        self.assertIsInstance(main.parse_timestamp(node), main.Timestamp)
        
        # Empty postfix
        node = [
          "sha256",
          "1234",
          ""
        ]
        self.assertIsInstance(main.parse_timestamp(node), main.Timestamp)
        
        # Empty prefix
        node = [
          "sha256",
          "",
          "1234"
        ]
        self.assertIsInstance(main.parse_timestamp(node), main.Timestamp)
        
        # Both prefix and postfix not empty
        node = [
          "sha256",
          "1234",
          "5678"
        ]
        self.assertIsInstance(main.parse_timestamp(node), main.Timestamp)
        

    def test_verify_hash(self):
        with self.assertRaises(ValueError):
            main.verify_hash([], "NOT HEX", "aa")

        with self.assertRaises(ValueError):
            main.verify_hash([], "aa", "NOT HEX")

        with self.assertRaises(ValueError):
            main.verify_hash([], "NOT HEX", "NOT HEX")

        self.assertTrue(main.verify_hash([], "ab", "ab"))

        self.assertFalse(main.verify_hash([], "ab", "cd"))



if __name__ == "__main__":
    unittest.main()