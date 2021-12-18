from queue import PriorityQueue


# Time complexity: O(nlog(k))
# Space complexity: O(k)
def k_closest(points: list, k: int) -> list:
    max_heap = PriorityQueue()

    for x, y in points:
        dist = x*x + y*y
        max_heap.put((-dist, x, y))
        if max_heap.qsize() > k:
            max_heap.get()

    return [[t[1], t[2]] for t in max_heap.queue]
