class Solution {
    public int[] countBits(int n) {
         int[] ans = new int[n + 1];  // 0부터 n까지의 결과를 저장할 배열

        for (int i = 1; i <= n; i++) {
            ans[i] = ans[i >> 1] + (i & 1);  // i/2의 결과에 i의 최하위 비트를 더함
        }

        return ans;
    }
}