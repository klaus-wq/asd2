class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            if self.Root is not None:
                self.Root.Parent = NewChild
                NewChild.Children.append(self.Root)
            self.Root = NewChild
            return None
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None
            while NodeToDelete.Children:
                self.DeleteNode(NodeToDelete.Children[0])

    def GetAllNodes(self):
        if self.Root is None:
            return []
        return self.GetAllNodesRecursive(self.Root)

    def GetAllNodesRecursive(self, node):
        resultNodes = []
        resultNodes.append(node)
        for child in node.Children:
            resultNodes += self.GetAllNodesRecursive(child)
        return resultNodes

    def FindNodesByValue(self, val):
        resultNodes = []
        for item in self.GetAllNodes():
            if item.NodeValue == val:
                resultNodes.append(item)
        return resultNodes

    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        leafCount = 0
        for item in self.GetAllNodes():
            if not item.Children:
                leafCount += 1
        return leafCount

    def EvenTrees(self):
        return self.CheckSubTree(self.Root)

    def CheckSubTree(self, currentNode):
        pairs = []
        for child in currentNode.Children:
            self.CheckSubTree(child)
            if len(self.GetAllNodesRecursive(child)) % 2 == 0:
                pairs.append(currentNode)
                pairs.append(child)
        return pairs