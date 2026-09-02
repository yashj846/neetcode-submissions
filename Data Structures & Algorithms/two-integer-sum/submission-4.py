class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if num_to_find in num_indices:
                return [num_indices[num_to_find], i]
            else:
                num_indices[nums[i]] = i
            




        

        