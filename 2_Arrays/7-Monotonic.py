class Solution:
    def monotone(self,nums):
        k = 1
        c = 1
        for i in range(0, len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                k += 1
            if nums[i] >= nums[i + 1]:
                c += 1
        return k == len(nums) or c == len(nums)
print(Solution().monotone([1,3,2]))