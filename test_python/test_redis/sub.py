#!/usr/bin/env python

from redis import Redis
import time

r = Redis()
#for k in r.keys():
#    print r.smembers(k)

p = r.pubsub()
#print p.execute_command('CHANNELS')
#info = p.subscribe(['chan1', 'chan2'])
p.subscribe('chan1')
for item in p.listen():
    if item['type'] == 'message':
        data = item['data']
        if data == 'done':
            break
        if r.hsetnx('cp-st', data, time.time()):
            if r.hexists('cp-st-done', data):
                r.hdel('cp-st', data)
            else:
                print data, r.hget('cp-st', data)
                time.sleep(3)
                r.hset('cp-st-done', data, time.time())
                print 'rm %s %s' % (data, r.hdel('cp-st', data))
