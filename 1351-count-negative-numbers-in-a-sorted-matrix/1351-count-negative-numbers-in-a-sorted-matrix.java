class Solution {
    public int countNegatives(int[][] grid) {
        return(int) Arrays.stream(grid)  // grid의 각 행(row)을 스트림으로 변환
            .flatMapToInt(row -> Arrays.stream(row))  // 각 행(row)을 다시 1차원 스트림으로 변환
            .filter(num -> num < 0)  // 음수인 요소만 필터링
            .count();  // 음수의 개수를 카운트
    }
}