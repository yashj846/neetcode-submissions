class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums_sorted = sorted(nums)
        ans = []
        for i in range(0, len(nums_sorted)-2, 1):
            num_to_find = -nums_sorted[i]
            l,r = i + 1, len(nums_sorted)-1
            while l < r:
                if  nums_sorted[l] + nums_sorted[r] > num_to_find:
                    r -= 1
                elif nums_sorted[l] + nums_sorted[r] < num_to_find:
                     l += 1
                elif nums_sorted[l] + nums_sorted[r] == num_to_find:
                    if [nums_sorted[i],nums_sorted[l],nums_sorted[r]] not in ans:
                        ans.append([nums_sorted[i],nums_sorted[l],nums_sorted[r]])
                    l += 1
                    r -= 1
        return(ans)



        