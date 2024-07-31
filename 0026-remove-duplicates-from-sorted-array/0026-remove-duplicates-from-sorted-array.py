class Solution:
    def removeDuplicates(self, nums):
        result = 1
        length = len(nums)
        if length == 0:
            return 0
        temp = nums[0]
        for i in range(1, length):
            current = nums[i]
            if temp != current:
                nums[result] = current
                result += 1
                temp = current
        return result

# Example usage:
solution = Solution()

nums1 = []
k1 = solution.removeDuplicates(nums1)
print(f'Output: {k1}, nums = {nums1[:k1]}')
