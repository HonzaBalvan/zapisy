import sys
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(str(node.val))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    trees = []

    for i in range(1, n + 1):
        line = data[i].strip()
        if not line:
            trees.append(None)
            continue
        values = list(map(int, line.split()))
        root = None
        for val in values:
            root = insert(root, val)
        trees.append(root)

    max_height = -1
    max_root_val = None
    for root in trees:
        if root is None:
            continue
        h = height(root)
        if h > max_height:
            max_height = h
            max_root_val = root.val

    output_lines = []
    for i, root in enumerate(trees):
        if root is None:
            output_lines.append("")
        else:
            levels = level_order(root)
            for level in levels:
                output_lines.append(" ".join(level))
        if i < len(trees) - 1:
            output_lines.append("")

    output_lines.append(f"{max_height} {max_root_val}")
    print("\n".join(output_lines))

if __name__ == "__main__":
    main()