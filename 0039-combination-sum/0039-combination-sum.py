class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def helper(remaining,path,start):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return 
            for i in range(start,len(candidates)):
                num = candidates[i]
                path.append(num)
                new_remaining = remaining - num
                helper(new_remaining,path,i)
                path.pop()
        helper(target, [], 0)
        return result


        