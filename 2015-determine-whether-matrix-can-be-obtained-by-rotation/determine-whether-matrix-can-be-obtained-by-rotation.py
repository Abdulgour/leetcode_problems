class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat==target:
            return True
        n=len(mat)
        item=3
        while item:
            item-=1
            for i in range(n):
                for j in range(n//2):
                    temp=mat[j][i]
                    mat[j][i]=mat[n-j-1][i]
                    mat[n-j-1][i]=temp
            for i in range(n):
                for j in range(i,n):
                    temp=mat[i][j]
                    mat[i][j]=mat[j][i]
                    mat[j][i]=temp
            if mat==target:
                return True
        return False