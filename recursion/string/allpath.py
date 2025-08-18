def main():
    path=[[0,0,0],
          [0,0,0],
          [0,0,0]]
    board=[[True,True,True],
           [True,True,True],
           [True,True,True]]
    allpath('',board,0,0,path,0)

def allpath(p,board,r,c,path,count):
    if r==len(board)-1 and c==len(board[0])-1:
        print(p,count)
        path[r][c]=count
        for i in range(len(path)):
            print(path[i])
        return 
    if board[r][c]==False:
        return
    board[r][c]=False
    path[r][c]=count
    if r<len(board)-1:
        allpath(p+'D',board,r+1,c,path,count+1)
    if c<len(board[0])-1:
        allpath(p+'R',board,r,c+1,path,count+1)
    if r>0:
        allpath(p+'U',board,r-1,c,path,count+1)
    if c>0:
        allpath(p+'L',board,r,c-1,path,count+1)
    board[r][c]=True
    path[r][c]=0

main()