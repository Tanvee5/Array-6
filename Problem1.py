# Problem 1 : Best Time to Buy and Sell Stock
# Time Complexity : O(n) where n is the number of the prices list 
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None

# Your code here along with comments explaining your approach
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # define the length of the prices list
        length = len(prices)
        # define minValue and set to postive infinity which will store the minvalue of the prices list to buy the stock
        minValue = float('inf')
        # define profit which will store the profit
        profit = 0
        # loop through prices list
        for i in range(length):
            # get minimum value between minValue and value of prices list at ith position
            minValue = min(minValue, prices[i])
            # get the maximum profit as maximum value between the profit and difference value of prices list at ith position and minValue
            profit = max(profit, prices[i] - minValue)
        # return profit
        return profit
