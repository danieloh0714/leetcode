# Time complexity: O(n)
# Space complexity: O(n)
def top_k_frequent(nums: list, k: int) -> list:
    n_to_freq = dict()
    for n in nums:
        n_to_freq[n] = n_to_freq.get(n, 0)+1

    freq_to_n = dict()
    max_freq = 0
    for n, freq in n_to_freq.items():
        max_freq = max(max_freq, freq)
        if freq not in freq_to_n:
            freq_to_n[freq] = []
        freq_to_n[freq].append(n)

    ans = []
    count = 0
    while max_freq > 0:
        if max_freq in freq_to_n:
            for n in freq_to_n[max_freq]:
                ans.append(n)
                count += 1
                if count == k: return ans
        max_freq -= 1

    return ans
