"""
Understand:
    input:array of ints [nums], int [k]
    return: int number of contigous(arrays in the array that have a product less than 10)
    constraints:
         1 <= nums.length <= 30,000
         1 <= nums[i] <= 1000
         0 <= k <= 1,000,000
    logic: given an array of nums and a k value
    we want to return all the sub arrays with products
    less than the k value.

    Match: 

"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Edge case: if k is 0 or 1, no product can be strictly less than k
        if k <= 1:
            return 0
        
        count = 0
        current_product = 1
        left = 0
        
        # Expand the window using the right pointer
        for right in range(len(nums)):
            current_product *= nums[right]
            
            # Shrink the window from the left if the product is too large
            while current_product >= k:
                current_product /= nums[left]
                left += 1
            
            # Number of valid subarrays ending at 'right'
            count += (right - left + 1)
            
        return count
        