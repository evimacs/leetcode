class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """

        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_map = dict()
        for x in range(len(nums)):
            if nums[x] in nums_map:
                if x - nums_map[nums[x]] <= k:
                    return True
                else:
                    nums_map[nums[x]] = x
            else:
                nums_map[nums[x]] = x
        return False


def main():
    solution = Solution()
    ret = solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    print(ret)


if __name__ == '__main__':
    main()
