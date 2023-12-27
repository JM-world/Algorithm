class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_list = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        temp_list = []
        result_list = []
        if digits != "":
            for i in digits:
                temp_list.append(num_list[int(i)])
        else:
            return []

        if len(digits) == 1:
            for i in temp_list[0]:
                result_list.append(i)
            print(result_list)
        elif len(digits) == 2:
            for i in temp_list[0]:
                for k in temp_list[1]:
                    result_list.append(i + k)
        elif len(digits) == 3:
            for i in temp_list[0]:
                for k in temp_list[1]:
                    for j in temp_list[2]:
                        result_list.append(i + k + j)
        else:
            for i in temp_list[0]:
                for k in temp_list[1]:
                    for j in temp_list[2]:
                        for u in temp_list[3]:
                            result_list.append(i + k + j + u)
        
        return result_list