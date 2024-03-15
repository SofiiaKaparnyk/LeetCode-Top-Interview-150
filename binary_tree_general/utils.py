def print_tree(root):
    _print_tree_recursively(root, 0)


def _print_tree_recursively(node, level):
    if node is not None:
        _print_tree_recursively(node.right, level + 1)
        print(" " * 4 * level + "->", node.val)
        _print_tree_recursively(node.left, level + 1)
