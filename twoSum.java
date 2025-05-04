class twoSum {
    public static int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (complement != -1) {
                for (int j = 0; j < nums.length; j++) {
                    if (i != j && nums[j] == complement) return new int[] {i, j};
                }
            }
        }
        return new int[0];
    }
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = twoSum(nums, target);
        System.out.println("Indices: " + result[0] + ", " + result[1]);
    }
}