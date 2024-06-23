class RecentCounter {

    private Queue<Integer> queue;

    // RecentCounter 생성자, 큐를 초기화합니다.
    public RecentCounter() {
        queue = new LinkedList<>();
    }
    
    // ping 메서드는 요청 시간 t를 받아서 처리합니다.
    public int ping(int t) {
        // 새로운 요청을 큐에 추가합니다.
        queue.offer(t);
        
        // 큐에서 3000 밀리초를 초과하는 오래된 요청을 제거합니다.
        while (!queue.isEmpty() && queue.peek() < t - 3000) {
            queue.poll();
        }
        
        // 큐에 남아 있는 요청의 수를 반환합니다.
        return queue.size();
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */