# Time complexity: O(nlog(n))
# Space complexity: O(log(n))
def find_min_arrow_shots(points: list) -> int:
    sorted_points = sorted(points, key=lambda point: point[1])

    arrows = 0

    curr_end = float('-inf')
    for start, end in sorted_points:
        if start > curr_end:
            arrows += 1
            curr_end = end

    return arrows
