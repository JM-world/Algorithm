class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        
        int[] result = new int[k];
        int[] temp = new int[mat.length];
        int i = 0;
        for (int[] arr : mat) {
            int cnt = 0;
            for (int num : arr) {
                
                if (num == 1) cnt++;
            }
            temp[i] = cnt;
            i++;
        }
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int j=0; j<temp.length; j++) {
            map.put(j, temp[j]);
        }
        
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet());
        list.sort(Map.Entry.comparingByValue());
        
        for (int q=0; q<k; q++) {
            result[q] = list.get(q).getKey();
        }
        
        return result;
    }
}