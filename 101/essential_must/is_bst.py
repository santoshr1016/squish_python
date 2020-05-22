def is_bst(root, lower_limit=None, upper_limit=None):
    if lower_limit is not None and root.data < lower_limit:
        return False
    if upper_limit is not None and upper_limit < root.data:
        return False
    is_left_bst = True
    is_right_bst = True

    if root.left is not None:
        is_left_bst = is_bst(root.left, lower_limit, root.data)
    if is_left_bst and root.right is not None:
        is_right_bst = is_bst(root.right, root.data, upper_limit)

    return is_left_bst and is_right_bst