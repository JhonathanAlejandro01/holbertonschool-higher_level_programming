#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_total = 0
    num_uniq = set(my_list)
    for i in num_uniq:
        list_total = list_total + i
    return list_total
