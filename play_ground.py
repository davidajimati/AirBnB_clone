#!/usr/bin/python3
def add(**kwargs):
    res = 0
    for value in kwargs.values():
        res += value
    print(res)

add(a = 34, b = 88)