class Solution(object):
    def containsDuplicate(self, nums):
        """

        :type nums: List[int]
        :rtype: bool
        """
        temp_dict = {}
        for x in nums:
            if x in temp_dict:
                _temp = temp_dict[x]
                _temp += 1
                if _temp >= 2:
                    return True
                temp_dict[x] = _temp
            else:
                temp_dict[x] = 1
        return False

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
