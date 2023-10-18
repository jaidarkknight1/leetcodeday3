class Solution:
    def romanToint(self,s:str) -> int:
        dict1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number=0
        for i in range (len(s)):
            char= s[i]
            roman = dict1[char]
            number - number +roman
        return number



