class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # j = 0
        # max_length = 0
        # string_index = {}


        # while j < len(s):
        #     if s[j] not in string_index:
        #         string_index[s[j]] = j
        #         max_length = max(max_length, len(string_index))
        #         j +=1
        #     else:
        #         j = string_index[s[j]] + 1
        #         string_index = {}
        # return(max_length)

        l = 0
        r = 0
        distinct_letters = set()
        max_length = 0
        while r < len(s) and l <= r:
            if s[r] not in distinct_letters:
                distinct_letters.add(s[r])
                max_length = max(max_length, r-l+1)
                r+=1
            else:
                distinct_letters.remove(s[l])
                l += 1
        return(max_length)


            









        