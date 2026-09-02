class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num_to_check = target - nums[i]
            if num_to_check in hashmap:
                return [hashmap[num_to_check], i]
            else:
                hashmap[nums[i]] = i


        
         