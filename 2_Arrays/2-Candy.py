class Solution:
    def distributeCandies(self, candyType):
        s=set(candyType)
        a=len(candyType)//2
        b=len(s)
        if a<b:
            return a
        return b
print(Solution().distributeCandies([6,6,6,6]))