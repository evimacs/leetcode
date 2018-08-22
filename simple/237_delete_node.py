class ListNode(object):
    def __init__(self, x, node=None):
        self.val = x
        self.next = node


class Solution(object):
    def deleteNode(self, node):
        """

        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node == None:
            return node

        if node.next == None:
            node = None

        node.val = node.next.val
        node.next = node.next.next


def main():
    solution = Solution()
    ret = solution.deleteNode([1, 2, 3, 1])
    print(ret)


if __name__ == '__main__':
    main()
