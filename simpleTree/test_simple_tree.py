import unittest

from simple_tree import SimpleTree, SimpleTreeNode

class SimpleTreeTests(unittest.TestCase):

    def setUp(self):
        self.simpleTree = SimpleTree(None)

    def testAddChild(self):
        root = SimpleTreeNode(1, None)
        self.simpleTree.AddChild(None, root)
        self.assertEqual(root.Children, [])
        self.assertEqual(root.Parent, None)

        child1 = SimpleTreeNode(11, None)
        self.simpleTree.AddChild(root, child1)
        child2 = SimpleTreeNode(12, None)
        self.simpleTree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simpleTree.AddChild(child1, child11)

        self.assertEqual(root.Children, [child1, child2])
        self.assertEqual(root.Parent, None)
        self.assertEqual(child1.Parent, root)
        self.assertEqual(child1.Children, [child11])
        self.assertEqual(child2.Parent, root)
        self.assertEqual(child2.Children, [])
        self.assertEqual(child11.Parent, child1)
        self.assertEqual(child11.Children, [])

    def testDeleteNode(self):
        root = SimpleTreeNode(1, None)
        self.simpleTree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simpleTree.AddChild(root, child1)
        child2 = SimpleTreeNode(12, None)
        self.simpleTree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simpleTree.AddChild(child1, child11)
        child12 = SimpleTreeNode(112, None)
        self.simpleTree.AddChild(child1, child12)

        self.simpleTree.DeleteNode(child1)

        self.assertEqual(root.Children, [child2])
        self.assertEqual(child1.Children, [])
        self.assertEqual(child1.Parent, None)
        self.assertEqual(child11.Children, [])
        self.assertEqual(child11.Parent, None)
        self.assertEqual(child12.Children, [])
        self.assertEqual(child12.Parent, None)

        self.simpleTree.DeleteNode(child2)

        self.assertEqual(root.Children, [])
        self.assertEqual(child2.Children, [])
        self.assertEqual(child2.Parent, None)

    def testGetAllNodes(self):
        self.assertCountEqual(self.simpleTree.GetAllNodes(), [])

        root = SimpleTreeNode(1, None)
        self.simpleTree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simpleTree.AddChild(root, child1)
        child2 = SimpleTreeNode(12, None)
        self.simpleTree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simpleTree.AddChild(child1, child11)
        child12 = SimpleTreeNode(112, None)
        self.simpleTree.AddChild(child1, child12)

        nodes = self.simpleTree.GetAllNodes()

        self.assertCountEqual(nodes, [root, child1, child2, child11, child12])

    def testFindNodesByValue(self):
        root = SimpleTreeNode(1, None)
        self.simpleTree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simpleTree.AddChild(root, child1)
        child2 = SimpleTreeNode(11, None)
        self.simpleTree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simpleTree.AddChild(child1, child11)
        child12 = SimpleTreeNode(112, None)
        self.simpleTree.AddChild(child1, child12)

        self.assertCountEqual(self.simpleTree.FindNodesByValue(1), [root])
        self.assertCountEqual(self.simpleTree.FindNodesByValue(11), [child1, child2])
        self.assertCountEqual(self.simpleTree.FindNodesByValue(0), [])

    def testMoveNode(self):
        root = SimpleTreeNode(1, None)
        self.simpleTree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simpleTree.AddChild(root, child1)
        child2 = SimpleTreeNode(12, None)
        self.simpleTree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simpleTree.AddChild(child1, child11)
        child111 = SimpleTreeNode(111, None)
        self.simpleTree.AddChild(child11, child111)

        self.simpleTree.MoveNode(child1, child2)

        self.assertEqual(root.Children, [child2])
        self.assertEqual(child1.Children, [child11])
        self.assertEqual(child11.Parent, child1)
        self.assertEqual(child1.Parent, child2)
        self.assertEqual(child2.Children, [child1])
        self.assertEqual(child11.Children, [child111])
        self.assertEqual(child111.Parent, child11)
        self.assertEqual(child111.Children, [])

    def testCount(self):
        self.assertEqual(self.simpleTree.Count(), 0)

        root = SimpleTreeNode(1, None)
        self.simpleTree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simpleTree.AddChild(root, child1)
        child2 = SimpleTreeNode(11, None)
        self.simpleTree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simpleTree.AddChild(child1, child11)
        child12 = SimpleTreeNode(112, None)
        self.simpleTree.AddChild(child1, child12)

        self.assertEqual(self.simpleTree.Count(), 5)

    def testLeafCount(self):
        self.assertEqual(self.simpleTree.LeafCount(), 0)

        root = SimpleTreeNode(1, None)
        self.simpleTree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simpleTree.AddChild(root, child1)
        child2 = SimpleTreeNode(11, None)
        self.simpleTree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simpleTree.AddChild(child1, child11)
        child12 = SimpleTreeNode(112, None)
        self.simpleTree.AddChild(child1, child12)

        self.assertEqual(self.simpleTree.LeafCount(), 3)

    def testEvenTrees(self):
        root = SimpleTreeNode(1, None)
        self.simpleTree.AddChild(None, root)
        child1 = SimpleTreeNode(2, None)
        self.simpleTree.AddChild(root, child1)
        child2 = SimpleTreeNode(3, None)
        self.simpleTree.AddChild(root, child2)
        child3 = SimpleTreeNode(6, None)
        self.simpleTree.AddChild(root, child3)
        child11 = SimpleTreeNode(5, None)
        self.simpleTree.AddChild(child1, child11)
        child12 = SimpleTreeNode(7, None)
        self.simpleTree.AddChild(child1, child12)
        self.assertEqual([node.NodeValue for node in self.simpleTree.EvenTrees()], [])
        child21 = SimpleTreeNode(4, None)
        self.simpleTree.AddChild(child2, child21)
        child31 = SimpleTreeNode(8, None)
        self.simpleTree.AddChild(child3, child31)
        child311 = SimpleTreeNode(9, None)
        self.simpleTree.AddChild(child31, child311)
        child312 = SimpleTreeNode(10, None)
        self.simpleTree.AddChild(child31, child312)
        self.assertEqual([node.NodeValue for node in self.simpleTree.EvenTrees()], [1, 3, 1, 6])

if __name__ == "__main__":
    unittest.main()