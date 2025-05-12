# Problem 4 : Best Time to Buy and Sell Stock with Cooldown
# Time Complexity : 
'''
Memoization - O(n) where n is the length of the prices
Top-Down - O(n) where n is the length of the prices
'''
# Space Complexity : 
'''
Memoization - O(n) where n is the length of the prices
Top-Down - O(n) where n is the length of the prices
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None

# Your code here along with comments explaining your approach
# Memoization Approach

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # define memo array to save the result for the ith transaction and specific buy/sell state
        self.memo = [[-1 for _ in range(2)] for _ in range(len(prices))]
        # call helper function with prices list, 0th index and flag for buy state set to 0 and return the value of profit
        return self.helper(prices, 0, 0)

    # helper function to calculate the profit for the ith day on the prices list with the flag (indiciating the buy/sell state)
    def helper(self, prices, i, flag):
        # base case if value of i is greater than or equal to prices length then return 0
        if i >= len(prices):
            return 0
        
        # another base case check if the value for ith day and flag in memo list is not equal to -1 then return that value
        if self.memo[i][flag] != -1:
            return self.memo[i][flag]
        
        # check the value of flag if it is 0 then it is buy state
        if flag == 0:
            # if it is buy state 
            # case1 - calculate the profit where stock is not buyed 
            case1 = self.helper(prices, i+1, flag)
            # case2 - calculate the profit where the stock at ith day is buyed and adjust the price for ith day by deducting
            case2 = -prices[i] + self.helper(prices, i+1, 1)
            # calculate the maximum value between case1 and case2
            ret = max(case1, case2)
            # save the ret value in memo at ith and 0th position
            self.memo[i][0] = ret
            # return the ret result
            return ret
        else:
            # else it is sell state
            # case3 - calculate the profit where stock is not selled 
            case3 = self.helper(prices, i+1, 1)
            # case4 - calculate the profit where the stock at ith day is selled and adjust the price for ith day by adding
            case4 = prices[i] + self.helper(prices, i+2, 0)
            # calculate the maximum value between case3 and case4
            ret = max(case3, case4)
            # save the ret value in memo at ith and 1th position
            self.memo[i][1] = ret
            # return the ret result
            return ret
        
# Top-Down Approach

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # get the length of the prices list
        length = len(prices)
        # if the length is less than or equal to 1 then return 0
        if length <= 1: 
            return 0
        
        # define dp matrix with 2 columns and length rows and set to 0
        dp =[[0] * 2 for _ in range(length)]
        # set the value of 0th row and 0th column of dp to -prices[0]
        dp[0][0] = -prices[0]
        # set the value of 1th row and 0th column of dp to maximum between -prices[0] and -prices[1]
        dp[1][0] = max(-prices[0], -prices[1])
        # set the value of 1th row and 1th column of dp to maximum between value of dp[0][1] and sum of dp[0][0] + value of prices list at 1st position
        dp[1][1] = max(dp[0][1], dp[0][0] + prices[1])
        # loop from 2 to the length of prices
        for i in range(2, length):
            # calculate the value of ith row and 0th column of dp as maximum between value of dp at (i-1)th row and 0th column and 
            # difference between the value of dp at (i-2)th row and 1th column and value of prices at ith position
            dp[i][0] = max(dp[i-1][0], dp[i-2][1] - prices[i])
            # calculate the value of ith row and 1th column of dp as maximum between value of dp at (i-1)th row and 1th column and 
            # sum of the value of dp at (i-1)th row and 0th column and value of prices at ith position
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        # return the value of dp at (length-1)th row and 1th column
        return dp[length - 1][1]
