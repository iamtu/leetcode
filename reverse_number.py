import math
class Solution:
  def reverse(self, x):
    x_p = abs(x)
    digits = []
    while x_p > 0:
      d = x_p % 10
      digits.append(d)
      x_p = x_p / 10
    print ('removeme digits:', digits)
    r_x = 0
    N = len(digits)
    for i in range(N):
      r_x += digits[i] * math.pow(10, N-i-1) 
    if x < 0:
      return -r_x
    else:
      return r_x
if __name__ == '__main__':
  s = Solution()
  x = 123
  t = 321
  print (t, s.reverse(x))