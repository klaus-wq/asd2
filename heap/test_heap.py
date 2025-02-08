import unittest

from heap import Heap


class HeapTests(unittest.TestCase):

    def setUp(self):
        self.heap = Heap()

    def testMakeHeap(self):
        self.heap.MakeHeap([], 0)
        self.assertEqual(self.heap.HeapArray, [None])
        self.assertEqual(len(self.heap.HeapArray), 1)
        self.heap.MakeHeap([1], 0)
        self.assertEqual(self.heap.HeapArray, [1])
        self.assertEqual(len(self.heap.HeapArray), 1)
        self.heap.MakeHeap([10, 50, 4, 45, 2], 1)
        self.assertEqual(self.heap.HeapArray, [50, 10, 4])
        self.assertEqual(len(self.heap.HeapArray), 3)
        self.heap.MakeHeap([10, 50, 4, 45, 2, 6, 3], 2)
        self.assertEqual(self.heap.HeapArray, [50, 45, 6, 10, 2, 4, 3])
        self.assertEqual(len(self.heap.HeapArray), 7)
        self.heap.MakeHeap([10, 50, 4, 45, 2], 2)
        self.assertEqual(self.heap.HeapArray, [50, 45, 4, 10, 2, None, None])
        self.assertEqual(len(self.heap.HeapArray), 7)

    def testGetMax(self):
        self.heap.MakeHeap([10, 50, 4, 45, 2, 6, 3], 2)
        self.assertEqual(self.heap.GetMax(), 50)
        self.assertEqual(self.heap.HeapArray, [45, 10, 6, 3, 2, 4, None])
        self.assertEqual(self.heap.GetMax(), 45)
        self.assertEqual(self.heap.HeapArray, [10, 4, 6, 3, 2, None, None])
        self.assertEqual(self.heap.GetMax(), 10)
        self.assertEqual(self.heap.HeapArray, [6, 4, 2, 3, None, None, None])
        self.assertEqual(self.heap.GetMax(), 6)
        self.assertEqual(self.heap.HeapArray, [4, 3, 2, None, None, None, None])
        self.assertEqual(self.heap.GetMax(), 4)
        self.assertEqual(self.heap.HeapArray, [3, 2, None, None, None, None, None])
        self.assertEqual(self.heap.GetMax(), 3)
        self.assertEqual(self.heap.HeapArray, [2, None, None, None, None, None, None])
        self.assertEqual(self.heap.GetMax(), 2)
        self.assertEqual(self.heap.HeapArray, [None, None, None, None, None, None, None])
        self.assertEqual(self.heap.GetMax(), -1)
        self.assertEqual(self.heap.HeapArray, [None, None, None, None, None, None, None])

    def testAdd(self):
        self.heap.HeapArray = []
        self.assertFalse(self.heap.Add(1))
        self.heap.HeapArray = [None, None, None, None, None, None, None]
        self.assertTrue(self.heap.Add(1))
        self.assertEqual(self.heap.HeapArray, [1, None, None, None, None, None, None])
        self.assertTrue(self.heap.Add(5))
        self.assertEqual(self.heap.HeapArray, [5, 1, None, None, None, None, None])
        self.assertTrue(self.heap.Add(50))
        self.assertEqual(self.heap.HeapArray, [50, 1, 5, None, None, None, None])
        self.assertTrue(self.heap.Add(45))
        self.assertEqual(self.heap.HeapArray, [50, 45, 5, 1, None, None, None])
        self.assertTrue(self.heap.Add(54))
        self.assertEqual(self.heap.HeapArray, [54, 50, 5, 1, 45, None, None])
        self.assertTrue(self.heap.Add(32))
        self.assertEqual(self.heap.HeapArray, [54, 50, 32, 1, 45, 5, None])
        self.assertTrue(self.heap.Add(543))
        self.assertEqual(self.heap.HeapArray, [543, 50, 54, 1, 45, 5, 32])
        self.assertFalse(self.heap.Add(1))


if __name__ == "__main__":
    unittest.main()