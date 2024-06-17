class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int sum = 0;
        for (int i=0; i < items.size(); i++) {
            if (ruleKey.equals("type") && ruleValue.equals(items.get(i).get(0))) sum++;
            if (ruleKey.equals("color") && ruleValue.equals(items.get(i).get(1))) sum++;
            if (ruleKey.equals("name") && ruleValue.equals(items.get(i).get(2))) sum++;
        }
        return sum;
    }
}