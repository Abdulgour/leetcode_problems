class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        a = [[] for r in range(numRows)]
        i, r = 0, 1
        for c in s:
            if i==0:
                r=1
            elif i == numRows-1:
                r=-1
            a[i].append(c)
            i+=r
        return ''.join(''.join(row) for row in a)