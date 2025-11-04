'''
偷懒版
nums = list(map(int,input().split()))
nums.sort()
print(*nums, sep=" ")
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

def merge(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dummy.next

def sortList(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sortList(head)
    right = sortList(mid)
    return merge(left,right)

nums = list(map(int,input().split()))
dummy = ListNode(0)
cur = dummy
for n in nums:
    cur.next = ListNode(n)
    cur = cur.next
head = dummy.next

head =sortList(head)

cur = head
res = []
while cur:
    res.append(str(cur.val))
    cur = cur.next

print(' '.join(res))