class Solution {
    
    private static final int type = 0;
    private static final int color = 1;
    private static final int name = 2;
    
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int i = type;
        
        if (ruleKey.equals("color")) i = color;
        else if (ruleKey.equals("name")) i = name;

        int sum = 0;
        for (List<String> item : items) {
            if (ruleValue.equals(item.get(i))) sum++;
        }
        return sum;
    }
}