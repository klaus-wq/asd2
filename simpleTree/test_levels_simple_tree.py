import unittest

from levels_simple_tree import SimpleTree, SimpleTreeNode

class SimpleTreeTests(unittest.TestCase):

    def setUp(self):
        self.simpleTree = SimpleTree(None)

    def testSetLevelsForNode(self):
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

        self.simpleTree.SetLevelForNode()

        self.assertEqual(root.Level, 0)
        self.assertEqual(child1.Level, 1)
        self.assertEqual(child2.Level, 1)
        self.assertEqual(child11.Level, 2)

if __name__ == "__main__":
    unittest.main()