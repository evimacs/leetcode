class Solution(object):
    def intersect(self, nums1, nums2):
        """

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = set(nums1) & set(nums2)
        ret_list = list()
        for x in ret:
            ret_list.extend([x] * min(nums1.count(x), nums2.count(x)))
        return ret_list


def main():
    solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    ret = solution.intersect(nums1, nums2)
    print(ret)

    nums1 = [4, 9, 5, 9, 4]
    nums2 = [9, 4, 9, 8, 4]
    ret = solution.intersect(nums1, nums2)
    print(ret)


if __name__ == '__main__':
    main()
