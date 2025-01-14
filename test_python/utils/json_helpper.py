import inspect
import json


key_class = '_*_class_*_'
key_data = '_*_data_*_'

def dump_default(*Ts):
    if all(inspect.isclass(T) for T in Ts):
        def default(obj):
            if isinstance(obj, Ts):
                d = obj.__dict__.copy()
                d[key_class] = type(obj).__name__
                return d
            elif isinstance(obj, set):
                return {key_class: 'set', key_data: list(obj)}
            return json.JSONEncoder.default(None, obj)

        return default


def load_hook(*Ts):
    if all(inspect.isclass(T) for T in Ts):
        type_dict = {t.__name__: t for t in Ts}

        def hook(d: dict):
            cls_name = d.pop(key_class, '')
            if cls_name == 'set':
                return set(d.get(key_data))
            T = type_dict.get(cls_name)
            return T(**d) if T else d

        return hook


if __name__ == '__main__':
    from dataclasses import dataclass
    from typing import List
    from collections import namedtuple

    @dataclass
    class A:
        a: int

    NT = namedtuple('NT', 'x y z')
    @dataclass
    class B:
        a: List[A]
        b: int
        c: set
        d: NT


    a = B(
        a = [A(i) for i in range(10)],
        b = 10,
        c = {1, 2, 5},
        d = NT('x', 2.2, 10),
    )

    s = json.dumps(a, default=dump_default(A, B))
    print(s)

    print(json.loads(s, object_hook=load_hook(A, B)))

    from functools import partial
    import pickle
    processor = partial(pickle.dumps, protocol=pickle.HIGHEST_PROTOCOL)
    b = processor(a)
    print(b, type(b))
    print(pickle.loads(b))