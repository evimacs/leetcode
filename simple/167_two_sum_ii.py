class Solution(object):
    def twoSum(self, numbers, target):
        """

        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        target_dict = dict()

        for x, y in enumerate(numbers, 1):
            _target = target - y
            if _target not in target_dict:
                target_dict[y] = x
            else:
                return [target_dict.get(_target), x]


def main():
    solution = Solution()
    ret = solution.twoSum([2, 7, 11, 15], 9)
    print(ret)


if __name__ == '__main__':
    main()
