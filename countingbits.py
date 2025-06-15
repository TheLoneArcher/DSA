class Solution(object):
    def countBits(self, n):
        return [int(str(bin(x)).count(1)) for x in range(n + 2)]
