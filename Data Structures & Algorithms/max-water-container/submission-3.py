class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most, l, r = 0, 0, len(heights) - 1

        while l < r:
            curr = (r - l) * min(heights[l], heights[r])
            most = max(curr, most)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return most