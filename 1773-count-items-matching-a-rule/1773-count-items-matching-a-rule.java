class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int i = 0;
        int sum = 0;
        switch (ruleKey) {
            case "color" -> i = 1;
            case "name" -> i = 2;
        }
        
        for (List<String> item : items) {
            if (ruleValue.equals(item.get(i))) sum++;
        }
        
        return sum;
    }
}