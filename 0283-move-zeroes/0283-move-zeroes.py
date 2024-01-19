class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            while True:
                if nums[nums.index(0) + 1:].count(0) == len(nums[nums.index(0) + 1:]):
                    break
                else:
                    nums.remove(0)
                    nums.append(0)
