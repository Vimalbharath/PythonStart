import math
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[False for _ in range(n)] for _ in range(n)]
        self.helper(board,0)

    def helper(self,board,r):
        if r==len(board):
            ans = [['Q' if val else '.' for val in row] for row in board]
            print(ans)
            return
        for c in range(len(board[0])):
            if self.isSafe(board,r,c):
                board[r][c]=True
                self.helper(board,r+1)
                board[r][c]=False

    def isSafe(self,board,r,c):
        for i in range(r):
            if board[i][c]:
                return False
        leftMin=min(r,c)
        for i in range(1,leftMin+1):
            if board[r-i][c-i]:
                return False
        rightMin=min(r,len(board[0])-1-c)
        for i in range(1,rightMin+1):
            if board[r-i][c+i]:
                return False

        return True


def main():
    sol=Solution()
    sol.solveNQueens(4)

main()