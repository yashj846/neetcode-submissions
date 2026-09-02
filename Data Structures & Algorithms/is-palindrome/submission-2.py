class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_replaced =(s.replace(" ", "")).lower()
        start = 0
        end = len(s_replaced)-1
        # print(start, end)

        while start < end:
            while start < end and not s_replaced[start].isalnum():
                start +=1
            while start < end and not s_replaced[end].isalnum():
                end -=1
            if s_replaced[start].lower() != s_replaced[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True

        