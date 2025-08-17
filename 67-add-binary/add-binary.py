class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=len(a)-1
        m=len(b)-1
        c=0
        s=''
        while m>=0 or n>=0 or c:
            total=c
            if n>=0:
                total+=int(a[n])
                n-=1
            if m>=0:
                total+=int(b[m])
                m-=1
            s=str(total%2)+s
            c=total//2
        return s