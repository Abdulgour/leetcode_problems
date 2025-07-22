class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        sum = 0
        start = 0
        l= []
        for i in range(len(nums)):
            while nums[i] in l:
                l.remove(nums[start])
                sum -= nums[start]
                start += 1
            sum += nums[i]
            l.append(nums[i])
            res = max(res, sum)
        return res