class Solution:
    def maximum69Number (self, num: int) -> int:
        nums=[]
        while num:
            n=num%10
            num//=10
            nums.insert(0,n)
        count=0
        res=0
        for i in nums:
            if i==6:
                if count<1:
                    res=res*10+9
                    count+=1
                else:
                    res=res*10+i
            else:
                res=res*10+i
        return res