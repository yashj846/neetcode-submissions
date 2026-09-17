class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        # res = -1

        while l <= r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            m = (r+l)//2
            if nums[m] == target:
                return m
            if target <=  nums[l]:
                l+=1
            else:
                r-=1
        return -1 

            



        