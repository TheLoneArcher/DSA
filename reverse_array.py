class Solution:
    def reverseArray(self, arr):
        size = len(arr)
        for i in range(size//2):
            arr[i], arr[size - 1 - i] = arr[size - 1 - i], arr[i]
        return arr
        
# Problems with the Initial Solution
# - Off by one error with the size (initially size - 1)
# - Another off by one error with the arr[size - i]