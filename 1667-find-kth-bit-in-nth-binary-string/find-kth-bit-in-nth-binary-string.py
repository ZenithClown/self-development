class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.makestring(n, k)[k - 1]

    def makestring(self, n : int, stop : int) -> str:
        string = "0"

        for _ in range(n - 1):
            if len(string) >= stop:
                break
            string += "1" + string.replace("1", "2").replace("0", "1").replace("2", "0")[::-1]

        return string