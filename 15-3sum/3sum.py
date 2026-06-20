class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #bruate force method hai
        '''n = len(nums)
        my_set = set()
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        my_set.add(tuple(temp))
        return [list(ans) for ans in my_set]'''



        n = len(nums)
        result = set()
        for i in range(0,n):
            my_set = set()
            for j in range(i+1,n):
                third = - (nums[i]+nums[j])
                if third in my_set:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[j])
        return [list(ans) for ans in result]


        

        