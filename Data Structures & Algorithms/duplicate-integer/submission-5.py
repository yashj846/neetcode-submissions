class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_values = set()
        for i in range(len(nums)):
            if nums[i] in set_values:
                return True
            else:
                set_values.add(nums[i])
        return False








         