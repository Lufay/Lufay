import hashlib
import inspect
import itertools
from typing import Iterable

import toolz


def md5(s, encoding="utf-8"):
    m = hashlib.md5()
    if encoding and isinstance(s, str):
        s = s.encode(encoding)
    m.update(s)
    return m.hexdigest()


def generator_partition(size):
    def decorator(func):
        assert inspect.isgeneratorfunction(func)
        def wrapper(*args, **kwargs):
            assert isinstance(args[0], Iterable)
            gen = (i for i in args[0])
            try:
                while True:
                    t = next(gen)
                    yield from func(itertools.chain([t], itertools.islice(gen, size-1)))
            except StopIteration:
                pass
        
        return wrapper
    return decorator


if __name__ == '__main__':
    @generator_partition(10)
    def g1(arr):
        for i in arr:
            yield f'hello {i}'

    for k in g1(i for i in range(100)):
        print(k)

    for t in toolz.partition_all(10, (i for i in range(101))):
        print(t)

    md = md5(b'fafafaf2414')
    print(len(md), md)