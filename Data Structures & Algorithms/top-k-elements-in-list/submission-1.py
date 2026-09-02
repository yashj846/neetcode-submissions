class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] in count_dict:
                count_dict[nums[i]] += 1
            else:
                count_dict[nums[i]] = 1

        sorted_data = (sorted(count_dict.items(), key=lambda item: item[1], reverse = True))
        # print(sorted_data)
        for i in range(k):
            # print(k)
            # print(sorted_data[i])
            ans.append(sorted_data[i][0])
        return(ans)





        