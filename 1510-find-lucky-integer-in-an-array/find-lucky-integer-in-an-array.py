class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=[]
        for i in range(len(arr)):
            found=False
            for j in range(len(freq)):
                if freq[j][0]==arr[i]:
                    freq[j][1]+=1
                    found=True
                    break
            if not found:
                freq.append([arr[i] ,1])
        max=-1
        for i in range(len(freq)):
            if freq[i][0]==freq[i][1]:
                if freq[i][0] > max:
                    max= freq[i][0]
        return max