class Solution:
    def arrayPairSum(self, arr):
        arr.sort()
        k=0
        for i in range(0,len(arr),2):
             k+=min(arr[i],arr[i+1])
        return k
print(Solution().arrayPairSum([1,4,3,2]))