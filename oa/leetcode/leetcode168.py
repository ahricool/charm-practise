class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnNumber -= 1
        size = 26
        power = 1
        while True:
            if columnNumber >= size:
                columnNumber -= size
                size *= 26
                power += 1
            else:
                ans = ""
                while power != 0:
                    columnNumber, b = columnNumber // 26, columnNumber % 26
                    ans = chr(ord("A") + b) + ans
                    power -= 1
                return ans
