# hash map with element and index
from typing import List


class Solution:
    def twoSums(self,nums:List[int], target:int)->List[int]:
        prevMap = {}  # create dictionary as hash map

        for i,n in enumerate(nums):  # what is enumerate
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] =i

        return


# check the solution

arr = [1,4,5,6,8,]
target = 10

twoSumOfArray = Solution()
result = twoSumOfArray.twoSums(arr,target)
print(result)

