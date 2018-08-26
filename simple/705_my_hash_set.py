class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = dict()

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set[key] = False

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        return self.set.get(key, False)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)