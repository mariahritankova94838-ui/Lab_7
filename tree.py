class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def find_max_brightness(root):
    if not root:
        return float('-inf')
    max_val = root.val
    left_max = find_max_brightness(root.left)
    right_max = find_max_brightness(root.right)
    return max(max_val, left_max, right_max)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(14)
    root.right.right = TreeNode(15)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(0)
    root.right.right.left.right = TreeNode(6)
    root.right.right.left.right.right = TreeNode(1)
    result = find_max_brightness(root)
    print(result)