class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped_anagrams, ans  = {}, []

        for i in range(len(strs)):
            anagram_group_key = tuple(sorted(strs[i]))
            if anagram_group_key in grouped_anagrams:
                grouped_anagrams[anagram_group_key].append(strs[i])
            else:
                grouped_anagrams[anagram_group_key] = [strs[i]]
        
        for k,v in grouped_anagrams.items():
            ans.append(v)

        return ans

        









        