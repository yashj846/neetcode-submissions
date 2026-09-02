class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        main_ans = []

        for i in strs:
            if "".join(sorted(i)) in anagram_dict:
                anagram_dict["".join(sorted(i))].append(i)
            else:
                anagram_dict["".join(sorted(i))] = [i]
        for k in anagram_dict:
            main_ans.append(anagram_dict[k])
        return main_ans





                    





        