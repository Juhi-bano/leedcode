class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #bruade force method hai
        '''n = len(nums)
        my_set = set()
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            temp = [nums[i],nums[j],nums[k],nums[l]]
                            temp.sort()
                            my_set.add(tuple(temp))
        return [list(ans) for ans in my_set]'''

        n = len(nums)
        result = set()
        nums.sort()
        if not nums or n < 4:
            return []
        for i in range(0,n):
            for j in range(i+1,n):
                start = j + 1
                end = n - 1
                while start < end:
                    Total = nums[i] + nums[j] + nums[start] + nums[end]
                    if Total == target:
                        temp = [nums[i],nums[j],nums[start],nums[end]]
                        result.add(tuple(temp))
                        start += 1
                        end -= 1
                    elif Total < target:
                        start += 1
                    elif Total > target:
                        end -= 1
        return [list(ans) for ans in result]
                


       


        


        
      