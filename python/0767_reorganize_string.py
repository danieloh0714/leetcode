from heapq import heapify, heappop, heappush


# Time complexity: O(nlog(n))
# Space complexity: O(1)
def reorganize_string(s: str) -> str:
    freqs = {}
    for char in s:
        freqs[char] = freqs.get(char, 0) + 1

    max_heap = [(-freq, char) for char, freq in freqs.items()]
    heapify(max_heap)

    ans = []
    prev = None
    while max_heap or prev:
        if not max_heap and prev: return ''

        freq, char = heappop(max_heap)
        ans.append(char)
        freq += 1

        if prev:
            heappush(max_heap, prev)
            prev = None

        if freq < 0:
            prev = (freq, char)

    return ''.join(ans)
