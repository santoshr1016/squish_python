# Use this class to create binary trees.
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    # Overriding the equality operator.
    # This will be used for testing your solution.
    def __eq__(self, other):
        if type(other) is type(self):
            return self.value == other.value
        return False

#  head2 = 15           lca2(15, 8, 13)
#        /   \
#       10     24
#      /\    / \
#     5  13  20  30
#    /\
#   2  8
# Works only for BST
def lca2(root, a, b):
    while root:
        if (a<=root.value and b>root.value) or (a>root.value) and b<=root.value:
            return root
        if a < root.value:
            root = root.left
        else:
            root = root.right


# Implement your function below.
def lca(root, j, k):
    path_to_j = path_to_x(root, j)
    print_path(root, [], 0, j)
    path_to_jj = path_to_xx(root, [], j)
    path_to_k = path_to_x(root, k)
    print_path(root, [], 0, k)
    path_to_kk = path_to_xx(root, [], k)


    lca_to_return = None
    while path_to_j and path_to_k:
        j_pop = path_to_j.pop()
        k_pop = path_to_k.pop()
        if j_pop is k_pop:
            lca_to_return = j_pop
        else:
            break
    return lca_to_return

# print_path(root, [], 0, j)
def print_path(root, l, count, x):
    if not root:
        return None
    l.insert(count, root.value)
    count += 1
    if root.value == x:
        print(l[:count])
    else:
        if root.left:
            print_path(root.left, l, count, x)
        if root.right:
            print_path(root.right, l, count, x)


def path_to_x(root, x):
    if root is None:
        return None
    if root.value == x:
        return [root.value]
    left_path = path_to_x(root.left, x)
    if left_path is not None:
        left_path.append(root.value)
        return left_path
    right_path = path_to_x(root.right, x)
    if right_path is not None:
        right_path.append(root.value)
        return right_path
    return None

# Only good for BST
def path_to_xx(root, stack, x):
    if root is None:
        return None
    if root.value == x:
        return stack.append(root.value)
    else:
        stack.append(root.value)
    if root.value > x:
        path_to_xx(root.left, stack, x)
    else:
        path_to_xx(root.right, stack, x)
    return stack

# A function for creating a tree.
# Input:
# - mapping: a node-to-node mapping that shows how the tree should be constructed
# - head_value: the value that will be used for the head ndoe
# Output:
# - The head node of the resulting tree
def create_tree(mapping, head_value):
    head = Node(value=head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head


# NOTE: The following values will be used for testing your solution.

# The mapping we're going to use for constructing a tree.
# {0: [1, 2]} means that 0's left child is 1, and its right
# child is 2.
# mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
# head1 = create_tree(mapping1, 0)
# This tree is:
# head1 = 0
#        / \
#       1   2
#      /\   /\
#     3  4 5  6


mapping2 = {15: [10, 24], 10: [5, 13], 5: [2, 8], 24: [20, 30]}
head2 = create_tree(mapping2, 15)
# This tree is:
#  head2 = 15
#        /   \
#       10     24
#      /\    / \
#     5  13  20  30
#    /\
#   2  8


# lca(head1, 1, 5) should return 0
# lca(head1, 3, 1) should return 1
# lca(head1, 1, 4) should return 1
# lca(head1, 0, 5) should return 0
# lca(head2, 4, 7) should return 5
# lca(head2, 3, 3) should return 3
print(lca(head2, 8, 30))  # should return 1
# print(lca2(head2, 2, 30))  # should return 1
# lca(head2, 3, 0) should return None (0 does not exist in the tree)