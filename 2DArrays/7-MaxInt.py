class Solution:
    def maxintmat(self,nums,m,n):
        if len(nums)==0:
            return m*n
        matrix = [[0 for i in range(n)] for j in range(m)] # List Comprehension
        n1=len(nums)
        for i in range(n1):
            for j in range(len(matrix)):
                for k in range(len(matrix[0])):
                    if j<nums[i][0] and k<nums[i][1]:
                        matrix[j][k]+=1
        k=max(map(max, matrix))
        print(matrix)
        print(k)
        p=0
        for i in matrix:
            p+=i.count(k)
        return p
print(Solution().maxintmat([[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]],3,3))