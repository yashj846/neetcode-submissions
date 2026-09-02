class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s)) + '#' +  s
        return encoded_str

    
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])
            start = j +1
            end = start + length
            res.append(s[start:end])
            i = end 
                        

        return res

s = Solution()
print(s.encode(['Hello', 'World']))



