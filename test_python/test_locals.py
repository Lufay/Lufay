#!/usr/bin/env python

import test

module = locals()['test']
cls = getattr(module, 'A')
print getattr(cls, 't')
