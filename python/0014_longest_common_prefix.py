# Time complexity: O(mn)
# Space complexity: O(1)
def longest_common_prefix(strs: list) -> str:
    ans = []
    
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return ''.join(ans)
        ans.append(strs[0][i])

    return ''.join(ans)
