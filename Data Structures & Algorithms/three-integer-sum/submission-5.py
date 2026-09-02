class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        ans = []
        for i in range(len(sorted_nums)):
            start = i +1
            end = len(sorted_nums) - 1
            while start < end:
                if sorted_nums[i] + sorted_nums[start] + sorted_nums[end] < 0:
                    start += 1
                elif sorted_nums[i] + sorted_nums[start] + sorted_nums[end] > 0:
                    end -= 1
                else:
                    if [sorted_nums[i], sorted_nums[start], sorted_nums[end]] not in ans:
                        ans.append([sorted_nums[i], sorted_nums[start], sorted_nums[end]])
                    start += 1
                    end -= 1
        return ans


        