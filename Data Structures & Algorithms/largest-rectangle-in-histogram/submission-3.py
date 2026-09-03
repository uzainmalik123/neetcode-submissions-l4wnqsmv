class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        startIndex = 0
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            startIndex = i

            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                startIndex = index
            
            stack.append((startIndex, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
