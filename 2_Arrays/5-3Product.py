class Solution:
    def product(self,nums):
        nums.sort()
        a = nums[0] * nums[1] * nums[len(nums) - 1]
        b = nums[-1] * nums[-2] * nums[-3]
        return max(a, b)
print(Solution().product([1,2,3,4]))