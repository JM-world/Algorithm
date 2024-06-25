class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();

        for (String op : operations) {
            if (op.equals("+")) {
                // 현재 스택에서 두 개의 값이 존재해야 합니다.
                int top = stack.pop();
                int newTop = top + stack.peek();
                stack.push(top); // pop한 값을 다시 스택에 추가
                stack.push(newTop); // 계산된 새로운 값을 스택에 추가
            } else if (op.equals("D")) {
                // 현재 스택에서 최소한 하나의 값이 존재해야 합니다.
                stack.push(2 * stack.peek()); // 두 배 값을 스택에 추가
            } else if (op.equals("C")) {
                // 스택에서 가장 최근의 값을 제거
                stack.pop();
            } else {
                // 정수를 스택에 추가
                stack.push(Integer.valueOf(op));
            }
        }

        // 스택에 남아 있는 모든 점수의 합을 계산
        int sum = 0;
        for (int score : stack) {
            sum += score;
        }

        return sum; // 최종 합계 반환
    }
}