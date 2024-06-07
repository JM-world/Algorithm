class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();

        // 첫 번째 줄은 무조건 1
        if (numRows >= 1) {
            List<Integer> firstRow = new ArrayList<>();
            firstRow.add(1);
            triangle.add(firstRow);
        }

        for (int i = 1; i < numRows; i++) {
            List<Integer> prevRow = triangle.get(i - 1);
            List<Integer> row = new ArrayList<>();

            // 각 행의 첫 번째 숫자는 1
            row.add(1);

            // 중간 숫자들 계산
            for (int j = 1; j < i; j++) {
                row.add(prevRow.get(j - 1) + prevRow.get(j));
            }

            // 각 행의 마지막 숫자는 1
            row.add(1);

            triangle.add(row);
        }

        return triangle;
    }
}