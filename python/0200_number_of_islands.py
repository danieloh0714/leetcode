# Time complexity: O(mn)
# Space complexity: O(mn)
def num_islands(grid: list) -> int:
    islands = 0

    visited = set()

    def dfs(r: int, c: int) -> bool:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]): return False
        if grid[r][c] == '0' or (r, c) in visited: return False
        visited.add((r, c))
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r+1, c)
        dfs(r, c-1)
        return True

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if dfs(r, c): islands += 1

    return islands
