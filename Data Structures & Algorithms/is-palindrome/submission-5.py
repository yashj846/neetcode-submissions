class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_new = ''
        for i in s_lower:
            if i.isalnum():
                s_new += i
        print(s_new)
        i = 0
        j = len(s_new)-1
        while i < j:

            if s_new[i] == s_new[j]:
                i+=1
                j -=1
            if s_new[i] != s_new[j]:
                return False

        return True
                


        