class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        result = []
        appear = (n/3)
        for num in nums:
            freq[num] = freq.get(num,0)+1
        for key in freq:
            if freq[key] > appear:
                result.append(key)
        return result

        