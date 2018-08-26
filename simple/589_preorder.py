class Node(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """

        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        result = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.children:
                curr.children.reverse()
                stack += curr.children
        return result


def main():
    solution = Solution()
    node = Node(1, children=[Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    ret = solution.preorder(node)
    print(ret)


if __name__ == '__main__':
    main()
