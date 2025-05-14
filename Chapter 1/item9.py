"""
Match is used for destructuring Nested Data

This function checks whether a target value exists in a binary search tree 
represented as nested tuples. Each node is a tuple: (pivot, left_subtree, right_subtree).

Note: Python structural pattern matching (`match`) is only available in Python 3.10+.
"""

def value_in_tree(tree, target):
    # Base case: reached a leaf node (non-tuple)
    if not isinstance(tree, tuple):
        return tree == target

    # Destructure tree using pattern matching
    match tree:
        # If target is less than pivot, search left subtree
        case pivot, left, _ if target < pivot:
            return value_in_tree(left, target)

        # If target is greater than pivot, search right subtree
        case pivot, _, right if target > pivot:
            return value_in_tree(right, target)

        # If target matches pivot
        case pivot, _, _ if target == pivot:
            return True

    # If none of the above match (shouldn't happen in valid BST)
    return False
