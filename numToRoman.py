class Solution(object):
    def romanToInt(self, s):
        total = 0
        skipNext = False
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i, num in enumerate(s):
            try:
                if skipNext == True:
                    skipNext = False
                    continue
                elif i + 1 == len(s):
                    total += d[num]
                elif (d[s[i]] < d[s[i + 1]]):
                    skipNext = True
                    total += (d[s[i + 1]] - d[s[i]])
                else: 
                    total += d[num]
            except IndexError:
                continue
        return total
        
result = Solution()
result.romanToInt("MCMXCVI")

