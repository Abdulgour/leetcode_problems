class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count=0
        occur=[]
        res=0
        for i in nums:
            if i == 0:
                count+=1
            else:
                res+=(count*(count+1))//2
                count=0
        res+=(count*(count+1))//2
        return res