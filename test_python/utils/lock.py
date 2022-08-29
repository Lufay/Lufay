import contextlib
import time

import redis

from redis_util import default_redis_client


@contextlib.contextmanager
def redis_lock(key, redis_client: redis.Redis = default_redis_client, timeout=5, retry=(30, 0.1)):
    try:
        retry_times, retry_interval = retry
        for i in range(retry_times):
            if redis_client.set(key, 1, ex=timeout, nx=True):
                yield True
                redis_client.delete(key)
                break
            else:
                time.sleep(retry_interval)
        else:
            yield False
    except TypeError:
        yield redis_client.set(key, 1, ex=timeout, nx=True)
        redis_client.delete(key)
