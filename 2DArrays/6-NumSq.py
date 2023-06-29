class Solution:
    def numsq(self,nums):
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]**2
        nums.sort()
        return nums
print(Solution().numsq([-4,-1,0,3,10]))