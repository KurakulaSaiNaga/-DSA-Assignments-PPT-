class Solution:
    def shortsl(self,nums,low,upp):
        l=[]
        for i in range(0,len(nums)-1):
            if i==0 and nums[i]>low and nums[i]-1!=low:
                l.append([low,nums[i]-1])
            if nums[i+1]-nums[i]!=1:
                l.append([nums[i]+1,nums[i+1]-1])
        if nums[len(nums)-1]!=upp:
            l.append([nums[len(nums)-1]+1,upp])
        return l
print(Solution().shortsl([3,4,5,50,75],0,99))
