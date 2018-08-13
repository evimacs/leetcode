class Solution(object):
    def buddyString(self, A, B):
        """

        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return len(set(A)) != len(A)
        else:
            temp = list()
            for i in range(len(A)):
                if A[i] != B[i]:
                    temp.append([A[i], B[i]])
            if len(temp) != 2:
                return False
            return temp[0] == temp[1][::-1]


def main():
    solution = Solution()
    A = 'aaaaaaabc'
    B = 'aaaaaaacb'
    ret = solution.buddyString(A, B)
    print(ret)


if __name__ == '__main__':
    main()
