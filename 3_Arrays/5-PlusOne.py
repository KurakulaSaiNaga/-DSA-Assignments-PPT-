class Solution:
    def plusone(self,nums):
        r=1
        l=[]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==9:
                r=nums[i]+r
                n=r%10
                l.insert(0,n)
                r=r//10
            else:
                l.insert(0,nums[i]+r)
                r=0
        if r!=0:
            l.insert(0,r)
        return l
print(Solution().plusone([9]))
