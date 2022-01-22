# 최소 힙에서 힙에 입력할 때와 출력할 때 단순히 -부호를 넣어준다
import heapq

# 내림차순 힙 정렬


def heapsort(iterable):
    h = []
    result = []
    for i in iterable:
        heapq.heappush(h, -i)
    for j in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
