"""
Q:https://leetcode.com/problems/valid-sudoku/submissions/

T(N) = N^2
S(N) = N
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        # check if row valid
        for i in range(n):
            row = [board[i][j] for j in range(n) if board[i][j] != "."]
            if not self.isValid(row):
                return False
        
        # check if col valid
        for i in range(n):
            col = [board[j][i] for j in range(n) if board[j][i] != "."]
            if not self.isValid(col):
                return False
        
        #check sub-boxes
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                block = [board[k][h] for k in range(i, i+3) \
                         for h in range(j, j+3) if board[k][h] != "."]
                if not self.isValid(block):
                    return False
        
        return True
    
    def isValid(self, arr):
        # check if arr conains duplicate
        return len(arr) == len(set(arr))
    
