class Solution(object):
    def countPrimes(self, n):
        """

        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i] == 1:
                prime[i * i:n:i] = [0] * len(prime[i * i: n: i])
        return sum(prime)


def main():
    solution = Solution()
    ret = solution.countPrimes(10)
    print(ret)


if __name__ == '__main__':
    main()
