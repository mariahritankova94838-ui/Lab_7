class TreeNode:

    def init(self, value):
        self.val = value
        self.left = None
        self.right = None


def find_max_brightness(root):
    if not root:
        return float("-inf")

    max_val = root.val
    left_max = find_max_brightness(root.left)
    right_max = find_max_brightness(root.right)

    return max(max_val, left_max, right_max)



    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(5)

    result = find_max_brightness(root)
    print(result)
