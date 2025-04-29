# My Solution
class Solution(object):
    def mergeAlternately(self, word1, word2):
        rs = ''
        minimum = min(len(word1), len(word2))
        for i in range(minimum):
            rs += word1[i]+word2[i]
        rs += (max(word1[minimum:], word2[minimum:]))
        return rs

# Alternate Solution
class Solution(object):
    def mergeAlternately(self, word1, word2):
        rs = ''
        maximum = max(len(word1), len(word2))
        for i in range(maximum):
            if i < len(word1):
                rs += word1[i]
            if i < len(word2):
                rs += word2[i]
        return rs