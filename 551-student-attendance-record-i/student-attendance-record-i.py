class Solution:
    def checkRecord(self, s: str) -> bool:
        A,L=0,0
        i=0
        n=len(s)
        for i in range(n):
            if s[i]=='A':
                A+=1
                if A>1:
                    return False
            elif s[i]=='L' and n-i>=3:
                if s[i+1]=='L':
                    if s[i+2]=='L':
                        return False
                    i+=1
                i+=1
            i+=1
        return True