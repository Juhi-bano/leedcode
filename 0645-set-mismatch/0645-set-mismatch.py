class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_set = set()
        duplicate = -1
        for num in nums:
            if num in nums_set:
                duplicate = num
            nums_set.add(num)
        for i in range(1,len(nums)+1):
            if i not in nums_set:
                return [duplicate,i]
        