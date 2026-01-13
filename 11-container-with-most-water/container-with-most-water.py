class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxarea=0
        while left < right:
            if height[left] < height[right]:
                area = (right-left)*height[left]
                left += 1
            elif height[left] > height[right]:
                area = (right-left)*height[right]
                right -= 1
            else:
                area = (right-left)*height[left]
                left += 1
                right -= 1
            if area > maxarea:
                maxarea = area
                area = 0
        return maxarea