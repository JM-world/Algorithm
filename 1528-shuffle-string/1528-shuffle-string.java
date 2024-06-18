class Solution {
    public String restoreString(String s, int[] indices) {
        char[] arr = new char[indices.length];
        int n = 0;
        for (int i : indices) {
            arr[i] = s.charAt(n);
            n++;
        }
        
        return String.valueOf(arr);
    }
}