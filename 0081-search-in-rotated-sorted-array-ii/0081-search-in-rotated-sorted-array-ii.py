class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target not in nums:
            return False
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False
        