class Solution:
    def nonrepeat(self,nums):
        for i in nums:
            if nums.count(i)==1:
                return i
print(Solution().nonrepeat([2,2,1]))