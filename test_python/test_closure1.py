#!/usr/bin/env python

def get_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = get_counter()
print c()
