class Solution {
    public int countPairs(List<Integer> nums, int target) {
         
        
        // nums를 오름차순으로 정렬한다.
        Collections.sort(nums);
        
        // start, end, cnt 선언
        int start = 0;
        int end = nums.size() - 1;
        int cnt = 0;
        
        // while문 선언 (start != end)
        while(start != end) {
            
            // 만약 두 값을 더한 값이 target보다 작으면,
            if (nums.get(start) + nums.get(end) < target) {
                
                cnt += end - start;
                start ++;
                
            } else {

                end--;
                
            }
        
        }
        
        return cnt;
    }
}