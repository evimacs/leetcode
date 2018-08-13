class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """

        :type nums1: List[int]
        :type m: int
        :type nums2: list[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead
        """
        nums1[m::] = nums2[::]
        nums1.sort()
        print(nums1)


def main():
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    ret = solution.merge(nums1, m, nums2, n)
    print(ret)


if __name__ == '__main__':
    main()
