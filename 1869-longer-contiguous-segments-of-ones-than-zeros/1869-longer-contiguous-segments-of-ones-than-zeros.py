class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count1 = 0
        count0 = 0
        maximum1 = 0
        maximum0 = 0
        for ch in s:
            if ch == "1":
                count1 += 1
                maximum1 = max(maximum1, count1)
            else:
                count1 = 0

            if ch == "0":
                count0 += 1

                maximum0 = max(maximum0, count0)

            else:
                count0 = 0

        if maximum1 > maximum0:

            return True
        else:
            return False


           