class Solution:
    def romanToInt(self, s: str) -> int:
        symbols =  {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        result = 0
        index = len(s) - 1
        while index > -1:
                        
            if (index > 0):
                word = s[index-1]+s[index]

                if word in symbols:
                    result += symbols[word]
                    index -= 2
                    continue
                else:       
                    result += symbols[s[index]]
                    index -= 1
            else: 
                result += symbols[s[index]]
                index -= 1


        return result