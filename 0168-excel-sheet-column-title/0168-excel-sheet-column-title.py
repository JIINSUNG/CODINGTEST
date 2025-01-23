class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self.answer = ""

        def convert(n : int):
            if n > 26:
                if n % 26 == 0:
                    convert(n//26 -1)
                else:
                    convert(n // 26)

            self.answer += alphabet[n%26-1]

        convert(columnNumber)
        return self.answer




