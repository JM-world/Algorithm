class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums2 = nums[:]
        while val in nums2:
            nums2.remove(val)
        for i in range(len(nums2)):
            nums[i] = nums2[i]
        return len(nums2)