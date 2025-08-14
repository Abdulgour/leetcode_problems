class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s=[]
        for i in range(1,len(num)-1):
            if num[i]==num[i-1] and num[i]==num[i+1]:
                s.append(num[i-1:i+2])
        
        if len(s)>1:
            s.sort()
            Max = s[len(s)-1]
        elif len(s)==1:
            Max = s[0]
        else:
            Max=''
        return Max