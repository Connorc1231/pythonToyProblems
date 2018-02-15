import bisect

class Solution(object):
    def maxEnvelopes(self, envelopes):
        # Get value of height sorted by width
        sortedSingles = [a[1] for a in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
        # Results array to store sorted, length to return 
        results, length = [0] * len(sortedSingles), 0
        # Loop through sorted widths
        for x in sortedSingles:
            # Get proper index for single and insert
            i = bisect.bisect_left(results, x, 0, length)
            results[i] = x
            # Length = i + 1
            if i == length:
                length += 1
        return length

result = Solution() 
print result.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])