class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s=set()
        n=len(nums)
        for i in range(n):
            if nums[i]<=0:
                continue
            elif nums[i] not in s:
                s.add(nums[i])
        if sum(s)>0:
            return sum(s)
        else:
            return max(nums)