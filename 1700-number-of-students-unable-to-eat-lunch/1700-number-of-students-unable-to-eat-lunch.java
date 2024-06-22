class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Queue<Integer> q = new LinkedList<>();
        for (int s : students) q.offer(s);
        
        int i = 0;
        int unableCount = 0; // 먹지 못한 학생 수
        
        while (!q.isEmpty()) {
            int s = q.poll();
            
            if (s == sandwiches[i]) {
                i++;
                unableCount = 0; // 초기화
            } else {
                q.offer(s);
                unableCount++;
            }
            
            if (unableCount == q.size()) return q.size();
        }
        
        return 0;
    }
}