class Solution(object):
    def countAndSay(self, n):
        """

        :type n: int
        :rtype: str
        """
        res = ["1"]
        for i in range(n):
            num = res[i]
            temp = num[0] #当前的值
            count = 0 #计数
            ans = "" #第n+1个数字的结果
            for j in range(0,len(num)):
                if num[j] == temp:
                    count += 1
                else:
                    ans += str(count)
                    ans += str(temp)
                    temp = num[j]
                    count = 1
            ans += str(count)
            ans += str(temp)
            res.append(ans)
        return res[n-1]


def main():
    solution = Solution()
    ret = solution.countAndSay(4)
    print(ret)


if __name__ == '__main__':
    main()
