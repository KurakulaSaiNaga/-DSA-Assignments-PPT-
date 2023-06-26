class Solution:
    def harmonious(self,arr):
        letter = {}
        ans = 0
        for i in arr:
            if i not in letter:
                letter[i] = 1
            else:
                letter[i] += 1
        for i in letter:
            if i + 1 in letter.keys():
                ans = max(ans, letter[i] + letter[i + 1])
        return ans

print(Solution().harmonious([1,3,2,2,5,2,3,7]))