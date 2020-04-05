# Merkle Tree Coding Test

This code uses standard Python routines to parse a Merkle path embedded in a json file.
A Merkle path consists of a series of cryptographic operations, applied to an initial `message`. Each operation has an `Operator` and two operands (`Prefix` and `Postfix`). The output of each operation is `Operator(Prefix + message + Postfix)`, which will become the `message` in the operation. The final `message` is a hash called the Merkel root.
The message is big-endian while merkle_root is little-endian.
