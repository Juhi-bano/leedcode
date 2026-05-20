class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        smallest = 1
        for num in nums:
            if num == smallest:
                smallest += 1
        return smallest