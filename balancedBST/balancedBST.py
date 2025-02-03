class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        a.sort()
        return self.GenerateTreeRecursive(None, a)

    def GenerateTreeRecursive(self, parent, a):
        if len(a) == 0:
            return None
        middleIndex: int = len(a) // 2
        node = BSTNode(a[middleIndex], parent)
        if parent is None:
            self.Root = node
        node.LeftChild = self.GenerateTreeRecursive(node, a[:middleIndex])
        node.RightChild = self.GenerateTreeRecursive(node, a[middleIndex + 1:])
        return node

    def IsBalanced(self, root_node):
        if root_node is None:
            return True
        return self.IsBalancedRecursive(root_node)[0] # сбалансировано ли дерево с корнем root_node

    def IsBalancedRecursive(self, tree):
        if tree is None:
            return True, 0
        left, leftLevel = self.IsBalancedRecursive(tree.LeftChild)
        right, rightLevel = self.IsBalancedRecursive(tree.RightChild)
        isBalanced = (left and right and abs(leftLevel - rightLevel) <= 1)
        return isBalanced, max(leftLevel, rightLevel) + 1