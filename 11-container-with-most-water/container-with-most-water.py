class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxarea=0
        while left < right:
            area = (right-left)*min(height[left],height[right])
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
            if area > maxarea:
                maxarea = area
                area = 0
        return maxarea