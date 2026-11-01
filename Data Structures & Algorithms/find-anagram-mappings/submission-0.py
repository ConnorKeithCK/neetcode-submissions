class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        loc = {}
        res = []
        for index , num in enumerate(nums2):
            loc[num] = index

        for num in nums1:
            res.append(loc[num])

        return res