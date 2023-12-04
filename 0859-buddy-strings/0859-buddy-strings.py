class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        ls = list(s)
        gs = list(goal)
        count = 0
        c1 = ""
        c2 = ""
        if s != goal and len(s) == len(goal):
            for i in range(len(ls)):
                if ls[i] != gs[i]:
                    c1 += ls[i]
                    c2 += gs[i]
                    count += 1
            if count == 2 and c1[::-1] == c2:
                return True
            else:
                return False
        elif len(s) == 1:
            return False
        elif s.count(s[0]) == len(s) and goal.count(goal[0]) == len(goal) and s == goal:
            return True
        elif s == goal:
            if len(set(s)) == len(s):
                return False
            else:
                return True

        else:
            return False