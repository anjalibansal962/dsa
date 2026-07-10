class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # LESSGO SOLVED THIS IN FIRST GO
        # i need area
        # area = b * h
        # find base first
        # max possible base = n - 1
        # this is for h = min(nums[i = 0], nums[j = n-1])
        # max_area = b * h
        # if nums[i] < nums[j]:
            # h = min(nums[i++], nums[j])
        # else:
            # h = min(nums[i], nums[j++])
        # b -= 1

        n = len(heights)
        b = n - 1   # max_b initialized
        max_area = 0
        l = 0
        r = n - 1
        while l < r:
            left = heights[l]
            right = heights[r]
            h = min(left, right)
            if h == left:
                l += 1
            else:
                r -= 1
            area = h * b
            b -= 1
            if area > max_area:
                max_area = area
        
        return max_area
