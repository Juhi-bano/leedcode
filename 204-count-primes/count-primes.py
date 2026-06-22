class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        Truth = [True]*n
        Truth[0] = Truth[1] = False
        for i in range(2,int(n**0.5)+1):
            if Truth[i]:
                for j in range(i*i,n,i):
                    Truth[j] = False
        return sum(Truth)



        