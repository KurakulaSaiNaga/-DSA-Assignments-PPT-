class Solution:
    def flower(self, nums, n):
        count = 0
        print(nums)
        flowerbed=nums
        if n == 0:
            return True
        for i in range(0, len(flowerbed) - 1):
            if i==0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
            else:
                if flowerbed[i-1]!=1 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
        if flowerbed[len(flowerbed) - 2] == 0 and flowerbed[len(flowerbed) - 1] == 0:
            flowerbed[len(flowerbed) - 1]=1
            count += 1
        #print(count)
        #print(nums)
        print(flowerbed)
        print(count)
        if count >= n:
            return True
        return False
print(Solution().flower([1,0,1,0,0,1,0,0],1))