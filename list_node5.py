class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


    def __repr__(self):
        node = self
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return '{}'.format(list)


class LinkedList(object):
    def __init__(self, *args):
        if not args:
            self.head = None
        else:
            self.head = _ = ListNode(args[0])
            for i in range(len(args[:-1])):
                _.next = ListNode(args[i+1])
                _ = _.next


# def rotateRight(head: ListNode, k: int) -> ListNode:
#     def get_length(head):
#         length = 0
#         _ = head
#         while _:
#             length += 1
#             _ = _.next
#         return length
#
#     length = get_length(head)
#     if not length or length == 1:
#         return head
#     k %= length
#     if not k:
#         return head
#     back_head = back_tail = head
#     for _ in range(length - k - 1):
#         back_tail = back_tail.next
#     head = back_tail.next
#     back_tail.next = None
#     front_tail = head
#     while front_tail.next:
#         front_tail = front_tail.next
#     front_tail.next = back_head
#     return head


def integerBreak(n: int) -> int:
    if n < 2:
        return 0
    if n < 6:
        return 2*(n-2)
    for i in range(2, n//2+1):
        print(i, (n//i)**(i-n%i)*(n//i+1)**(n % i))





# head = LinkedList(1, 2, 3, 4).head
print(integerBreak(14))