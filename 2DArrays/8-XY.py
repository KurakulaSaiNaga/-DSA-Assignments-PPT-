class Solution:
    def xypoints(self,nums,n):
        if len(nums)==2:
            return nums
        l=[]
        a=n
        i=0
        while i!=n:
            l.append(nums[i])
            l.append(nums[a])
            i+=1
            a+=1
        return l
print(Solution().xypoints([1,2,3,4,5,6],3))

