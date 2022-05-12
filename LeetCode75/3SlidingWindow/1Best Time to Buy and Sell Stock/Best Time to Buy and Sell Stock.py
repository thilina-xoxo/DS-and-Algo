from typing import List


class Solution:
    def maxProfit(self, prices:List[int]) -> int:
        l,r = 0,1
        maxP =0

        while r <  len(prices):  # we can not use l < len(prices) -1 ; l depend on value of r
            if ( prices[l] < prices[r]):
                proffit = prices[r] - prices[l]
                maxP = max(proffit,maxP)
            else:
                l=r
            r+=1
        return maxP


# check
sol = Solution()

prices1 = [7,6,4,3,1]
prices2 = [7,1,5,3,6,4]

print(sol.maxProfit(prices1)) # ans = 0
print(sol.maxProfit(prices2)) # ans = 5