import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    # for num in heap:
    #     print(f'heap = {heap}')
    #     temp = heapq.heappop(heap)
    #     print(f'temp = {temp}')
    #     print(f'heap now = {heap}')
    #     print("===================")

    # for i in range(len(heap)):


    # return []
    return [heapq.heappop(heap) for i in range(len(heap))]


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
