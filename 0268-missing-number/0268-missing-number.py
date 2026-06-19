class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        acxpected_sum = n*(n+1)//2
        actual_sum = sum(nums)
        return acxpected_sum - actual_sum
        