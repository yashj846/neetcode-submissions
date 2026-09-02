class Solution:
    def maxArea(self, heights: List[int]) -> int:
            max_area = 0

            for i in range(len(heights)):
                start = i
                end = i + 1
                while end < len(heights):
                    area = (end - start) * min(heights[start], heights[end])
                    max_area = max(area, max_area)
                    end += 1
            return(max_area)


        
        