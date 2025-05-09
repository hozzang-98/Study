class Solution:
    
    def letterCombinations(self, digits: str) -> list[str]:

        from itertools import product
        
        if digits == "": return []

        dic = {}
        start = 0
        for i in range(2, 10):
            count = 4 if i in [7, 9] else 3
            dic[str(i)] = [chr(97 + start + j) for j in range(count)]
            start += count

        if len(digits) == 1: return dic[digits]

        answer = []
        length = len(digits)

        tmp = []
        for digit in digits:

            tmp.append(dic[digit])
        
        result = [''.join(chars) for chars in product(*tmp)]
        
        return result

