class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [len(temperatures) - 1]
        res = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            while stack:
                idx = stack.pop()
                if temperatures[idx] > temperatures[i]:
                    res[i] = idx - i
                    break
            stack.append(idx)
            stack.append(i)
                
        return res



        