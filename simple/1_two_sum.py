class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dict = dict()
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in temp_dict:
                return [i, temp_dict.get(temp)]
            else:
                temp_dict[nums[i]] = i
        return []


def main():
    solution = Solution()
    result = solution.twoSum([2, 15, 11, 7], 9)
    print(result)


if __name__ == '__main__':
    main()
