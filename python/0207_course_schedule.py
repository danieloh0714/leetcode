# Time complexity: O(V+E)
# Space complexity: O(V+E)
def can_finish(num_courses: int, prerequisites: list) -> bool:
    adj_list = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        adj_list[course].append(prereq)

    states = [-1 for _ in range(num_courses)]
    def cycle_check(course):
        state = states[course]
        if state == 0: return True
        if state == 1: return False
        states[course] = 0
        for prereq in adj_list[course]:
            if cycle_check(prereq): return True
        states[course] = 1
        return False

    for course in range(num_courses):
        if cycle_check(course): return False

    return True
