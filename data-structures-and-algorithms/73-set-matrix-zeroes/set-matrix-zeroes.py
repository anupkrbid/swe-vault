class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        # since matrix[0][0] collides with roow and column set the matrix[m][0] column indecator with this variable
        col0 = None

        # use 0'th row and column to mark if the whole row or column needs to be changed to zero 
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # mark row using 0'th column
                    matrix[i][0] = 0
                    # mark 0'th column using col0 and rest using 0'th row 
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0
                    
        # modify marked rows to zero except the 0'th index, as marked colums are yet to be modified 
        for i in range(m-1, 0, -1):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        # modify marked columns to zero except the 0'th index, as col0 will be used to transform that 
        for i in range(n-1, 0, -1):
            if matrix[0][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0
        
        # modify 0'th row to zero if matrix[0][0] is marked
        if matrix[0][0] == 0:
            for i in range(n):
                matrix[0][i] = 0
        
        # modify 0'th column to zero if col0 is marked
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0
        