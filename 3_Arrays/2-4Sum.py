class Solution:
    def targetsum(self,nums,target):
        n = len(nums)
        s1 = set()
        l1 = []
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            s1.add(tuple(sorted((nums[i], nums[j], nums[k], nums[l]))))
        for i in s1:
            l1.append(list(i))
        return l1
print(Solution().targetsum([1,0,-1,0,-2,2],0))

