"""
Understand:
    input: int array nums
    output: boolean True if any value appears in array more than once, False otherwise
    logic: go through given array, we want to see if the current val in the array, apprears more than once
    return true if any value appears more than once, return false otherwise
    edge cases: empty array: return False
Plan:
    define function
        for each num in array
            if the array contains another copy of that num
                return True
        return False
    """
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
        