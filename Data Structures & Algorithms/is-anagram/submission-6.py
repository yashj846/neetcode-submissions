class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}
        for i in s:
            print(i)
            s_freq[i] = 1 + s_freq.get(i, 0)
        for j in t:
            t_freq[j] = 1 + t_freq.get(j, 0)
        
        if len(s_freq) != len(t_freq):
            return False
        else:
            for k,v in t_freq.items():
                if k not in s_freq:
                    return False
                if s_freq[k] != v:
                    return False
        return True

    

        
        