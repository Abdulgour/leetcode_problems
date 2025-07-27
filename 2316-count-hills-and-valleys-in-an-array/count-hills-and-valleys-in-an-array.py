class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n= len(nums)
        i=0
        while i < n-1:
            if nums[i]==nums[i+1]:
                nums.pop(i)
                n-=1
                i-=1
            i+=1
        count=0
        for i in range(1,n-1):
            if nums[i-1]< nums[i] >nums[i+1]:
                count+=1
            elif nums[i-1]> nums[i] <nums[i+1]:
                count+=1
        return count