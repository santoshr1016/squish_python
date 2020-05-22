from queue import Queue
from collections import OrderedDict

class Tree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, val):
        if self.data > val:
            if not self.left:
                self.left = Tree(val)
            else:
                self.left.add_node(val)
        else:
            if not self.right:
                self.right = Tree(val)
            else:
                self.right.add_node(val)

    def inorder(self):
        if not self:
            return
        else:
            if self.left:
                self.left.inorder()
            print(self.data, end=" ")
            if self.right:
                self.right.inorder()

    def iterative_inorder(self):
        result = []
        stack = []
        root = self
        while True:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                break
            node = stack.pop()
            result.append(node.data)
            root = node.right
        print(result)

    def preorder(self):
        if not self:
            return
        else:
            print(self.data, end=" ")
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def iterative_preorder(self):
        result = []
        stack = []
        root = self
        while True:
            while root:
                result.append(root.data)
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                break
            node = stack.pop()
            root = node.right
        print(result)

    def postorder(self):
        if not self:
            return
        else:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.data, end=" ")

    def iterative_postorder(self):
        stack = []
        node = self
        while True:
            while node:
                stack.append((node.data * -1, node))  # Negating the data to mark as Visited Node
                node = node.left
            if len(stack) == 0:
                break
            data, node = stack.pop()
            if data < 0:
                data *= -1
                stack.append((node.data, node))
                node = node.right
            else:
                print(node.data, end=" ")
                node = None

    def largestValuesInTreeRows(self):
        if self is None:
            return []
        result = []
        result_list = []
        q = Queue()
        q.put(self)
        q.put("*")

        while not q.empty():
            node = q.get()
            if node == "*":
                if not q.empty():
                    q.put("*")
                result_list.append(result)
                result = []
            else:
                result.append(node.data)

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

        print(result_list)
        # final = [max(item) for item in result_list]
        # return final

    def level_order(self):
        result = list()
        if not self:
            return
        q = Queue()
        q.put(self)
        while not q.empty():
            node = q.get()
            result.append(node.data)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        print(result)

    def height_using_level_order(self):
        result = list()
        if not self:
            return
        q = Queue()
        q.put(self)
        q.put(None)
        ht = 0
        while not q.empty():
            node = q.get()
            if node is None:
                if not q.empty():
                    q.put(None)
                ht = ht + 1
            else:
                result.append(node.data)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        print(ht)

    def height_using_recursion(self):
        h1, h2 = 0, 0
        if not self:
            return 0
        if self.left:
            h1 = self.left.height_using_recursion()
        if self.right:
            h2 = self.right.height_using_recursion()

        return max(h1, h2) + 1

    def sum_of_all_nodes(self):
        total = 0
        if not self:
            return 0
        mid = self.data
        ldata, rdata = 0, 0
        if self.left:
            ldata = self.left.sum_of_all_nodes()
        if self.right:
            rdata = self.right.sum_of_all_nodes()

        return mid + ldata + rdata

    def print_path(self, root, l, count, summ=260):
        if not root:
            return None
        l.insert(count, root.data)
        count += 1
        if root.left is None and root.right is None:
            print(l[:count])
            if sum(l[:count]) == summ:
                print("THIS ABOVE IS THE PATH HAVING SUM {0}".format(summ))
        else:
            if root.left:
                self.print_path(root.left, l, count, summ)
            if root.right:
                self.print_path(root.right, l, count, summ)

    def print_all_paths(self):
        root = self
        count = 0
        self.print_path(root, [], count)

    def vertical_order(self):
        od = OrderedDict()
        root = self
        q = Queue()
        hd = 0
        q.put((root, hd))
        od[hd] = [(root, hd)]
        while not q.empty():
            node, hd = q.get()
            if node.left:
                if not od.get(hd - 1, 0):
                    od[hd - 1] = [(node.left, hd - 1)]
                else:
                    od.get(hd - 1).append((node.left, hd - 1))
                q.put((node.left, hd - 1))
            if node.right:
                if not od.get(hd + 1, 0):
                    od[hd + 1] = [(node.right, hd + 1)]
                else:
                    od.get(hd + 1).append((node.right, hd + 1))
                q.put((node.right, hd + 1))
        for list_items in od.values():
            for item in list_items:
                print(item[0].data, item[1])



t = Tree(50)
t.add_node(35)
t.add_node(65)
t.add_node(30)
t.add_node(40)
t.add_node(75)
t.add_node(38)
t.add_node(70)
t.add_node(80)

print("inorder:", end=" ")
t.inorder()
print("\npostorder:", end=" ")
t.postorder()
print("\npreorder:", end="",)
t.preorder()
print("\n","*"*5, "Level Order", "*"*5)
t.level_order()
print("*"*5, "Height Using Level Order", "*"*5)
t.height_using_level_order()
print("*"*5, "Height Using Level Order", "*"*33)
print(t.largestValuesInTreeRows())
print("*"*5, "Height Using Recursion", "*"*5)
print(t.height_using_recursion())
print("*"*5, "Sum of all Nodes", "*"*5)
print(t.sum_of_all_nodes())
print("*"*5, "Print All paths and a path has sum 260", "*"*5)
t.print_all_paths()
print("*"*5, "Non recursive Inorder", "*"*5)
t.iterative_inorder()
print("*"*5, "Non recursive Preorder", "*"*5)
t.iterative_preorder()
print("*"*5, "Non recursive Postorder", "*"*5)
t.iterative_postorder()
print()
print("*"*5, "Vertical Order", "*"*5)
t.vertical_order()
print("*"*5, "", "*"*5)

print("*"*5, "", "*"*5)

print("*"*5, "", "*"*5)

print("*"*5, "", "*"*5)





