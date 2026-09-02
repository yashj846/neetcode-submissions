class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for i in nums_set:
            if i-1 not in nums_set:
                length = 1
                while i + 1 in nums_set:
                    length +=1
                    i +=1
                max_length = max(length, max_length)
        return max_length





        # nums_set = set(nums)
        # start_series = []
        # max_length = 0

        # for i in nums_set:
        #     if i - 1 not in nums:
        #         start_series.append(i)

        # for i in start_series:
        #     j = i
        #     length = 1
        #     while j+1 in nums_set and max_length <= length(nums_set)/2:
        #         j +=1
        #         length +=1
        #     max_length = max(length,max_length)
        # return(max_length)
                


        


        # for i in nums:


    
        