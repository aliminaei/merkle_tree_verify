import hashlib
import json
import os

class Timestamp:
    # Accepted/Supported operators
    accepted_operators = [
        "sha256"
    ]

    def __init__(self, operator, prefix, postfix):
        if not operator:
            raise ValueError("Invalid operator.")

        if operator not in self.accepted_operators:
            raise ValueError("Invalid operator.")

        self.operator = operator
        self.prefix = prefix
        self.postfix = postfix

"""
This function should walk through the timestamps and verify message against merkleRoot
Hints: use hashlib.sha256 and hash.hexdigest. message is big-endian while merkleRoot is little-endian.
""" 
def verify_hash(timestamp_list, message, merkle_root):
    # check if initial message is in a valid hex format
    if not is_hex_bytes(message):
        raise ValueError("Invalid initail message. Initial message should be in valid hex format.")

    # check if merkle root is in a valid hex format
    if not is_hex_bytes(merkle_root):
        raise ValueError("Invalid merkle root. Merkle root should be in valid hex format.")

    merkle_root = change_endian(merkle_root)

    timestamps = []
    # Iterate through the list and parse Timestamp objects
    print("Parsing list of timestamps.")
    for node in timestamp_list:
        timestamp = parse_timestamp(node)
        timestamps.append(timestamp)

    # Navigating through the timestamps!
    for timestamp in timestamps:
        message = timestamp.prefix + message + timestamp.postfix
        message_bytes = bytearray.fromhex(message)
        sha256 = hashlib.sha256(message_bytes)
        message = sha256.hexdigest()

    # checking if the message verifies agains the root!
    return merkle_root == message

def change_endian(hex_string):
    """
    This function changes the endian of a given hex string.
    """
    if not is_hex_bytes(hex_string):
        raise ValueError("The string is not a valid hexadecimal string.")

    message_ba = bytearray.fromhex(hex_string)
    message_ba.reverse()
    return ''.join(format(x, '02x') for x in message_ba)

def is_hex_bytes(hex_string):
    """
    This functoin checks if a given string is a hex string and can be converted to byte array.
    """
    try:
        bytearray.fromhex(hex_string)
    except ValueError:
        return False

    return True


def load_timestamp_list_from_file(filename):
    """
    This function receives a path to a JSON file that contains the timestamps and returns a list of unvalidated/unparsed timestamps.
    """

    if not filename:
        raise ValueError("Invalid File Name.")

    timestamp_list = []

    if not os.path.exists(filename):
        raise IOError("File Not Found.")

    try:
        with open(filename, "rt") as fp:
            timestamp_list = json.load(fp)

    except ValueError:
        raise ValueError("The file is not a valid JSON format.")

    return timestamp_list

def parse_timestamp(node):
    """
    This function receives a timestamp in a list format and returns a Timestamp object.
    """

    if len(node) != 3:
        raise ValueError("Invalid timestamp object.")

    return Timestamp(node[0], node[1], node[2])

if __name__ == "__main__":
    msg = "b4759e820cb549c53c755e5905c744f73605f8f6437ae7884252a5f204c8c6e6"
    merkle_root = "f832e7458a6140ef22c6bc1743f09610281f66a1b202e7b4d278b83de55ef58c"  

    # read all the timestamps from the JSON file as a list
    print("Reading timestamps from file.")
    timestamps = load_timestamp_list_from_file("./bag/timestamp.json")

    if verify_hash(timestamps, msg, merkle_root):
        print("CORRECT!")
    else:
        print("INCORRECT!")