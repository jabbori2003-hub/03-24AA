# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)

# cur = head
# while cur is not Node:
#     print(cur.data)
#     cur = cur.next

# print('None')

from collections import deque
q = deque [12,23,34]
q.append(40)
q.appendleft(3)
print(q)

q.pop()
q.popleft()
print(q)