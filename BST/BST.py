class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        return self.FindNodeByKeyRecursive(key, self.Root, BSTFind()) # возвращает BSTFind

    def FindNodeByKeyRecursive(self, key, node, find):
        if node is not None:
            find.Node = node
            if node.NodeKey == key:
                find.NodeHasKey = True
                return find
            if node.NodeKey < key:
                find.ToLeft = False
                return self.FindNodeByKeyRecursive(key, node.RightChild, find)
            if node.NodeKey > key:
                find.ToLeft = True
                return self.FindNodeByKeyRecursive(key, node.LeftChild, find)
        return find

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        currentNode = self.FindNodeByKey(key)
        if currentNode.NodeHasKey:
            return False  # если ключ уже есть
        newNode = BSTNode(key, val, currentNode.Node)
        if currentNode.Node is None:
            self.Root = newNode
            return True
        if currentNode.ToLeft:
            currentNode.Node.LeftChild = newNode
        else:
            currentNode.Node.RightChild = newNode
        return True

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        if FromNode is None:
            return None
        node = FromNode
        if FindMax:
            while node.RightChild is not None:
                node = node.RightChild
            return node
        else:
            while node.LeftChild is not None:
                node = node.LeftChild
            return node

    def isLeaf(self, node):
        if node.LeftChild is None and node.RightChild is None:
            return True
        return False

    def DeleteNodeByKey(self, key):
        foundNode = self.FindNodeByKey(key)
        if foundNode.NodeHasKey is False:
            return False
        nodeToDelete = foundNode.Node

        if self.isLeaf(nodeToDelete) is True and nodeToDelete.Parent is None:
            self.Root = None
            return True

        if self.isLeaf(nodeToDelete):
            if foundNode.ToLeft:
                nodeToDelete.Parent.LeftChild = None
            else:
                nodeToDelete.Parent.RightChild = None
            nodeToDelete.Parent = None

        elif nodeToDelete.LeftChild is not None and nodeToDelete.RightChild is not None:
            successorNode = self.FinMinMax(nodeToDelete.RightChild, False)
            self.DeleteNodeByKey(successorNode.NodeKey)
            if nodeToDelete is self.Root:
                self.Root = successorNode
            else:
                nodeToDelete.Parent.RightChild = successorNode
            successorNode.Parent = nodeToDelete.Parent
            successorNode.RightChild = nodeToDelete.RightChild
            successorNode.LeftChild = nodeToDelete.LeftChild
            successorNode.RightChild.Parent = successorNode
            successorNode.LeftChild.Parent = successorNode
            nodeToDelete.Parent = None
            nodeToDelete.LeftChild = None
            nodeToDelete.RightChild = None

        else:
            if nodeToDelete.LeftChild is None:
                successorNode = nodeToDelete.RightChild
            else:
                successorNode = nodeToDelete.LeftChild
            if nodeToDelete is self.Root:
                self.Root = successorNode
                successorNode.Parent = None
            else:
                if foundNode.ToLeft:
                    nodeToDelete.Parent.LeftChild = successorNode
                else:
                    nodeToDelete.Parent.RightChild = successorNode
                successorNode.Parent = nodeToDelete.Parent
            nodeToDelete.LeftChild = None
            nodeToDelete.RightChild = None
            nodeToDelete.Parent = None

        return True

    def Count(self):
        return self.CountRecursive(self.Root)  # количество узлов в дереве

    def CountRecursive(self, node):
        if node is None:
            return 0
        rightCount = self.CountRecursive(node.RightChild)
        leftCount = self.CountRecursive(node.LeftChild)
        return 1 + rightCount + leftCount

    def WideAllNodes(self):
        result = []
        if self.Root is None:
            return ()
        nodes = [self.Root]

        while nodes:
            currentNodes = []
            for item in nodes:
                result.append(item)
                if item.LeftChild:
                    currentNodes += [item.LeftChild]
                if item.RightChild:
                    currentNodes += [item.RightChild]
            nodes = currentNodes

        return tuple(result)

    def DeepAllNodes(self, order):
        result = []
        if self.Root is None:
            return ()

        def inOrder(node):
            if node is None:
                return ()
            inOrder(node.LeftChild)
            result.append(node)
            inOrder(node.RightChild)

        def postOrder(node):
            if node is None:
                return ()
            postOrder(node.LeftChild)
            postOrder(node.RightChild)
            result.append(node)

        def preOrder(node):
            if node is None:
                return ()
            result.append(node)
            preOrder(node.LeftChild)
            preOrder(node.RightChild)

        if order == 0:
            inOrder(self.Root)
        elif order == 1:
            postOrder(self.Root)
        elif order == 2:
            preOrder(self.Root)

        return tuple(result)

    def Identic(self, paramTree):
        return self.IdenticRecursive(self.Root, paramTree.Root)

    def IdenticRecursive(self, initNode, paramNode):
        if initNode is None and paramNode is None:
            return True
        if initNode is None or paramNode is None:
            return False
        if initNode.NodeKey != paramNode.NodeKey:
            return False
        left = self.IdenticRecursive(initNode.LeftChild, paramNode.LeftChild)
        right = self.IdenticRecursive(initNode.RightChild, paramNode.RightChild)
        if left and right:
            return True
        return False