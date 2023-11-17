class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n_list = list(set(nums))
        n_list.sort()
        for i , k in enumerate(n_list):
            nums[i] = k
        return len(n_list)