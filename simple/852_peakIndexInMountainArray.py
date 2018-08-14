class Solution(object):
    def peakIndexInMountainArray(self, A):
        """

        :type A: List[int]
        :rtype: int
        """
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = (start + end) // 2
            if A[mid] >= A[mid - 1] and A[mid] >= A[mid + 1]:
                return mid
            elif A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
                start = mid + 1
            elif A[mid] < A[mid - 1] and A[mid] > A[mid + 1]:
                end = mid - 1


def main():
    solution = Solution()
    ret = solution.peakIndexInMountainArray()
    print(ret)


if __name__ == '__main__':
    main()
