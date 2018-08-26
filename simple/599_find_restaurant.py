class Solution(object):
    def findRestaurant(self, list1, list2):
        """

        :type list1: List[int]
        :type list2: int
        :rtype: List[str]
        """
        temp = set(list1) & set(list2)
        temp_dict = dict()
        for _temp in temp:
            sum_index = list1.index(_temp) + list2.index(_temp)
            temp_dict.setdefault(sum_index, []).append(_temp)
        return temp_dict[min(temp_dict.keys())]


def main():
    solution = Solution()
    ret = solution.findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"])
    print(ret)


if __name__ == '__main__':
    main()
