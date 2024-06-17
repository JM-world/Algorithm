class Solution {
    
    private static final int TYPE = 0;
    private static final int COLOR = 1;
    private static final int NAME = 2;
    
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int i = TYPE;
        
        if (ruleKey.equals("color")) i = COLOR;
        else if (ruleKey.equals("name")) i = NAME;

        int sum = 0;
        for (List<String> item : items) {
            if (ruleValue.equals(item.get(i))) sum++;
        }
        return sum;
    }
}