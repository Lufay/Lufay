import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)

default_redis_client = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    drc = default_redis_client
    print(drc.keys())

    # drc.sadd('undone', *(f'ar:{i}' for i in range(10)))
    # drc.expire('undone', 60*5)

    # print(drc.smembers('undone'))

    job_key = 'apscheduler.jobs'
    job_ids = drc.hkeys(job_key)
    print(drc.hmget(job_key, job_ids))