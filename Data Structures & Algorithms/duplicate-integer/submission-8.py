class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        for k,v in freq.items():
            if v > 1:
                return True
        return False

        