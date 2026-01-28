class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_set = [set() for i in range(9)]
        c_set = [set() for i in range(9)]
        matrix = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in r_set[i] or board[i][j] in c_set[j] or board[i][j] in matrix[i//3][j//3]:
                    return False
                r_set[i].add(board[i][j])
                c_set[j].add(board[i][j])
                matrix[i//3][j//3].add(board[i][j])
        return True