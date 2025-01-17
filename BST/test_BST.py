import unittest
import random

from BST import BSTNode, BST


class BSTTests(unittest.TestCase):

    def setUp(self):
        self.root = BSTNode(1, 1, None)
        self.rootLeft = BSTNode(2, 2, self.root)
        self.rootRight = BSTNode(6, 6, self.root)
        self.rootRightLeft = BSTNode(5, 5, self.rootRight)
        self.rootRightRight = BSTNode(7, 7, self.rootRight)
        self.rootRight.LeftChild = self.rootRightLeft
        self.rootRight.RightChild = self.rootRightRight
        self.root.LeftChild = self.rootLeft
        self.root.RightChild = self.rootRight

        self.tree = BST(self.root)

    def testFindNodeByKey(self):
        tree = BST(None)
        node = tree.FindNodeByKey(0)
        self.assertEqual(node.Node, None)
        self.assertEqual(node.NodeHasKey, False)
        self.assertEqual(node.ToLeft, False)
        node = self.tree.FindNodeByKey(11)
        self.assertEqual(node.Node, self.rootRightRight)
        self.assertEqual(node.NodeHasKey, False)
        self.assertEqual(node.ToLeft, False)
        node = self.tree.FindNodeByKey(3)
        self.assertEqual(node.Node, self.rootRightLeft)
        self.assertEqual(node.NodeHasKey, False)
        self.assertEqual(node.ToLeft, True)
        node = self.tree.FindNodeByKey(6)
        self.assertEqual(node.Node, self.rootRight)
        self.assertEqual(node.NodeHasKey, True)
        node = self.tree.FindNodeByKey(1)
        self.assertEqual(node.Node, self.root)
        self.assertEqual(node.NodeHasKey, True)

    def testAddKeyValue(self):
        tree = BST(None)
        self.assertEqual(tree.AddKeyValue(1, 1), True)
        self.assertEqual(tree.Root.NodeKey, 1)
        self.assertEqual(tree.Root.NodeValue, 1)
        self.assertEqual(tree.Root.LeftChild, None)
        self.assertEqual(tree.Root.RightChild, None)
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(self.tree.AddKeyValue(1, 1), False)
        self.assertEqual(self.root.NodeKey, 1)
        self.assertEqual(self.root.NodeValue, 1)
        self.assertEqual(self.tree.AddKeyValue(3, 3), True)
        self.assertEqual(self.rootRightLeft.LeftChild.Parent, self.rootRightLeft)
        self.assertEqual(self.rootRightLeft.LeftChild.NodeKey, 3)
        self.assertEqual(self.rootRightLeft.LeftChild.NodeValue, 3)
        self.assertEqual(self.tree.AddKeyValue(11, 11), True)
        self.assertEqual(self.rootRightRight.RightChild.Parent, self.rootRightRight)
        self.assertEqual(self.rootRightRight.RightChild.NodeKey, 11)
        self.assertEqual(self.rootRightRight.RightChild.NodeValue, 11)

    def testFinMinMax(self):
        tree = BST(None)
        self.assertIsNone(tree.FinMinMax(tree.Root, True))
        self.assertIsNone(tree.FinMinMax(tree.Root, False))
        maxRoot = self.tree.FinMinMax(self.root, True)
        self.assertEqual(maxRoot, self.rootRightRight)
        minRoot = self.tree.FinMinMax(self.root, False)
        self.assertEqual(minRoot, self.rootLeft)
        maxSubtree = self.tree.FinMinMax(self.rootRight, True)
        self.assertEqual(maxSubtree, self.rootRightRight)
        minSubtree = self.tree.FinMinMax(self.rootRight, False)
        self.assertEqual(minSubtree, self.rootRightLeft)

    def testDeleteNodeByKey(self):
        tree = BST(None)
        self.assertFalse(tree.DeleteNodeByKey(10))
        self.assertFalse(self.tree.DeleteNodeByKey(2))
        self.assertTrue(self.tree.DeleteNodeByKey(1))
        self.assertFalse(self.tree.FindNodeByKey(1).NodeHasKey)
        self.assertTrue(self.tree.DeleteNodeByKey(6))
        self.assertFalse(self.tree.FindNodeByKey(6).NodeHasKey)
        self.assertTrue(self.tree.DeleteNodeByKey(2))
        self.assertFalse(self.tree.FindNodeByKey(2).NodeHasKey)

    def testCount(self):
        tree = BST(None)
        self.assertEqual(tree.Count(), 0)
        self.assertEqual(self.tree.Count(), 5)
        self.tree.AddKeyValue(3, 3)
        self.assertEqual(self.tree.Count(), 6)
        self.tree.DeleteNodeByKey(1)
        self.assertEqual(self.tree.Count(), 5)


if __name__ == "__main__":
    unittest.main()