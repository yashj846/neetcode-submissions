class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        left_wall, right_wall = height[l], height[r]
        water_stored = 0


        while l < r:
            if left_wall <= right_wall:
                water_stored += max(0, (left_wall - height[l]))
                l += 1
                left_wall = max(left_wall, height[l])
            else:
                water_stored += max(0, (right_wall - height[r]))
                r -= 1
                right_wall = max(right_wall, height[r])

        return water_stored



            




            
        