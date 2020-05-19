#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            number = number + 1
        except IndexError:
            break
    print()
    return number