import pickle
from utils.redis_util import default_redis_client

class TopErrPsmsDesc:
    def __init__(self) -> None:
        self.psms = []

    def __set__(self, ins, value):
        self.psms = value
        vb = pickle.dumps(value)
        default_redis_client.setex(HotService.top_err_psms_cache_name, 24*60*60, vb)

    def __get__(self, ins, owner=None):
        if self.psms:
            return self.psms
        b_psms = default_redis_client.redis_client.get(HotService.top_err_psms_cache_name)
        return pickle.loads(b_psms)
    

class HotService:
    top_err_psms_cache_name = 'boe_top_err_psms'
    top_err_psms = TopErrPsmsDesc()


if __name__ == '__main__':
    HotService().top_err_psms = ['a', 'b', 'c', 'd']
    print(HotService.top_err_psms)
    HotService().top_err_psms = ['e', 'f', 'g', 'h']
    print(HotService.top_err_psms)