import unittest
from BBST import GenerateBBSTArray


class GenerateBBSTArrayTests(unittest.TestCase):

    def testGenerateBBSTArray(self):
        self.assertEqual(GenerateBBSTArray([]), [])
        self.assertEqual(GenerateBBSTArray([1]), [1])
        self.assertEqual(GenerateBBSTArray([2, 5]), [5, 2])
        self.assertEqual(GenerateBBSTArray([10, 20, 4, 3, 6, 5, 11]), GenerateBBSTArray([6, 4, 11, 3, 5, 10, 20]))
        self.assertEqual(GenerateBBSTArray([5, 6, 7, 8, 9, 10, 11]), GenerateBBSTArray([8, 6, 10, 5, 7, 9, 11]))
        self.assertEqual(GenerateBBSTArray([11, 10, 9, 8, 7, 6, 5]), GenerateBBSTArray([8, 6, 10, 5, 7, 9, 11]))


if __name__ == "__main__":
    unittest.main()