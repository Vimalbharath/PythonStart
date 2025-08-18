def main():
    board=[[True,True,True],
           [True,True,True],
           [True,True,True]]
    allpath('',board,0,0)

def allpath(p,board,r,c):
    if r==len(board)-1 and c==len(board[0])-1:
        print(p)
        return 
    if board[r][c]==False:
        return
    board[r][c]=False
    if r<len(board)-1:
        allpath(p+'D',board,r+1,c)
    if c<len(board[0])-1:
        allpath(p+'R',board,r,c+1)
    if r>0:
        allpath(p+'U',board,r-1,c)
    if c>0:
        allpath(p+'L',board,r,c-1)
    board[r][c]=True

main()