class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles_sorted = sorted(piles)
        # start = 0
        # end = len(piles_sorted) -1 
        min_rate  = max(piles)
        # rate_array = [x for x in range(1, max(piles) + 1)]
        # time_taken = len(piles)
        # print(rate_array)
        start = 1
        end = max(piles)
        while start <= end: 
            rate = (start + end) //2
            time_taken = 0
            for p in piles:
                if (p/rate) % 1 != 0:
                   time_taken += int(p/rate) + 1
                else:
                    time_taken += int(p/rate)
            if time_taken <= h:
                min_rate = min(rate, min_rate)
                end = rate - 1
            elif time_taken > h:
                start = rate + 1
        return(min_rate)  

        # import math
        # min_rate = max(piles)
        # for i in range(1, min_rate+1, 1):
        #     time_taken = 0
        #     for j in piles:
        #         time_taken += int(math.ceil(j/i))
        #     # print(i, time_taken)
        #     if time_taken <= h:
        #         # print(i, time_taken)
        #         min_rate = min(i, min_rate)
        #     # break
        # return(min_rate)                   

            


        