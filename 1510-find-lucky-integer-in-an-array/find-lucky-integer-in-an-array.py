class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky=[]
        for num in arr:
            count=0
            for i in range(len(arr)):
                if num==arr[i]:
                    count+=1
            if count==num:
                lucky.append(count)
        if not lucky:
            return -1
        else:
            Max=max(lucky)
        return Max