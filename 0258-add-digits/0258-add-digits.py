class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            _num = 0
            for i in str(num):
                _num += int(i)

            if _num < 10:
                return _num
            else:
                num = _num         