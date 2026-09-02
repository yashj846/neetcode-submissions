class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_num = set()
        for i in nums:
            if i in unique_num:
                return True
            else:
                unique_num.add(i)
        return False
         