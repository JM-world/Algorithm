class Solution:
    import random
    from math import prod
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        while True:
            random.shuffle(nums)
            a = nums[:]
            if a not in result:
                result.append(a)

            if len(result) == prod([i for i in range(2, len(nums)+1)]):
                break
        return result