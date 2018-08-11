class Solution(object):
    def majorityElement(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """

        index = len(nums) // 2
        return sorted(nums)[index]


def main():
    solution = Solution()
    ret = solution.majorityElement([3, 2, 3])
    print(ret)


if __name__ == '__main__':
    main()
