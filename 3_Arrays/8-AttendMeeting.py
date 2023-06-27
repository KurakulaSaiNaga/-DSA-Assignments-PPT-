class Solution:
    def meeting(self,nums):
        k=0
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i][1]<=nums[i+1][0]:
                k+=1
        return k==(len(nums)-1)
print(Solution().meeting( [[0,20],[5,10],[20,30]] ))