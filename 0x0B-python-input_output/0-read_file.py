#!/usr/bin/python3
"""Read and prints text"""


def read_file(filename=""):
    """Read

    Args:
        filename (filename, optional_mode)
    """
    with open(filename, encoding='utf-8') as file_read:
        print(file_read.read(), end="")
