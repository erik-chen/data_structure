"""
    stack LIFO
"""


class Stack(object):

    def __init__(self):
        self._numbers = [0 for x in range(100)]
        self._top = -1

    @property
    def top(self):
        return self._top

    def stack_empty(self):
        if self._top == -1:
            return True
        else:
            return False

    def push(self, x):
        if self._top <= 98:
            self._top += 1
            self._numbers[self._top] = x
        else:
            print('error: overflow')

    def pop(self):
        if self.stack_empty():
            print('error: underflow')
        else:
            x = self._numbers[self._top]
            self._top -= 1
            return x

    def __str__(self):
        return str(self._numbers[0:self._top+1])


def main():
    S = Stack()
    for i in range(1, 102):
        S.push(i)
        print(S)
    for i in range(1, 102):
        print(S.pop())


if __name__ == '__main__':
    main()