class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        n=len(strs[0])
        k = 0
        for i in range(len(strs)):
            if strs[i]=='':
                return ''
            elif i>0:
                m=min(len(strs[0]),len(strs[i]))
                for j in range(m):
                    if strs[0][j]==strs[i][j]:
                        k += 1
                    else:
                        break    
                n=min(k,n)
                k=0
        return strs[0][:n]
