class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        Maxpow=0
        Minpow=0
        maxs = int(''.join(sorted(str(n), reverse=True)))
        mins = int(''.join(sorted(str(n))))
        while maxs>1:
            maxs=maxs//2
            Maxpow+=1
        while mins>1:
            mins=mins//2
            Minpow+=1
        found = False
        for i in range(Minpow,Maxpow+1):
            if 2**i==n or sorted(str(2**i))==sorted(str(n)):
                found = True
                break
        return found