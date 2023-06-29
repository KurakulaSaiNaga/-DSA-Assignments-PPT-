class Solution:
    def common(self,a,b,c):
        l=[]
        for i in a:
            if i in b and i in c:
                l.append(i)
        return l
print(Solution().common([1,2,3,4,5],[1,2,5,7,9],[1,3,4,5,8]))