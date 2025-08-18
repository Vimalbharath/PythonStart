def main():
    board=[[True,True,True],
           [True,False,True],
           [True,True,True]]
    pathobs('',board,0,0)

def pathobs(p,board,r,c):
    if r==len(board)-1 and c==len(board[0])-1:
        print(p)
        return 
    if board[r][c]==False:
        return
    if r<len(board)-1:
        pathobs(p+'D',board,r+1,c)
    if c<len(board[0])-1:
        pathobs(p+'R',board,r,c+1)
    return 

main()