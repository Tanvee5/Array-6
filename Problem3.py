# Problem 3 : Best Time to Buy and Sell Stock IV
# Time Complexity : O(n * k) where n is the number of elements in orices list and k  is the number k times transaction
# Space Complexity : O(k) where k  is the number k times transaction
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None

# Your code here along with comments explaining your approach
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # define buy array and set to infinity with size as k+1, which will store the minimum price to buy
        buy = [float('inf')] * (k+1)
        # define sell array and set to 0 with size as k+1, which will store total maximum profit that can be made
        sell = [0] * (k+1)
        # get the length of the prices list
        length = len(prices)

        # loop through the prices list
        for i in range(length):
            # loop from 1 to k+1 transactions
            for j in range(1, k+1):
                # set the value of buy at jth position as minimum between buy[j] and difference between prices[i] and sell[j-1]
                buy[j] = min(buy[j], prices[i] - sell[j-1])
                # set the value of sell at jth position as maximum between sell[j] and difference between prices[j] and buy[j]
                sell[j] = max(sell[j], prices[i] - buy[j])
        # return the value of sell at kth position which will give total profit for k transaction
        return sell[k]
