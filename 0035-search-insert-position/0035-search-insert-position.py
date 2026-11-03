
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        stanga = 0
        dreapta = len(nums) - 1

        while stanga <= dreapta:
            mijloc = (stanga + dreapta) // 2

            if nums[mijloc] == target:
                return mijloc
            elif nums[mijloc] < target:
                stanga = mijloc + 1
            else:
                dreapta = mijloc - 1

        return stanga
