class Solution {
    public int deleteGreatestValue(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int answer = 0;

        // 모든 행을 내림차순으로 정렬
        for (int[] row : grid) {
            Arrays.sort(row);
        }

        // 가장 큰 값을 삭제하고 그 중 최대값을 답에 더하는 작업 반복
        for (int col = n - 1; col >= 0; col--) {
            int maxVal = 0;
            for (int row = 0; row < m; row++) {
                maxVal = Math.max(maxVal, grid[row][col]);
            }
            answer += maxVal;
        }

        return answer;
    }
}