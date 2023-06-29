class Solution:
    def stair(self,n):
        stair = 0
        i = 1
        while n >= i:
            n -= i
            i += 1
            stair += 1
        return stair
print(Solution().stair(5))