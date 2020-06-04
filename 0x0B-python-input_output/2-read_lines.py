#!/usr/bin/python3
"""Read n Lines"""


def read_lines(filename="", nb_lines=0):
    """This function that reads n lines of a text file (UTF8)

    Args:
        filename (txt): the file to read.
        nb_lines (int): numbers the lines to reader
        and is lower or equal to 0 read all.
    """
    with open(filename, encoding="utf-8") as read_n:
        if nb_lines <= 0:
            print(read_n.read(), end="")
        for i in range(nb_lines):
            print(read_n.readline(), end="")
