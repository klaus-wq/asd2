import unittest

from simple_tree import SimpleTree, SimpleTreeNode

class SimpleTreeTests(unittest.TestCase):

    def setUp(self):
        self.simple_tree = SimpleTree(None)

    def testAddChild(self):
        root = SimpleTreeNode(1, None)
        self.simple_tree.AddChild(None, root)
        self.assertEqual(root.Children, [])
        self.assertEqual(root.Parent, None)

        child1 = SimpleTreeNode(11, None)
        self.simple_tree.AddChild(root, child1)
        child2 = SimpleTreeNode(12, None)
        self.simple_tree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simple_tree.AddChild(child1, child11)

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
        self.simple_tree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simple_tree.AddChild(root, child1)
        child2 = SimpleTreeNode(12, None)
        self.simple_tree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simple_tree.AddChild(child1, child11)
        child12 = SimpleTreeNode(112, None)
        self.simple_tree.AddChild(child1, child12)

        self.simple_tree.DeleteNode(child1)

        self.assertEqual(root.Children, [child2])
        self.assertEqual(child1.Children, [])
        self.assertEqual(child1.Parent, None)
        self.assertEqual(child11.Children, [])
        self.assertEqual(child11.Parent, None)
        self.assertEqual(child12.Children, [])
        self.assertEqual(child12.Parent, None)

        self.simple_tree.DeleteNode(child2)

        self.assertEqual(root.Children, [])
        self.assertEqual(child2.Children, [])
        self.assertEqual(child2.Parent, None)

    def testGetAllNodes(self):
        self.assertCountEqual(self.simple_tree.GetAllNodes(), [])

        root = SimpleTreeNode(1, None)
        self.simple_tree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simple_tree.AddChild(root, child1)
        child2 = SimpleTreeNode(12, None)
        self.simple_tree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simple_tree.AddChild(child1, child11)
        child12 = SimpleTreeNode(112, None)
        self.simple_tree.AddChild(child1, child12)

        nodes = self.simple_tree.GetAllNodes()

        self.assertCountEqual(nodes, [root, child1, child2, child11, child12])

    def testFindNodesByValue(self):
        root = SimpleTreeNode(1, None)
        self.simple_tree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simple_tree.AddChild(root, child1)
        child2 = SimpleTreeNode(11, None)
        self.simple_tree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simple_tree.AddChild(child1, child11)
        child12 = SimpleTreeNode(112, None)
        self.simple_tree.AddChild(child1, child12)

        self.assertCountEqual(self.simple_tree.FindNodesByValue(1), [root])
        self.assertCountEqual(self.simple_tree.FindNodesByValue(11), [child1, child2])
        self.assertCountEqual(self.simple_tree.FindNodesByValue(0), [])

    def testMoveNode(self):
        root = SimpleTreeNode(1, None)
        self.simple_tree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simple_tree.AddChild(root, child1)
        child2 = SimpleTreeNode(12, None)
        self.simple_tree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simple_tree.AddChild(child1, child11)
        child111 = SimpleTreeNode(111, None)
        self.simple_tree.AddChild(child11, child111)

        self.simple_tree.MoveNode(child1, child2)

        self.assertEqual(root.Children, [child2])
        self.assertEqual(child1.Children, [child11])
        self.assertEqual(child11.Parent, child1)
        self.assertEqual(child1.Parent, child2)
        self.assertEqual(child2.Children, [child1])
        self.assertEqual(child11.Children, [child111])
        self.assertEqual(child111.Parent, child11)
        self.assertEqual(child111.Children, [])

    def testCount(self):
        self.assertEqual(self.simple_tree.Count(), 0)

        root = SimpleTreeNode(1, None)
        self.simple_tree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simple_tree.AddChild(root, child1)
        child2 = SimpleTreeNode(11, None)
        self.simple_tree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simple_tree.AddChild(child1, child11)
        child12 = SimpleTreeNode(112, None)
        self.simple_tree.AddChild(child1, child12)

        self.assertEqual(self.simple_tree.Count(), 5)

    def test_regression_LeafCount(self):
        self.assertEqual(self.simple_tree.LeafCount(), 0)

        root = SimpleTreeNode(1, None)
        self.simple_tree.AddChild(None, root)
        child1 = SimpleTreeNode(11, None)
        self.simple_tree.AddChild(root, child1)
        child2 = SimpleTreeNode(11, None)
        self.simple_tree.AddChild(root, child2)
        child11 = SimpleTreeNode(111, None)
        self.simple_tree.AddChild(child1, child11)
        child12 = SimpleTreeNode(112, None)
        self.simple_tree.AddChild(child1, child12)

        self.assertEqual(self.simple_tree.LeafCount(), 3)

if __name__ == "__main__":
    unittest.main()