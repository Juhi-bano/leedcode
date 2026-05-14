class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums =  sorted(nums)
        n = len(nums)-1
        expected_array = list(range(1,n+1))+[n]
        if nums == expected_array:
            return True
        return False

        