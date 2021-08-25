def solve(self, matrix):
        n=len(matrix)
        cycle=int(n/2)
        for i in range(cycle):
            for j in range(i,n-1-i):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][n-1-i]
                matrix[j][n-1-i]=matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j]=matrix[n-1-j][i]
                matrix[n-1-j][i]=temp
                
        return matrix
