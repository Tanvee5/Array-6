# Problem 2 : Best Time to Buy and Sell Stock III
# Time Complexity : O(n) where n is the number of elements in the prices list
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None

# Your code here along with comments explaining your approach
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # get the length of the prices list
        length = len(prices)
        # define buy1 variable which will store the minimum price to make first buy
        buy1 = float('inf')
        # define buy2 which will store the effective minimum price for second buy adjusted with first profit
        buy2 = float('inf')
        # define profit1 which will store maximum profit which can made from first transaction
        profit1 = 0
        # define profit2 which will store total maximum profit that can be made from 2 transaction
        profit2 = 0
        # loop through prices list
        for i in range(length):
            # get the minimum between buy1 and value of prices at ith position as buy1
            buy1 = min(buy1, prices[i])
            # get the maximum between profit1 and difference between value of prices at ith position and buy1 as profit for first transaction
            profit1 = max(profit1, prices[i] - buy1)
            # get the minimum between buy2 and difference between value of prices at ith position and profit1 as effective buy price for second transaction
            buy2 = min(buy2, prices[i] - profit1)
            # get the maximum between profit2 and difference between value of prices at ith position and buy2 as total profit for 2 transaction
            profit2 = max(profit2, prices[i] - buy2)
        # return the total profit
        return profit2
