import hashlib
import json
import os

class Timestamp:
    def __init__(self, op, prefix, postfix):
        self.operator = op
        self.prefix = prefix
        self.postfix = postfix

"""
This function should walk through the timestamps and verify message against merkleRoot
Hints: use hashlib.sha256 and hash.hexdigest. message is big-endian while merkleRoot is little-endian.
""" 
def verify_hash(timestamps, message, merkle_root):
    return False


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

if __name__ == "__main__":
    msg = "b4759e820cb549c53c755e5905c744f73605f8f6437ae7884252a5f204c8c6e6"
    merkle_root = "f832e7458a6140ef22c6bc1743f09610281f66a1b202e7b4d278b83de55ef58c"    
    timestamp_list = load_timestamp_list_from_file("./bag/timestamp.json")

    timestamps = []

    if verify_hash(timestamps, msg, merkle_root):
        print("CORRECT!")
    else:
        print("INCORRECT!")