class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        ans = []
        for k in range(len(sorted_nums)-2):
            i = k + 1
            j = len(sorted_nums)-1
            while i < j :
                if sorted_nums[k] + sorted_nums[i] + sorted_nums[j] > 0:
                    j -=1
                elif sorted_nums[k] + sorted_nums[i] + sorted_nums[j] < 0:
                    i += 1
                else:
                    if [sorted_nums[i],sorted_nums[j],sorted_nums[k]] not in ans:
                        ans.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                    i+=1
                    j-=1
        return ans



        