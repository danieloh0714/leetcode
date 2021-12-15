# Time complexity: O(1)
# Space complexity: O(1)
def is_valid_sudoku(board: list) -> bool:
    seen = set()

    for r in range(len(board)):
        for c in range(len(board[0])):
            curr = board[r][c]
            if curr != '.':
                row = f'row{r}{curr}'
                col = f'col{c}{curr}'
                box = f'box{r//3}{c//3}{curr}'
                if row in seen or col in seen or box in seen:
                    return False
                seen.add(row)
                seen.add(col)
                seen.add(box)

    return True
