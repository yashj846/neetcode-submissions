class Solution:
    def isPalindrome(self, s: str) -> bool:


        i = 0
        j = len(s) -1

        while i < j:
            print(i,j, s[i], s[j])
            while (not s[i].isalnum() or s[i] == ' ') and i < j:
                i += 1
            while (not s[j].isalnum() or s[j] == ' ') and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
        return True
            
            
            




                


        