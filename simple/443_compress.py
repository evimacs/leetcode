class Solution(object):
    def compress(self, chars):
        """

        :type chars: List[str]
        :rtype: int
        """

        ret = list()
        temp = ''
        flag = 1
        for x in chars:
            if x != temp:
                ret.append(x)
                print(flag)
                if flag > 1:
                    ret.append(str(flag))
                flag = 1
                temp = x
            else:
                flag += 1

        for y, x in enumerate(ret):
            if len(x) > 1:
                for j, i in enumerate(x):
                    ret.insert(j, i)
        chars = ret[:len(chars):]
        print(chars)
        return len(chars)


def main():
    solution = Solution()
    ret = solution.compress(["a", "a", "b", "b", "c", "c", "c"])
    print(ret)


if __name__ == '__main__':
    main()

