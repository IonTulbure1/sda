
class Solution:
    def numberOfSteps(self, num: int) -> int:
        pasi = 0

        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1

            pasi = pasi + 1

        return pasi
