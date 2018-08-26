class Solution(object):
    def subdomainVisits(self, cpdomains):
        """

        :type cpdomains: List[str]
        :rtype: List[str]
        """
        temp = dict()
        for cpdomain in cpdomains:
            a = cpdomain.split()
            b = a[1].split('.')
            for i in range(0, len(b)):
                _temp = '.'.join(b[i:])
                if _temp in temp:
                    temp[_temp] += int(a[0])
                else:
                    temp[_temp] = int(a[0])
        ret = list()
        for key, value in temp.items():
            ret.append('%s %s' % (value, key))
        return ret


def main():
    solution = Solution()
    ret = solution.subdomainVisits(
        ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com",
         "5 wiki.org"])
    print(ret)


if __name__ == '__main__':
    main()
