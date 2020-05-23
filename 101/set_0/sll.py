class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.dummy_head = None

    def create_ll(self):
        self.dummy_head = Node(0)

    def get_root(self):
        return self.dummy_head.next

    def add_node(self, val):
        head = self.get_root()
        if not head:
            self.dummy_head.next = Node(val)
        else:
            while head and head.next:
                head = head.next
            head.next = Node(val)

    def traverse_ll(self):
        head = self.get_root()
        while head:
            print(head.data, end=" ")
            head = head.next

    def reverse(self):
        head = self.get_root()
        left = None
        while head:
            right = head.next
            head.next = left
            left = head
            head = right
        self.dummy_head.next = left

    def copy_list(self, root, node):
        pass

 


ll = LinkedList()
ll.create_ll()
ll.add_node(11)
ll.add_node(22)
ll.add_node(33)
ll.add_node(44)
ll.add_node(55)
ll.add_node(66)
ll.add_node(77)
ll.add_node(88)
ll.add_node(99)
ll.traverse_ll()
ll.reverse()
print()
ll.traverse_ll()
print()