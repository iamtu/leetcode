class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        quotient = 0
        while True:
            dividend_abs = dividend_abs-divisor_abs
            if dividend_abs >= 0:
                quotient += 1
            else:
                break
        if (dividend > 0 and divisor > 0) or (dividend > 0 and divisor > 0):
            return quotient
        else:
            return -quotient

if __name__ == '__main__':
  s = Solution()
  dividend = -2147483648
  divisor = -1
  print (s.divide(dividend, divisor))