class Solution:
    def search(self,nums,target):
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low+=1
            else:
                high-=1
        return -1
print(Solution().search([1,2,3,4,5,6],10))