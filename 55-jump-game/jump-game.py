class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_length = 0
        for i in range(len(nums)):
            if i > max_length:
                return False
            else:
                max_length = max(max_length,i+nums[i])
        return True

        