# Time complexity: O(V+E)
# Space complexity: O(V+E)
def find_order(num_courses: int, prerequisites: list) -> list:
    adj_list = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        adj_list[course].append(prereq)

    ordering = []
    states = [-1 for _ in range(num_courses)]
    def cycle_check(course: int) -> bool:
        state = states[course]
        if state == 0: return True
        if state == 1: return False
        states[course] = 0
        for prereq in adj_list[course]:
            if cycle_check(prereq): return True
        states[course] = 1
        ordering.append(course)
        return False

    for course in range(num_courses):
        if cycle_check(course): return []

    return ordering
