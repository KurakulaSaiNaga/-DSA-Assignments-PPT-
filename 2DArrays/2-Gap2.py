class Solution:
    def gap(self,nums1,nums2):
        l=[]
        for i in range(len(nums1)-1):
            for j in range(i+1,len(nums1)):
                if abs(nums1[i]-nums1[j])==2 and nums1[i] not in nums2 and nums1[j] not in nums2:
                    l.append([nums1[i],nums1[j]])
        for i in range(len(nums2)-1):
            for j in range(i+1,len(nums2)):
                if abs(nums2[i]-nums2[j])==2 and nums2[i] not in nums1 and nums2[j] not in nums1:
                    l.append([nums2[i],nums2[j]])
        return l
print(Solution().gap([1,2,3],[2,4,6]))