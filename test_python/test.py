
from __future__ import annotations
from collections import UserDict
from dataclasses import dataclass, fields

from enum import Enum
from datetime import datetime, timedelta
import sched
import string

# from typing_extensions import Self

# from test_dj.helpper.apps import cron_job


class AA:
    a: Self

    name = "AA"
    print(f'load AA {datetime.now()}')

    def __init__(self, n=0) -> None:
        self.ne = n
        print(f'init AA {self.ne}')

    def set_n(self, n):
        self.next = AA(n)

    def __str__(self):
        return f'{self.__class__.name}({self.ne})'


class BB(AA):
    name = "BB"

    def __init__(self, n=0) -> None:
        super().__init__(n)

    @classmethod
    def get_instance_cls(cls, key):
        if 'b' in key:
            return cls
        else:
            return cls.mro()[1]
    
    def __str__(self):
        return f'{self.__class__.name}({self.ne}) ' + super().__str__()


@dataclass
class MyClass:
    my_field: str
    my_other_field: int

    @classmethod
    def from_dict(cls, dict):
        return cls(*[dict[f.name] for f in fields(cls)])

if __name__ == '__main__':
    class Period(timedelta, Enum):
        "different lengths of time"
        _ignore_ = 'Period i'
        Period = vars()
        for i in range(367):
            Period['day_%d' % i] = i

    print(list(Period)[:2])

    # from tzlocal.unix import get_localzone
    # t = get_localzone()
    # print(t, type(t))

    # sch = sched.scheduler()
    # sch.enter(1,2,cron_job, [1, 23, 4], {'f': 12})
    # sch.run()

    cls = BB.get_instance_cls('aaa')
    ins = cls(10)
    print(ins, type(ins))

    cls = BB.get_instance_cls('b')
    ins2 = cls(20)
    print(ins2, type(ins2))

    d = {'my_field': 'a', 'my_other_field': 'b', 'other_field': 'c'}
    # obj = MyClass(**d)
    obj = MyClass.from_dict(d)
    print(obj)
