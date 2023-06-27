class Solution:
    def position(self, nums, target):
        if target < nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)
        else:
            low = 0
            high = len(nums) - 1
            while (low <= high):
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    low += 1
                if nums[mid] > target:
                    high -= 1
        if nums[low] < target:
            return low + 1
        return low


print(Solution().position([1, 3, 5, 6, 8, 10], 9))
