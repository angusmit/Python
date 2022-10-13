#solution 1 highest value control
class Solution:
    def romanToInt(self, s: str) -> int:
        sym = ["I","V","X","L","C","D","M"]
        val = [1,5,10,50,100,500,1000]
        d = {sym[i]: val[i] for i in range(len(sym))}
        output = 0
        for i in range(len(s)-1,-1,-1):
            n = d[s[i]]
            if 3 * n < output:
                output = output - n
            else:
                output = output + n
        return output


#solution 2 left to right 
class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        d = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
        for i in range(len(s)):
            if i + 1 < len(s) and d[s[i]] < d[s[i+1]]:
                output -= d[s[i]]
            else:
                output +=d[s[i]]
        return output