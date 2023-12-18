class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a = max(nums)
        nums.pop(nums.index(max(nums)))
        b = max(nums)
        c = min(nums)
        nums.pop(nums.index(min(nums)))
        d = min(nums)
        return (a * b) - (c * d)