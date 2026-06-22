class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        for key in freq:
            if freq[key] > 1:
                return key