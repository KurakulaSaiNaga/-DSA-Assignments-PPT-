class Solution:
    def transpose(self,matrix):
        a=len(matrix)
        b=len(matrix[0])
        transpose1=[[0 for i in range(a)] for j in range(b)] #List Comprehension
        for i in range(b):
            for j in range(a):
                transpose1[i][j]=matrix[j][i]
        return transpose1
print(Solution().transpose([[1,2,3],[4,5,6]]))