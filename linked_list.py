"""
    双链表
"""


class Link(object):
    def __init__(self, key, prev=None, next1=None):
        self._key = key
        self._prev = prev
        self._next1 = next1

    @property
    def key(self):
        return self._key

    @property
    def prev(self):
        return self._prev

    @property
    def next1(self):
        return self._next1

    @key.setter
    def key(self, key):
        self._key = key

    @prev.setter
    def prev(self, other):
        self._prev = other

    @next1.setter
    def next1(self, other):
        self._next1 = other

    # def __repr__(self):
    #     return str('key=%d, prev=%s, next1=%s' % (self._key, self._prev, self._next1))


class LinkedList(object):
    def __init__(self):
        self._head = None

    def insert(self, x):
        x.next1 = self._head
        if self._head != None:
            self._head.prev = x
        self._head = x
        x.prev = None

    def delete(self, x):
        if x.prev != None:
            x.prev.next1 = x.next1
        else:
            self._head = x.next1
        if x.next1 != None:
            x.next1.prev = x.prev

    def search(self, k):
        i = self._head
        while i != None:
            if i.key != k:
                i = i.next1
        return i

    def __str__(self):
        i = self._head
        a = []
        while i != None:
            a += [i.prev, i, i.next1, '█████████']
            i = i.next1
        return str(a)

L = LinkedList()
L.insert(Link(5))
L.insert(Link(6))
L.insert(Link(8))
print(L)
print(L.search(8))