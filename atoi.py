class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        char2digit = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        N = len(s)
        i = 0
        # remove whitespace
        while i < N:
            if s[i] == ' ':
                i += 1
            else:
                break
        s = s[i:]
        is_negative = False
        if s[0] == '-':
            is_negative = True
            s = s[1:]

        digits = []
        N = len(s)
        i = 0
        while i < N:
            if s[i] >= '0' and s[i] <= '9':
                digits.append(char2digit[s[i]])
                i += 1
            else:
                break
        
        if not digits:
            return 0
        else:
            num = 0
            M = len(digits)
            for i in range(M):
                num += digits[i] * 10**(M-1-i)
        if is_negative:
            num = -num
        if num < -2**31:
            return -2**31
        if num >= 2**31:
            return 2**31 -1 
        return num
if __name__ == '__main__':
    sl = Solution()
    s = "42"
    s = "   -42"
    s = "4193 with words"
    print (sl.myAtoi(s))