class Solution {
    public int maxProduct(int[] nums) {
        
        // 만약 배열의 길이가 2라면 각 값을 곱한 수를 반환한다.
        if (nums.length == 2) return (nums[0] - 1) * (nums[1] - 1);
        
        // 우선순위 큐를 최대 힙으로 생성한다.
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        // 배열을 순회하면서 큐에 add한다.
        for (int i : nums) {
            pq.add(i);
        }
        
        // 큐에서 최대 힙을 차례대로 max1, max2에 할당하고 제거한다.
        int max1 = pq.poll();
        int max2 = pq.poll();
        
        // 식에 맞게 계산하여 반환한다.
        return (max1 - 1) * (max2 - 1);
        
    }
}