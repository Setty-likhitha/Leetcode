class Solution:
    def twoSum(self, nums, target):
        a = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in a:
                a[num] = i
            else:
                return [a[n], i]