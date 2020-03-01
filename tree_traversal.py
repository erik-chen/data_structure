"""
    主题：树的广度优先遍历和深度优先遍历
    作者：陈志豪
    日期：2019、8、18
"""
class Queue(object):

    def __init__(self):
        self._numbers = [0 for x in range(100)]
        self._head = 0
        self._tail = 0

    @property
    def numbers(self):
        return self._numbers

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def stack_empty(self):
        if self._head == self._tail:
            return True
        else:
            return False

    def enqueue(self, x):
        if self._head - self._tail == 1 or self._head == 0 and self._tail == 99:
            print('error: overflow')
        else:
            self._numbers[self._tail] = x
            if self._tail == 99:
                self._tail = 0
            else:
                self._tail += 1

    def dequeue(self):
        if self.stack_empty():
            print('error: underflow')
            return
        else:
            x = self._numbers[self._head]
            if self._head == 99:
                self._head = 0
            else:
                self._head += 1
        return x

    def __str__(self):
        if self._head <= self._tail:
            queue_str = str(self._numbers[self._head:self._tail])
        else:
            queue_str = str(self._numbers[self._head:100]+self._numbers[0:self._tail])
        return queue_str


#  level order traversal
def BFS(tree, queue):
    if queue.numbers[queue.head:queue.tail]:
        i = queue.numbers[queue.head]
        print(tree[i])
        if 2*i <= len(tree)-1:
            queue.enqueue(2*i)
        if 2 * i + 1 <= len(tree) - 1:
            queue.enqueue(2*i+1)
        queue.dequeue()
        BFS(tree, queue)


#  pre, post, in order traversal [rooted ordered binary tree]
def DFS(tree, i):
    """
        infix, postfix, prefix只需要调整print语句的顺序就好
    """
    if 2*i <= len(tree)-1:
        DFS(tree, 2*i)
    if 2*i+1 <= len(tree)-1:
        DFS(tree, 2*i+1)
    print(tree[i])


def main():
    tree = ['NIL']
    ord_value = 65
    while ord_value <= 90:
        tree.append(chr(ord_value))
        ord_value += 1
    print(tree)
    queue = Queue()
    queue.enqueue(1)
    # BFS(tree, queue)
    DFS(tree, 1)


if __name__ == '__main__':
    main()