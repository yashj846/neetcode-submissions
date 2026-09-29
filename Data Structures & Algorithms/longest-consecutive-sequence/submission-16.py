class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0
        for i in nums_set:
            if i - 1 not in nums_set:
                seq = 1 
                while i + 1 in nums_set:
                    i = i + 1
                    seq += 1
                max_seq = max(max_seq, seq)
        return max_seq





        

                    

        
        





    
        