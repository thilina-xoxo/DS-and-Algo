from typing import List


class Solution:
    def search(self, nums:List[int], target:int ) -> int:
        l,r = 0, len(nums)-1
         # there is another way of calculation mid value without overflowing

        while(l<=r):   # = is important for cases only one item in the list
            mid = (l + r) // 2
            if(nums[mid] > target):
                r = mid -1
            elif(nums[mid] < target):
                l = mid +1
            else:
                return mid

        return -1

sol = Solution()

nums1 = [-1,0,3,5,9,12]
nums2 = [-1,0,3,5,9,12]

print(sol.search(nums1,9))
print(sol.search(nums2,2))


