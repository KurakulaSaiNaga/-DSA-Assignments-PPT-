class Solution:
    def twoSum(self, nums, target):
        l = []
        for i in range(len(nums)):
            t = target - nums[i]
            k = nums[i + 1:]
            if t in k:
                l.append(i)
                l.append(i + k.index(t) + 1)
                break
        return l


print(Solution().twoSum([2, 7, 11, 12, 15], 9))
