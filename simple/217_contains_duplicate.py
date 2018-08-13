class Solution(object):
    def containsDuplicate(self, nums):
        """

        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

def main():
    solution = Solution()
    ret = solution.containsDuplicate([1,2,3,1])
    print(ret)
    ret = solution.containsDuplicate([1,2,3,4])
    print(ret)
    ret = solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]
)
    print(ret)


if __name__ == '__main__':
    main()
