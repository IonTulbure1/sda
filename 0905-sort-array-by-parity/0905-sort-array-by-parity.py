
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pare = []
        impare = []

        for num in nums:
            if num % 2 == 0:
                pare.append(num)
            else:
                impare.append(num)

        return pare + impare
