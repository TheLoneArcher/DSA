#User function Template for python3

class Solution:
    def pushZerosToEnd(self, arr):
        size = len(arr)
        pos = 0
        for i in range(size):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
        while pos < size:
            arr[pos] = 0
            pos += 1
        return arr

if __name__ == "__main__":
    sol = Solution()
    arr = [0, 1, 0, 3, 12]
    print(sol.pushZerosToEnd(arr))  # Output: [1, 3, 12, 0, 0]
    	
# Problems with the Initial Solution
# - Possibility of swapping a zero with another zero, no checking
# - If zeroind is a zero itself then the operation performed will be redundant
# - Experimenting with pushing non-zero numbers to the front and overwriting the rest of the elements