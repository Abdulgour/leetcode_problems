class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c=0
        occur=[]
        for i in nums:
            if i == 0:
                c+=1
            else:
                occur.append(c)
                c=0
        occur.append(c)
        res=0
        for n in occur:
            res+=(n*(n+1))//2
        return res