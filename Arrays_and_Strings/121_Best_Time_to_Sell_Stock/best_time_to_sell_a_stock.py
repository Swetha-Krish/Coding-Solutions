class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_profit = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_profit:
                min_profit = prices[i]

            profit = prices[i] - min_profit

            if profit > max_profit: 
                max_profit = profit
        
        return max_profit

# Time complexity: O(n)
# Space Complexity: O(1)