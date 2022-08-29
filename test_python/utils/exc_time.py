import contextlib
from inspect import isgeneratorfunction
from time import time, sleep

def execute_time(func):
    
    def wrapper(*args, **kwargs):
        start = time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time()
            print(f'{func.__name__}() execute time: {end-start}s')

    def wrapper_generator(*args, **kwargs):
        start = time()
        try:
            yield from func(*args, **kwargs)
        finally:
            end = time()
            print(f'{func.__name__}() execute time: {end-start}s')

    # 返回嵌套的函数
    return wrapper_generator if isgeneratorfunction(func) else wrapper


@contextlib.contextmanager
def log_exe_time_ctx(metrics, action=None):
    start_time = time()
    yield
    end_time = time()
    print("info", metrics, action, end_time - start_time)


if __name__ == '__main__':
    class Solution(object):
        @execute_time
        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            hashmap = {}
            for i, num in enumerate(nums):
                hashmap[num] = i
            sleep(2)
            for j, num in enumerate(nums):
                k = hashmap.get(target-num)
                if k is not None and j != k:
                    return [j, k]


    def yi(arr):
        sleep(1.5)
        for i in arr:
            yield i # , i**2

    @execute_time
    def yi2(arr):
        sleep(1)
        yield from yi(arr)


    t = Solution()
    print('mid')
    print(t.twoSum([2, 7, 11, 15], 9))

    t = []
    t.extend(yi2([2, 7, 11, 15]))
    print(t)

    print([(i, i**2) for i in t])

    with log_exe_time_ctx('log', 'act'):
        sleep(2)
        print('mid context')

