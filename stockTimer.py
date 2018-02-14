class Solution(object):
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


result = Solution()
print result.maxProfit([1, 6, 4, 5, 8, 3, 9])