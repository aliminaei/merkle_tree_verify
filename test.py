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

    def test_is_hex_bytes(self):
        self.assertFalse(main.is_hex_bytes("a"))
        self.assertFalse(main.is_hex_bytes("z"))
        self.assertFalse(main.is_hex_bytes("1"))
        self.assertFalse(main.is_hex_bytes("-1"))
        self.assertFalse(main.is_hex_bytes("az"))
        self.assertTrue(main.is_hex_bytes(""))
        self.assertTrue(main.is_hex_bytes("11"))
        self.assertTrue(main.is_hex_bytes("ab"))
        self.assertTrue(main.is_hex_bytes("1a"))
        self.assertTrue(main.is_hex_bytes("a1"))

    def test_verify_hash(self):
        with self.assertRaises(ValueError):
            main.verify_hash([], "NOT HEX", "aa")

        with self.assertRaises(ValueError):
            main.verify_hash([], "aa", "NOT HEX")

        with self.assertRaises(ValueError):
            main.verify_hash([], "NOT HEX", "NOT HEX")

        self.assertFalse(main.verify_hash([], "ab", "cd"))

        self.assertTrue(main.verify_hash([], "ab", "ab"))


if __name__ == "__main__":
    unittest.main()