class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        changed = 0
        i = 0
        N = len(nums)
        if N == 0:
            return 0
        while True:
            if i == N-1:
                break
            if nums[i] == val:
                #found vi tri tu cuoi di len de thay the cho val
                idx = N-1
                while idx >= 0 and nums[idx] == val:
                    idx -= 1
                if idx > i: #tim thay
                    # change nums[i] cho nums[idx]
                    e = nums[idx]
                    nums[idx] = nums[i]
                    nums[i] = e
                else:
                    break
            i += 1
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    nums = [3, 3]
    val = 3
    print (s.removeElement(nums, val))
    print (nums, type(nums))