#!/usr/bin/env python
import operator


a = {"a": 9, "b": 8, "c": 7}
b = {"b": 1, "c": 2, "d": 3}
c = {"c": 1, "d": 999, "e": 3}

print(a | b| c)

def get(m, func):
    for t in m:
        yield func(t)

print(list(get(a.items(), operator.itemgetter(0))))

print(sorted(a.items(), key=operator.itemgetter(0), reverse=True))
