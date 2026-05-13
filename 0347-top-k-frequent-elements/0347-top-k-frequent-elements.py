class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        arr = []
        for key, value in freq.items():
            arr.append((value,key))
        arr.sort(reverse=True)
        result = []
        for i in range(k):
            result.append(arr[i][1])
        return result        