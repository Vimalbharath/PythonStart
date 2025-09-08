import math

class GraphMatrix:
    def __init__(self,num_vertices=0):
        self.matrix=[[]]
        self.vertices={}

    def addVertex(self,name):
        self.vertices[name]=len(self.vertices)
        if not self.matrix or not self.matrix[0]:
            self.matrix=[[0]]
            return
        
        self.matrix=self.increase_matrix_size(self.matrix)
        size=len(self.matrix)
        self.matrix[size-1][size-1]=0

        for i in self.matrix:
            for a in i:
                print(a,end=" ")
            print()
        print(self.vertices)

    def increase_matrix_size(self,matrix):

        if not matrix or not matrix[0]:
            print("Error: The input matrix is empty.")
            return [[]]
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        new_matrix = [[math.inf] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(rows):
            for j in range(cols):
                new_matrix[i][j] = matrix[i][j]
                
        return new_matrix
    
if __name__=="__main__":
    graph=GraphMatrix()
    graph.addVertex("a")
    graph.addVertex("b")