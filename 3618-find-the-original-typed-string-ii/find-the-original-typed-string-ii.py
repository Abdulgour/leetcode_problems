class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod=10**9+7
        c=1
        l=[]
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                c+=1
            else:
                l.append(c)
                c=1
        l.append(c)
        totalpossiblestring=1
        for n in l:
            totalpossiblestring=(totalpossiblestring*n) % mod
        if k<=len(l):
            return totalpossiblestring
        elif k==len(word):
            return 1
        dp=[0]*k
        dp[0]=1
        for n in l:
            dummy=[0]*k
            num=0
            for j in range(k):
                if j>0:
                    num=(num+dp[j-1]) % mod
                if j>n:
                    num=(num-dp[j-n-1]) % mod
                dummy[j]=num
            dp=dummy
        notpossible=sum(dp[len(l):k])
        possibleString=(totalpossiblestring-notpossible)%mod
        return possibleString