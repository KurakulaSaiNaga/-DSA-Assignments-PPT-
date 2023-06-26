class Solution:
    def score(self,nums,k):
        a = max(nums) - k
        b = min(nums) + k
        return max(0, a - b)
print(Solution().score([0,10],2))