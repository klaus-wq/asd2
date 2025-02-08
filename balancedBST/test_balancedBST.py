import unittest

from balancedBST import BalancedBST


class BalancedBSTTests(unittest.TestCase):
    def setUp(self):
        self.tree = BalancedBST()

    def testGenerateTree(self):
        self.tree.GenerateTree([])
        self.assertIsNone(self.tree.Root)
        self.tree.GenerateTree([50, 25, 75, 37, 62, 84, 31, 43, 55, 92])
        self.assertEqual(self.tree.Root.NodeKey, 55)
        self.assertEqual(self.tree.Root.Level, 0)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 37)
        self.assertEqual(self.tree.Root.LeftChild.Level, 1)
        self.assertEqual(self.tree.Root.LeftChild.Parent, self.tree.Root)
        self.assertEqual(self.tree.Root.LeftChild.LeftChild.NodeKey, 31)
        self.assertEqual(self.tree.Root.LeftChild.LeftChild.Level, 2)
        self.assertEqual(self.tree.Root.LeftChild.LeftChild.Parent, self.tree.Root.LeftChild)
        self.assertEqual(self.tree.Root.LeftChild.LeftChild.LeftChild.NodeKey, 25)
        self.assertEqual(self.tree.Root.LeftChild.LeftChild.Level, 2)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild.RightChild)
        self.assertEqual(self.tree.Root.LeftChild.RightChild.NodeKey, 50)
        self.assertEqual(self.tree.Root.LeftChild.RightChild.Level, 2)
        self.assertEqual(self.tree.Root.LeftChild.RightChild.Parent, self.tree.Root.LeftChild)
        self.assertEqual(self.tree.Root.LeftChild.RightChild.LeftChild.NodeKey, 43)
        self.assertEqual(self.tree.Root.LeftChild.RightChild.LeftChild.Level, 3)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild.RightChild)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 84)
        self.assertEqual(self.tree.Root.RightChild.Level, 1)
        self.assertEqual(self.tree.Root.RightChild.Parent, self.tree.Root)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 75)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.Level, 2)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.Parent, self.tree.Root.RightChild)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.LeftChild.NodeKey, 62)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.LeftChild.Level, 3)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)
        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 92)
        self.assertEqual(self.tree.Root.RightChild.RightChild.Level, 2)
        self.assertEqual(self.tree.Root.RightChild.RightChild.Parent, self.tree.Root.RightChild)
        self.assertIsNone(self.tree.Root.RightChild.RightChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.RightChild.RightChild)

    def testIsBalanced(self):
        self.tree.GenerateTree([])
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))
        self.tree.GenerateTree([1])
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))
        self.tree.GenerateTree([50, 25, 75, 37, 62, 84, 31, 43, 55, 92])
        self.assertTrue(self.tree.IsBalanced(self.tree.Root))

if __name__ == "__main__":
    unittest.main()