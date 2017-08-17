#!/usr/bin/env python

from redis import Redis
import time

r = Redis()
for item in r.hgetall('cp-st'):
    print item

r.delete('cp-st', 'cp-st-done')
for i in range(20):
    r.publish('chan1', 'kkk %d' % i)
r.publish('chan1', 'done')
