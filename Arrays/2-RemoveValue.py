class Solution:
    def replace(self,nums, target):
        if target not in nums:
            return 0,nums
        for i in range(len(nums)):
            if nums[i] == target:
                nums[i]='_'
        count=0
        j=0
        for i in range(len(nums)):
            if nums[i]!='_':
                nums[i], nums[j] = nums[j], nums[i]
                count+=1
                j+=1
        return count,nums


print(Solution().replace([3,2,2,3], 3))