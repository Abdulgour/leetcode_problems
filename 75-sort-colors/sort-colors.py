class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j=0,1
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[i]>nums[j]:
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
                j+=1
            i+=1
        return nums