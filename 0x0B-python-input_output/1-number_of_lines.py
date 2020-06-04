#!/usr/bin/python3
"""Number of lines"""


def number_of_lines(filename=""):
    """[number_of_lines]

    Args:
        filename (str, optional): [description]. Defaults to "".
    """
    with open(filename, encoding='utf-8') as file_line:
        return(len(file_line.readlines()))
