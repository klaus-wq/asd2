class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.Level = None # уровень


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def SetLevelForNode(self):
        if self.Root is None:
            return
        self.SetLevelForNodeRecursive(self.Root, 0)

    def SetLevelForNodeRecursive(self, node, level):
        node.Level = level
        for child in node.Children:
            self.SetLevelForNodeRecursive(child, level + 1)

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            if self.Root is not None:
                self.Root.Parent = NewChild
                NewChild.Children.append(self.Root)
            self.Root = NewChild
            return None
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
