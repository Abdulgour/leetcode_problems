class Solution:
    def maximum69Number (self, num: int) -> int:
        n=str(num)
        res=0
        c=0
        for i in n:
            if i=="6":
                if c<1:
                    res=res*10+9
                    c+=1
                else:
                    res=res*10+int(i)
            else:
                    res=res*10+int(i)
        return res