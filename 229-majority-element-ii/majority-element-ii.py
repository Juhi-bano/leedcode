class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        appears = floor(n/3)
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num,0)+1
        for key in freq:
            if freq[key] > appears:
                result.append(key)
        return result


    

       