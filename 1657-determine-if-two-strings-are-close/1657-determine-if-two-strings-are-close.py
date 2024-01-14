class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        
        cnt_list = []
        for i in set(word2):
            cnt_list.append(word2.count(i))
        
        for k in set(word1):
            if word1.count(k) in cnt_list:
                cnt_list.remove(word1.count(k))
            else:
                return False
        return True