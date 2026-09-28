class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left

            if height[left] < height[right]:
                water_height = height[left]
            else:
                water_height = height[right]

            area = width * water_height

            if area > max_area:
                max_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
