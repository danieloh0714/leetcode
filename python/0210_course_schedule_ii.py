# Time complexity: O(V+E)
# Space complexity: O(V+E)
def find_order(num_courses: int, prerequisites: list) -> list:
    adj_list = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        adj_list[course].append(prereq)

    ans = []
    states = [-1 for _ in range(num_courses)]
    def dfs(course: int) -> bool:
        if states[course] == 0: return False
        if states[course] == 1: return True
        states[course] = 0

        for prereq in adj_list[course]:
            if not dfs(prereq): return False

        states[course] = 1
        ans.append(course)
        return True

    for course in range(num_courses):
        if not dfs(course): return []

    return ans
