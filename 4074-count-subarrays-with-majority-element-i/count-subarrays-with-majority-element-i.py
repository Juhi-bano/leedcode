class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            target_count = 0
            for j in range(i,len(nums)):
                if nums[j] == target:
                    target_count += 1
                length = j - i + 1
                if target_count > length/2:
                    ans += 1
        return ans
