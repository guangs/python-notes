# https://www.workat.tech/problem-solving/practice/flatten-multi-level-linked-list
# Medium
# ./resources/06-medium-flatten-linked-list.png

# https://www.youtube.com/watch?v=QWoX2-s8KLE

class ListNode:
    def __init__(self, data=0, next=None, down=None):
        self.data = data
        self.next = next
        self.down = down


column_1 = ListNode(1)
column_1.down = ListNode(3)
column_1.down.down = ListNode(8)

column_2 = ListNode(5)
column_2.down = ListNode(8)


column_3 = ListNode(8)
column_3.down = ListNode(14)
column_3.down.down = ListNode(26)

column_4 = ListNode(13)
column_4.down = ListNode(15)
column_4.down.down = ListNode(22)
column_4.down.down.down = ListNode(25)

column_1.next = column_2
column_2.next = column_3
column_3.next = column_4

root = column_1


# 这段代码是不是本题的solution，仅仅是一种遍历，有点类似深度遍历，以down指针为指向
def flatten_linked_list(root: ListNode) -> ListNode:
    stack = []
    current = root

    while current:
        if current.next:
            stack.append(current.next)
            current.next = None
        if current.down:
            current = current.down
        else:
            if stack:
                current.down = stack.pop()
                current = current.down
            else:
                return root


# 这段代码是本题的solution，使用了一个辅助函数insert_node来插入节点
# 这个函数的作用是将一个新节点插入到一个已排序的链表中
def flatten_linked_list_sorted(root: ListNode) -> ListNode:

    def insert_node(node: ListNode, new_node: ListNode):
        parent = node
        while node and node.data < new_node.data:
            parent = node
            node = node.next
        if not node:
            parent.next = new_node
        else:
            parent.next = new_node
            new_node.next = node
        

    current = root
    while current:
        down_node = current.down
        next_node = current.next

        if not down_node:
            current.down = next_node
            current.next = None
            current = next_node
            continue

        if not next_node:
            return root

        if down_node.data <= next_node.data:
            current.next = None
            current = down_node
            down_node.next = next_node
        else:
            current.down = next_node
            current.next = None
            current = next_node
            insert_node(current, down_node)

    return root



f = flatten_linked_list_sorted(root)
while f:
    print(f.data)
    f = f.down
