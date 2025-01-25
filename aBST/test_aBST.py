import unittest

from aBST import aBST


class aBSTTests(unittest.TestCase):

    def setUp(self) -> None:
        self.tree = aBST(3)
        self.tree.Tree[0] = 50
        self.tree.Tree[1] = 25
        self.tree.Tree[2] = 75
        self.tree.Tree[4] = 37
        self.tree.Tree[5] = 62
        self.tree.Tree[6] = 84
        self.tree.Tree[9] = 31
        self.tree.Tree[10] = 43
        self.tree.Tree[11] = 55
        self.tree.Tree[14] = 92

    def testLength(self):
        tree = aBST(0)
        self.assertEqual(len(tree.Tree), 1)
        tree1 = aBST(1)
        self.assertEqual(len(tree1.Tree), 3)
        tree2 = aBST(5)
        self.assertEqual(len(tree2.Tree), 63)

    def testFindKeyIndex(self):
        tree = aBST(0)
        self.assertEqual(tree.FindKeyIndex(50), 0)
        self.assertEqual(self.tree.FindKeyIndex(50), 0)
        self.assertEqual(self.tree.FindKeyIndex(62), 5)
        self.assertEqual(self.tree.FindKeyIndex(43), 10)
        self.assertIsNone(self.tree.FindKeyIndex(28))
        self.assertIsNone(self.tree.FindKeyIndex(51))
        self.assertIsNone(self.tree.FindKeyIndex(100))
        self.assertEqual(self.tree.FindKeyIndex(20), -3)
        self.assertEqual(self.tree.FindKeyIndex(65), -12)
        self.assertEqual(self.tree.FindKeyIndex(80), -13)

    def testAddKey(self):
        tree = aBST(3)
        self.assertEqual(tree.AddKey(1), 0)
        self.assertEqual(self.tree.AddKey(100), -1)
        self.assertEqual(self.tree.Tree, [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92])
        self.assertEqual(self.tree.AddKey(20), 3)
        self.assertEqual(self.tree.Tree, [50, 25, 75, 20, 37, 62, 84, None, None, 31, 43, 55, None, None, 92])
        self.assertEqual(self.tree.AddKey(100), -1)
        self.assertEqual(self.tree.Tree, [50, 25, 75, 20, 37, 62, 84, None, None, 31, 43, 55, None, None, 92])
        self.assertEqual(self.tree.AddKey(70), 12)
        self.assertEqual(self.tree.Tree,[50, 25, 75, 20, 37, 62, 84, None, None, 31, 43, 55, 70, None, 92],)


if __name__ == "__main__":
    unittest.main()
