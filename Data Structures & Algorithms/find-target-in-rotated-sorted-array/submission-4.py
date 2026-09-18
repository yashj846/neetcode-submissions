class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:
            m = (l + r)//2

            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m 
        
        l, r= 0, len(nums) - 1
        # pivot = m

        if target == nums[m]:
            return m
        elif target < nums[m]:
            return -1
        elif target > nums[m]:
                if target <= nums[r]:
                    l = m + 1
                    r = len(nums) - 1
                else:
                    r = m - 1
                    l = 0

                while l <= r:
                    m2 = (l + r)//2

                    if target > nums[m2]:
                        l = m2 + 1
                    elif target < nums[m2]:
                        r = m2 - 1
                    elif target == nums[m2]:
                        return m2
        return -1





        while l <= r:
            if target == nums[pivot]:
                return pivot
            
            
            





        
        # print(nums[m])

            

            



        