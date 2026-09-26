class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        count_bucket =  [[] for _ in range(len(nums) + 1)]
        ans = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for key,v in freq.items():
            count_bucket[v].append(key)
        

        for i in range(len(count_bucket)-1, 0, -1):
            for j in count_bucket[i]:
                # print(j)
                ans.append(j)
                # print(len(ans))
                if len(ans) == k:
                    return ans        





        
        
        
            





        