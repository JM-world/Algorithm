class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int sum = 0;
        if (ruleKey.equals("type")) {
            for (List<String> item : items) {
                if (ruleValue.equals(item.get(0))) sum++;
            }
        } else if (ruleKey.equals("color")) {
            for (List<String> item : items) {
                if (ruleValue.equals(item.get(1))) sum++;
            }
        } else {
            for (List<String> item : items) {
                if (ruleValue.equals(item.get(2))) sum++;
            }
        }
        return sum;
    }
}