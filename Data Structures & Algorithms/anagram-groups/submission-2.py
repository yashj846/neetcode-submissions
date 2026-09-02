class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        my_ans = []
        for i in strs:
            identifier = [0] * 26
            for j in i:
                identifier[ord(j) - 97] += 1
            if tuple(identifier) in anagram_dict:
                anagram_dict[tuple(identifier)].append(i)
            else:
                anagram_dict[tuple(identifier)] = [i]

        for i in anagram_dict:
            my_ans.append(anagram_dict[i])
        return(my_ans)


                

        




                    





        