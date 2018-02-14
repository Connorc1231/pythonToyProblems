class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i, char_group in enumerate(zip(*strs)):
            if len(set(char_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

result = Solution()
print result.longestCommonPrefix(['hello', 'heya', 'hellaa', 'heman'])
