class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rl = []
        for i in nums1:
            if nums2[nums2.index(i)+1:] == []:
                rl.append(-1)
            else:
                if max(nums2[nums2.index(i)+1:]) > i:
                    for k in nums2[nums2.index(i)+1:]:
                        if i < k:
                            rl.append(k)
                            break
                else:
                    rl.append(-1)
        return rl