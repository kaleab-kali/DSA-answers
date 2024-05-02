class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         nums[:] = [element for element in nums if element!=val]
         k = len(nums)
         return k