from contextlib import closing
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode
import redis
from pathlib import Path
import json
import time

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)

default_redis_client = redis.Redis(connection_pool=pool)

def cache_token(target: str, token_key, expire_key, r_token_key=None):
    up = urlparse(target)
    if up.scheme == 'file':
        f = Path(up.path)
    elif up.scheme == 'redis':
        q_dict = parse_qs(up.query)
        key = q_dict.pop('key')[0]
        if up.netloc:
            url = urlunparse(up._replace(query=urlencode(q_dict)))
            f = redis.from_url(url)
        else:
            f = default_redis_client
    if not f:
        raise ValueError('target must start with file or redis')
    
    def decr(func):

        def load_conf() -> dict:
            if isinstance(f, Path) and f.is_file():
                with closing(f.open()) as conf_file:
                    return json.load(conf_file)
            elif f.exists(key):
                return json.loads(f.get(key))
        def save_conf(data):
            if isinstance(f, Path):
                with closing(f.open('w')) as conf_file:
                    json.dump(data, conf_file)
            elif (secs := data.get(expire_key, 0)) > 0:
                f.setex(key, secs*2, json.dumps(data))
            else:
                f.set(key, json.dumps(data))
        def wrapper(*args, **kwargs):
            if (conf := load_conf()):
                if time.time() <= float(conf.get(expire_key, 0)) and (token := conf.get(token_key)):
                    return token
                if r_token_key and (r_token := conf.get(r_token_key)):
                    args = [*args, r_token]
            conf = func(*args, **kwargs)
            save_conf(conf)
            return conf.get(token_key)
        return wrapper
    return decr


if __name__ == '__main__':
    drc = default_redis_client
    print(drc.keys())
    c = redis.from_url('redis://localhost:6379/0')
    print(c.keys())

    @cache_token('redis://localhost:6379/3?key=bbc.conf', 'key', 'e')
    def get_token():
        return {'key': 'yes', 'e': 100}
    
    print(get_token())

    # drc.sadd('undone', *(f'ar:{i}' for i in range(10)))
    # drc.expire('undone', 60*5)

    # print(drc.smembers('undone'))