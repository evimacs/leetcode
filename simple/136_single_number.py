class Solution(object):
    def singleNumber(self, nums):
        """

        :type nums: List[int]
        :rtype: int
        """
        target_dict = dict()

        for x in nums:
            if x in target_dict:
                target_dict[x] += 1
            else:
                target_dict[x] = 0

        for x in target_dict:
            if target_dict[x] == 1:
                return x


def main():
    solution = Solution()
    ret = solution.singleNumber([4, 1, 2, 1, 2])


if __name__ == '__main__':
    main()
