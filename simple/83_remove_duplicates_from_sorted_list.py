class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """

        :type head: ListNode
        :rtype: ListNode
        """
        temp_list = list()
        p = head
        while True:
            if not p:
                break
            if p.val in temp_list:
                p.next = p.next.next
            else:
                temp_list.append(p.val)
            p = p.next
        return head


def main():
    solution = Solution()
    ret = solution.deleteDuplicates()
    print(ret)


if __name__ == '__main__':
    main()

