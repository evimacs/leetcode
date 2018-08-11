class Solution(object):
    def fizzBuzz(self, n, ):
        """

        :type n: int
        :rtype: List[str]
        """
        ret = list()

        for i in range(1, n + 1):
            if not i % 3:
                if not i % 5:
                    ret.append('FizzBuzz')
                else:
                    ret.append('Fizz')
            elif not i % 5:
                ret.append('Buzz')
            else:
                ret.append(str(i))
        return ret


def main():
    solution = Solution()
    ret = solution.fizzBuzz()
    print(ret)


if __name__ == '__main__':
    main()
