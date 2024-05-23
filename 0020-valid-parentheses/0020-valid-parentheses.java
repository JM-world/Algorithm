import java.util.*;
class Solution {
    public boolean isValid(String s) {
        
        String[] sArr = s.chars().mapToObj(a -> String.valueOf((char) a)).toArray(String[] :: new);
        List<String> sList = new ArrayList<>();
        
        sList.add(sArr[0]);
        
        for (int i = 1; i < sArr.length; i++) {
            
            if (!sList.isEmpty()) {
                
                String last = sList.get(sList.size()-1);
                
                if ((last.equals("(") && sArr[i].equals(")")) ||
                    (last.equals("{") && sArr[i].equals("}")) ||
                    (last.equals("[") && sArr[i].equals("]"))) {
                    
                    sList.remove(sList.size()-1);
                    continue;
                    
                } else if (sArr[i].equals("(") ||
                           sArr[i].equals("{") ||
                           sArr[i].equals("[")) {
                    
                    sList.add(sArr[i]);
                    continue;
                    
                } else {
                    
                    return false;
                }
                
            } else {
                sList.add(sArr[i]);
            }
        }
        
        return sList.isEmpty() ? true : false;
        
    }
}

// ex) 반례 [[{}]{}]