class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = height[0]
        prefix_max_arr = [height[0]] * len(height)
        suffix_max = height[-1]
        suffix_max_arr = [height[-1]] * len(height)
        ans = [0] * len(height)

        for i in range(1, len(height)):
            prefix_max_arr[i] = prefix_max
            prefix_max = max(prefix_max, height[i])
        
        for i in range(len(height)-1, 0, -1):
            suffix_max_arr[i] = suffix_max
            suffix_max = max(suffix_max, height[i])
        
        for i in range(1, len(height)-1, 1):
            ans[i] = max(min(prefix_max_arr[i], suffix_max_arr[i]) - height[i],0)

        # print(ans)

        return sum(ans)            



            




            
        