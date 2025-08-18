from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[False for _ in range(n)] for _ in range(n)]
        self.helper(board,0,0)

    def helper(self,board,r,c):
        if r==len(board):
            ans = [['Q' if val else '.' for val in row] for row in board]
            print(ans)
            return
        if board[r][c]==False:
            if not self.isSafe(board,r,c):
                board[r][c]=True
                self.helper(board,r+1,c)
                board[r][c]=False

    def isSafe(self,board,r,c):
        while r>-1:
            if(board[r][c]==False):
                return False
            r=r-1
        return False


def main():
    sol=Solution()
    sol.solveNQueens(4)

main()