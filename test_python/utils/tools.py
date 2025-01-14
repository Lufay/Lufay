import hashlib
import inspect
import itertools
from typing import Iterable


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


class classproperty:
    def __init__(self, method_or_cached):
        if callable(method_or_cached):
            self.method = method_or_cached
            self.cached = False
        else:
            self.cached = bool(method_or_cached)
    
    def __call__(self, method):
        self.method = method
        return self
    
    def __set_name__(self, owner, name):
        self.__name__ = name
    
    def __get__(self, ins, owner):
        if not self.cached:
            return self.method(owner)
        if not hasattr(self, '_cache'):
            self._cache = self.method(owner)
        return self._cache
    
    from collections import namedtuple
    property_val = namedtuple('property_val', 'value cached')
    def __set__(self, ins, value):
        if isinstance(value, self.property_val):
            self.cached = bool(value.cached)
            value = value.value
        if callable(value):
            self.method = value
        elif self.cached:
            self._cache = value
        else:
            self.method = lambda c: value

    def __delete__(self, ins):
        if self.cached:
            del self._cache

import threading
from contextlib import contextmanager
class ReadWriteLock:
    """ A lock object that allows many simultaneous "read locks", but
    only one "write lock." """
    
    def __init__(self):
        self._read_ready = threading.Condition()
        self._readers = 0

    def acquire_read(self):
        """ Acquire a read lock. Blocks only if a thread has
        acquired the write lock. """
        with self._read_ready:
            self._readers += 1

    def release_read(self):
        """ Release a read lock. """
        with self._read_ready:
            self._readers -= 1
            if not self._readers:
                self._read_ready.notify_all()

    def acquire_write(self):
        """ Acquire a write lock. Blocks until there are no
        acquired read or write locks. """
        self._read_ready.acquire()
        while self._readers > 0:
            self._read_ready.wait()

    def release_write(self):
        """ Release a write lock. """
        self._read_ready.release()

    @contextmanager
    def rlock(self):
        try:
            self.acquire_read()
            yield self
        finally:
            self.release_read()

    @contextmanager
    def wlock(self):
        try:
            self.acquire_write()
            yield self
        finally:
            self.release_write()


from dataclasses import dataclass
from typing import Callable, Iterable, Tuple
from functools import wraps
@dataclass
class GeneratorWithLen:
    total: int
    seq: Iterable
    refresher: Callable[[], Tuple[int, Iterable]] = None
    has_more: Callable[[], bool] = None

    def __iter__(self):
        if self.seq:
            yield from self.seq
        if self.has_more and self.refresher:
            while self.has_more():
                total, self.seq = self.refresher()
                assert total == self.total
                yield from self.seq

    def __len__(self):
        return self.total
    
    @classmethod
    def simple(cls, total):
        def inner(func):
            @wraps(func)
            def d(*args, **kwargs):
                return cls(total, func(*args, **kwargs))
            return d
        return inner
    

if __name__ == '__main__':
    @generator_partition(10)
    def g1(arr):
        for i in arr:
            yield f'hello {i}'

    for k in g1(i for i in range(100)):
        print(k)

    # import toolz
    # for t in toolz.partition_all(10, (i for i in range(101))):
    #     print(t)

    md = md5(b'fafafaf2414')
    print(len(md), md)

    from functools import cached_property,wraps
    class Test:
        def __init__(self):
            self._t = 998

        def ff(self):
            ...

        @classproperty
        def engine(cls):
            print('in engine')
            return 'connect'
        
        @cached_property
        def t(self):
            return self._t
    
    total = 10
    count = 0
    import random
    @GeneratorWithLen.simple(10)
    def la(n):
        yield from range(n)

    t = la(3)

    print(len(t))
    print(list(t))

    def get_new_generator():
        total = 10
        count = 0
        def r():
            nonlocal count
            n = random.randint(1, total-count)
            print(n)
            count += n
            return total, [random.random() for i in range(n)]
        return GeneratorWithLen(total, [], r, lambda: count < total)
    it = get_new_generator()
    print(len(it))
    for t in it:
        print(t)
    print(len(it))