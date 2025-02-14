
import unittest

from simpleGraph import SimpleGraph

class TestsSimpleGraph(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(3)

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


if __name__ == "__main__":
    unittest.main()