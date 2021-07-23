class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = len(nums)
    expects = []
    cur_idx = 0
    while True:
      if cur_idx == N:
        break
      next_idx = cur_idx + 1
      while (next_idx < N):
        if nums[cur_idx] == nums[next_idx]:
          next_idx += 1
        else:
          break
      expects.append(nums[cur_idx])
      cur_idx = next_idx

    return len(expects)

if __name__ ==  '__main__':
  s = Solution()
  a = [0, 0 , 1 , 1, 2 , 3, 3, 3]
  print(s.removeDuplicates(a))
