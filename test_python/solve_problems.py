def get_triple(arr: list[int], target: int):
    '''无序数组，输出任意一组三个数和为target
    '''
    d = {}
    length = len(arr)
    for i in range(length-2):
        if arr[i] >= target:
            continue
        for j in range(i+1, length-1):
            key = arr[i] + arr[j]
            if key >= target or key in d:
                continue
            d[key] = (i, j)
            for k in range(j+1, length):
                key = target - arr[k]
                if key in d:
                    return *d[key], k


if __name__ == '__main__':
    a, b, c = get_triple([-1, 1,2,3,2,1,4,5,6], 11)
    print(a, b, c)
    