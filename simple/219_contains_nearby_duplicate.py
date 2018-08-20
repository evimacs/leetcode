class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """

        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_map = dict()
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                num_map.setdefault(nums[i], []).append(i)
        for key, values in num_map.items():
            values = list(values)
            values.sort()
            if values[0] + key <= values[-1]:
                return True
        return False




def main():
    solution = Solution()
    ret = solution.containsNearbyDuplicate([99, 99], 2)
    print(ret)


if __name__ == '__main__':
    main()
