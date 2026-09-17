class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            m = (l + r)//2
            res = min(res, nums[m])

            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m 
        return res
        

        


        # while nums[start] > nums[mid]:
        #     mid -= 1
        # while nums[end] < nums[mid]:
        #     mid += 1
        # print(nums[:mid+1])
        # return mid+1
        # print(nums[mid+1:])
        