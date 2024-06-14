class Solution {
    public int[] shuffle(int[] nums, int n) {
        
        int[] arr = new int[nums.length];
        int cnt = 0;
        int x = 0;
        
        for (int i = 0; i < nums.length; i ++) {
            if (cnt % 2 == 0) {
                arr[i] = nums[x];
            }
            else {
                arr[i] = nums[x + n];
                x++;
            }
            cnt++;
        }
        
        return arr;
    }
}