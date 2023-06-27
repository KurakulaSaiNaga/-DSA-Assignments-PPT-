class Solution:
    def closest(self,nums,target):
        nums.sort()  # Sort the array in ascending order
        n = len(nums)
        closest_sum = float('inf')  # Initialize the closest sum to a large value

        for i in range(n - 2):
            low = i + 1
            high = n - 1

            while low < high:
                current_sum = nums[i] + nums[low] + nums[high]

                if current_sum == target:
                    return current_sum

                # Update closest_sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    low += 1
                else:
                    high -= 1
        return closest_sum

print(Solution().closest([1,1,1,0],100))
