class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_sorted = list(sorted(set(nums)))
        # print(sorted(nums))
        start_ind = 0
        end_ind = 0
        expected_d = 0
        current_max_length = 1 if len(nums_sorted) > 0 else 0
        print(nums_sorted)

        while end_ind < len(nums_sorted):
            # print( end_ind, start_ind,expected_d)
            # print(nums_sorted[end_ind] - nums_sorted[start_ind])
            if nums_sorted[end_ind] - nums_sorted[start_ind] == expected_d:
                current_max_length = max(end_ind-start_ind + 1, current_max_length)
                end_ind += 1
                expected_d += 1
                # print('current max',current_max_length )
            else:
                # print('here')
                start_ind = end_ind
                expected_d = 0
            
        return(current_max_length)





        