# Split Linked List in Parts https://leetcode.com/explore/item/3992


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for testing

def mklist(integer):
    string = str(integer)
    listnod = ListNode(int(string[0]))
    string = string[1:]
    while string:
        listnod = ListNode(int(string[0]), listnod)
        string = string[1:]
    return listnod

head = mklist(87654321)
k = 5

def geti(ln):
    i = 1
    t = head
    while t.next:
        i+= 1
        t = t.next
    return i

i = geti(head)
n = i // k
n_ = i % k
list = []

def nil(ln, x):
    if x == 0:
        return None
    return ListNode(ln.val, nil(ln.next, x-1))
#
# while head.next:
#     if n_> 0:
#         x = n + 1
#         n_ -= 1
#     else:
#         x = n
#     list.append(nil(head, x))
#     for e in range(x):
#         head = head.next

print(n_)
