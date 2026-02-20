class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,word, path):
            if word == "":
                return True
            if i >= len(board) or j >= len(board[0]) or i <0 or j <0 or board[i][j]!=word[0] or (i,j) in path:
                return False
            else:
                res = False
                path.add((i,j))
                res =  dfs(i+1,j,word[1:],path) or dfs(i-1,j,word[1:],path)or dfs(i,j+1,word[1:],path) or dfs(i,j-1, word[1:],path)
                path.remove((i,j))
                return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,word, set()):
                    return True
        return False
        