
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def heapify(n, i):
            mare = i
            stanga = 2 * i + 1
            dreapta = 2 * i + 2

            if stanga < n and nums[stanga] > nums[mare]:
                mare = stanga

            if dreapta < n and nums[dreapta] > nums[mare]:
                mare = dreapta

            if mare != i:
                nums[i], nums[mare] = nums[mare], nums[i]
                heapify(n, mare)

        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)

        return nums
