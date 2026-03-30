class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        maximumArea = 0

        while i < j:
            index = j - i
            currArea = min(heights[i], heights[j]) * index

            if currArea > maximumArea:
                maximumArea = currArea
                if heights[i] < heights[j]:
                    i += 1
                else:
                    j -= 1
            else:
                if heights[i] < heights[j]:
                    i += 1
                else:
                    j -= 1

        return maximumArea