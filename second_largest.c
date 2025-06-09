int getSecondLargest(int *arr, int n) {
    int max = -1, sec = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] > max) {
            sec = max;
            max = arr[i];
        }
        else if (arr[i] < max && arr[i] > sec) sec = arr[i];
    }
    return sec;
}
// Edge Cases in Sample Outputs:
// - Duplicates not considered
// - If nothing no duplicates then return -1

// Problems in the Initial Solution
// - Didn't update the mm1 or second greatest number in the first if condition
