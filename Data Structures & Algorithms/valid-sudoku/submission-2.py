class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_set = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in row_set:
                    return False
                else:
                    row_set.add(board[row][col])
        for col in range(9):
            col_set= set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in col_set:
                    return False
                else:
                    col_set.add(board[row][col])
        for row_start in range(0,9,3):
            for col_start in range(0,9,3):
                box_set= set()

                for row in range(row_start, row_start +3):
                    for col in range(col_start, col_start +3):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in box_set:
                            return False
                        
                        box_set.add(board[row][col])
        return True
