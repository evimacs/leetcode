class Solution(object):
    def search(self, nums, target):
        """

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            index = (start + end) // 2
            if nums[index] == target:
                return index
            if nums[index] > target:
                end = index - 1
            else:
                start = index + 1
        return -1


def main():
    solution = Solution()
    ret = solution.search()
    print(ret)


if __name__ == '__main__':
    main()
