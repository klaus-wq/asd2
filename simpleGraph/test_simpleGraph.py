
import unittest

from simpleGraph import SimpleGraph

class TestsSimpleGraph(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(5)

    def testAddVertex(self):
        self.graph.AddVertex(10)
        self.assertEqual(self.graph.vertex[0].Value, 10)
        self.assertFalse(self.graph.IsEdge(0, 0))
        self.assertFalse(self.graph.IsEdge(0, 1))
        self.assertFalse(self.graph.IsEdge(0, 2))
        self.assertFalse(self.graph.IsEdge(0, 0))
        self.assertFalse(self.graph.IsEdge(1, 0))
        self.assertFalse(self.graph.IsEdge(2, 0))

    def testAddEdge(self):
        self.graph.AddVertex(10)
        self.graph.AddVertex(20)
        self.assertFalse(self.graph.IsEdge(0, 2))
        self.graph.AddEdge(0, 2)
        self.assertTrue(self.graph.IsEdge(0, 2))
        self.assertTrue(self.graph.IsEdge(2, 0))

    def testRemoveEdge(self):
        self.graph.AddVertex(10)
        self.graph.AddVertex(20)
        self.graph.AddEdge(0, 2)
        self.assertTrue(self.graph.IsEdge(0, 2))
        self.graph.RemoveEdge(0, 2)
        self.assertFalse(self.graph.IsEdge(0, 2))
        self.assertFalse(self.graph.IsEdge(2, 0))

    def testRemoveVertex(self):
        self.graph.AddVertex(10)
        self.graph.AddVertex(20)
        self.graph.AddVertex(30)
        self.graph.AddEdge(0, 0)
        self.graph.AddEdge(0, 2)
        self.assertTrue(self.graph.IsEdge(0, 0))
        self.assertTrue(self.graph.IsEdge(0, 2))
        self.graph.RemoveVertex(0)
        self.assertIsNone(self.graph.vertex[0])
        self.assertFalse(self.graph.IsEdge(0, 0))
        self.assertFalse(self.graph.IsEdge(0, 1))
        self.assertFalse(self.graph.IsEdge(0, 2))
        self.assertFalse(self.graph.IsEdge(0, 0))
        self.assertFalse(self.graph.IsEdge(1, 0))
        self.assertFalse(self.graph.IsEdge(2, 0))

    def testDepthFirstSearch(self):
        self.graph.AddVertex(10)
        self.graph.AddEdge(0, 0)
        path1 = self.graph.DepthFirstSearch(0, 0)
        self.assertEqual([v.Value for v in path1], [10, 10])
        self.graph.AddVertex(20)
        self.graph.AddVertex(30)
        path2 = self.graph.DepthFirstSearch(0, 2)
        self.assertEqual(path2, [])
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        path3 = self.graph.DepthFirstSearch(0, 2)
        self.assertEqual([v.Value for v in path3], [10, 30])
        path4 = self.graph.DepthFirstSearch(1, 2)
        self.assertEqual([v.Value for v in path4], [20, 10, 30])

    def testBreadthFirstSearch(self):
        self.graph.AddVertex(10)
        self.graph.AddEdge(0, 0)
        path1 = self.graph.BreadthFirstSearch(0, 0)
        self.assertEqual([v.Value for v in path1], [])
        self.graph.AddVertex(20)
        self.graph.AddVertex(30)
        path2 = self.graph.BreadthFirstSearch(0, 2)
        self.assertEqual(path2, [])
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(0, 2)
        path3 = self.graph.BreadthFirstSearch(0, 2)
        self.assertEqual([v.Value for v in path3], [10, 30])
        path4 = self.graph.BreadthFirstSearch(1, 2)
        self.assertEqual([v.Value for v in path4], [20, 10, 30])

    def testWeakVertices(self):
        weakVertices = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weakVertices], [])
        self.graph.AddVertex(10)
        self.graph.AddVertex(20)
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        weakVertices1 = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weakVertices1], [10, 20])
        self.graph.AddVertex(30)
        self.graph.AddEdge(2, 0)
        weakVertices2 = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weakVertices2], [])
        self.graph.AddVertex(40)
        self.graph.AddVertex(50)
        self.graph.AddVertex(60)
        self.graph.AddEdge(3, 4)
        weakVertices3 = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weakVertices3], [40, 50])
        self.graph = SimpleGraph(6)
        self.graph.AddVertex(70)
        self.graph.AddEdge(1, 3)
        self.graph.AddEdge(4, 1)
        weakVertices4 = self.graph.WeakVertices()
        self.assertEqual([v.Value for v in weakVertices4], [70])

if __name__ == "__main__":
    unittest.main()