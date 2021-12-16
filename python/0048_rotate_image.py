# Time complexity: O(n^2)
# Space complexity: O(1)
def rotate(matrix: list) -> None:
    for r in range(len(matrix)):
        for c in range(r, len(matrix[0])):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for r in range(len(matrix)):
        for c in range(len(matrix[0])//2):
            opp = len(matrix)-1-c
            matrix[r][c], matrix[r][opp] = matrix[r][opp], matrix[r][c]
