#User function Template for python3

class Solution:
    def reverseArr(self, arr, st, en):
        while st < en:
            arr[st], arr[en] = arr[en], arr[st]
            st += 1
            en -= 1
    def rotateArr(self, arr, d):
        size = len(arr) - 1
        d %= (size + 1) # Fix: Off by one due to zero indexing
        self.reverseArr(arr, 0, d - 1) # Fix: Off by one in the reverseArr function
        self.reverseArr(arr, d, size)
        self.reverseArr(arr, 0, size)
        return arr
# Issues with the Initial Solution:
# - Didn't sort the array in place, because I didn't use the [:] substring operator, 
#   I know it's not using any fancy logic but I thought it's cool so I'm saving it
#   I'll start another solution
# def rotateArr(self, arr, d):
#         newarr = arr[d:] + arr[:d]
#         arr[:] = newarr
# - I googled the solution and saw a neat one
#   Reversed until first d elements, 
#   then reversed from d to the end and reversed the entire thing