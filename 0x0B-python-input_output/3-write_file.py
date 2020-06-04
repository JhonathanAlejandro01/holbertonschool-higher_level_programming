#!/usr/bin/python3
""" function that writes & returns number of characters"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
        and returns the number of characters written:

    Args:
        filename (str): the name file.
        text (text): text to write.
    """
    with open(filename, mode="w", encoding='utf-8') as f_write:
        f_write.write(text)
        return(len(text))
