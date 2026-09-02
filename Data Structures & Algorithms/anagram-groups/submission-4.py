class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        ans = {}


        for st in strs:
            alphabet_frequency = [0] * 26 #constant space
            # print(alphabet_frequency)
            for i in st:
                alphabet_frequency[ord(i)-97] += 1
            if tuple(alphabet_frequency) in ans:
                ans[tuple(alphabet_frequency)].append(st)
            else:
                ans[tuple(alphabet_frequency)] = [st]
        final_ans = []

        for k,v in ans.items():
            final_ans.append(v)
        return final_ans
















        