import numpy as np


def binary_search(slist, item):
    """
    二分法：时间复杂度为O(logN)，N为操作数;算法的速度指的并非时间，而是操作数的增速。
    :param slist: 源集合，必须有序
    :param item: 待查询的项
    :return: 返回项在集合的位置
    """
    low = 0
    high = len(slist) - 1

    while low <= high:
        mid = (low+high)//2
        guess = slist[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


a = np.linspace(1, 16, 16)

guess_index = binary_search(a, 3)

print(guess_index)
