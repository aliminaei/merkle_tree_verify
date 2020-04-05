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
        self.assertFalse(main.is_hex_bytes("1z"))
        self.assertTrue(main.is_hex_bytes(""))
        self.assertTrue(main.is_hex_bytes("11"))
        self.assertTrue(main.is_hex_bytes("ab"))
        self.assertTrue(main.is_hex_bytes("1a"))
        self.assertTrue(main.is_hex_bytes("a1"))

    def test_change_endian(self):
        with self.assertRaises(ValueError):
            main.change_endian("a")
        with self.assertRaises(ValueError):
            main.change_endian("z")
        with self.assertRaises(ValueError):
            main.change_endian("1")
        with self.assertRaises(ValueError):
            main.change_endian("-1")
        with self.assertRaises(ValueError):
            main.change_endian("az")
        with self.assertRaises(ValueError):
            main.change_endian("1z")
        with self.assertRaises(ValueError):
            main.change_endian("111")

        self.assertEqual(main.change_endian(""), "")
        self.assertEqual(main.change_endian("11"), "11")
        self.assertEqual(main.change_endian("12"), "12")
        self.assertEqual(main.change_endian("aa"), "aa")
        self.assertEqual(main.change_endian("ab"), "ab")
        self.assertEqual(main.change_endian("1122"), "2211")
        self.assertEqual(main.change_endian("1234"), "3412")
        self.assertEqual(main.change_endian("abcd"), "cdab")

    def test_verify_hash(self):
        with self.assertRaises(ValueError):
            main.verify_hash([], "NOT HEX", "aa")

        with self.assertRaises(ValueError):
            main.verify_hash([], "aa", "NOT HEX")

        with self.assertRaises(ValueError):
            main.verify_hash([], "NOT HEX", "NOT HEX")

        self.assertFalse(main.verify_hash([], "ab", "cd"))

        self.assertTrue(main.verify_hash([], "ab", "ab"))

        timestamps = []
        timestamp = main.Timestamp("sha256", "", "e3be16e996ecf573979ca58498c50029")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256", "", "a74fe7cf3fa4c5847a47c3c8e6ee85094bcbda0c50b05848eef67c96ef8867f5")
        timestamps.append(timestamp)
        self.assertTrue(main.verify_hash(timestamps, "b4759e820cb549c53c755e5905c744f73605f8f6437ae7884252a5f204c8c6e6", "2b042c394497958496ae3394ee2bb8708c40203afc7c38a7160f0cd20fd7a182"))

        timestamps = []
        timestamp = main.Timestamp("sha256","","e3be16e996ecf573979ca58498c50029")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","a74fe7cf3fa4c5847a47c3c8e6ee85094bcbda0c50b05848eef67c96ef8867f5")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","5a732436","9d516c058e000e98")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","0f8b9b68f4a5308a792b01029e6408c2f8a79bf0e72b091bc5463f217fffea08")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","e087f144aec2b08b775ea801f546fb809ad82e23d87fb0fdfe35b3faf459bc59","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","9170c727c5b2dce1ff7fe2e843dca8294f142e6980114c926a9f2b3610756479","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","e392495e8597ae1ec816d3aad4e2411da6d128fd2c568ff87de3f132d0b8164f","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","4e5278a7e6a875910100bd70317133e2071af3787b8b6228b70a70997c179962","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","a244afeae2c7d5aa549d9b2ce2e43c5b6aecfc491efaa4fc24869c648279bd2f")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","fb108fd210f4c3e965849447eca959cdb1cbac3f4e1ce69fe0705c285a80efc5","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","9e6317d313c051d6a5dfb1ad834718fbc5cebdba4a9fbfdda861b21490f350d1","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","67a9e84d15d62fbeef18e3ff610bd915722f384d7bd3bd2a0883ead2bb482305")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","ead42d71454500b8ce18ca8e0b06b93e3e72d50936c2af3a792dda6682ec141e","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","ab1ea49456e9d128e45b888f2bd0a5c16b69f1b351adaae0e766d0bfc56457f9","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","8f52066e1b15860c57152634419f4b9c0aa9a280747ae04d989617f58dca15d1")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","01000000017e492ee25567d49bfe09fb41c9d36a39fbb9757f8401d72800e8a1e9736691700000000000fdffffff0236f0220000000000160014e200dde45eb0529aebe86e16060fb9b109008b560000000000000000226a20","e8bc0700")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","dcc94a971f268e2953aeee073434758d0cfcf627f8f4dc938cba06451bbb70d6","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","c5fc88a22ac9de501d9d7cf12b996165d0bf925ead1101fccc652835a47f086b")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","82f15a2cc3ed0758b009c2470ae6106b4f9b070aa04c22ef4d9afb71a8d148b4","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","5da51ca594d6a6c4c43de78cc97dbf2a070480e56f54e1101bc91d5c14a0df16")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","29ca36df09c596211d02fcb3388a77cd7fcce8bb9be0e1c7ebe48dbe37e037af","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","08f5fa5f008f07f50711556a6579015c1588798749e8f854e4f1b2bc2ab7f165","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","cff11cb99b400fa25b1ca2ad9447fbdb667de93f6c3a0730c208342c2ed6b97e","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","4a0c7480cc6828e425273755bd54807809085900d80d211bc0df5db641f56c24")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","252a52ba681e24e8a3607193544086ac76c43e80edba2f3299a111607147ac4c")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","ee981314ca806770fdb0769359d6fd64b1da35c286541da6226b34790c4c0389","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","fc7523b8e95abcd7176549d9ecb73d467bc92e6118cc902d2a027adeb2185105","")
        timestamps.append(timestamp)
        timestamp = main.Timestamp("sha256","","")
        timestamps.append(timestamp)
        self.assertTrue(main.verify_hash(timestamps, "b4759e820cb549c53c755e5905c744f73605f8f6437ae7884252a5f204c8c6e6", "f832e7458a6140ef22c6bc1743f09610281f66a1b202e7b4d278b83de55ef58c"))


if __name__ == "__main__":
    unittest.main()