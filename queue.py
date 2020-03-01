"""
    queue FIFO
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


def main():
    S = Queue()
    for i in range(1, 101):
        S.enqueue(i)
        print(S)
    for i in range(1, 101):
        print(S.dequeue())


if __name__ == '__main__':
    main()