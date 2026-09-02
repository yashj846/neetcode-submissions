class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq_dict = {}
        window_size = len(s1)
        if len(s1) > len(s2):
            return False
        for i in s1:
            s1_freq_dict[i] = 1 + s1_freq_dict.get(i, 0)

        s2_freq_dict = {}
        for i in range(window_size):
            s2_freq_dict[s2[i]] = 1 + s2_freq_dict.get(s2[i], 0)

        print(s2_freq_dict)
        if s1_freq_dict == s2_freq_dict:
            return True
        else:
            l = 0
            r = l + window_size
            while r < len(s2):
                print(l,r)
                if s2[l] in s2_freq_dict and s2_freq_dict[s2[l]] == 1:
                    s2_freq_dict.pop(s2[l])
                else:
                     s2_freq_dict[s2[l]] -= 1
                s2_freq_dict[s2[r]] = 1 + s2_freq_dict.get(s2[r], 0)
                if s1_freq_dict == s2_freq_dict:
                    return True
                else:
                    l += 1
                    r += 1
        return False


        
        # l,r = 0, window_size-1
        # s2_freq_dict = {}
        # while r < len(s2):
        #     for i in range(window_size):
        #         s2_freq_dict[s2[l+i]] = 1 + s2_freq_dict.get(s2[l+i], 0)
        #     print(s2_freq_dict)

        #     if s2_freq_dict == s1_freq_dict:
        #         return True
        #     else:
        #         l +=1
        #         r +=1
        #         s2_freq_dict = {}
        # return False





        