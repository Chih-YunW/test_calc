import unittest
import calc

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calc.add(1,3), 4)
	def test_edge_case_add(self):
                self.assertEqual(calc.add(0,0), 0)
	def test_type_add(self):
		self.assertRaises(TypeError, calc.add, 'dog', 2)
class testCaseSub(unittest.TestCase):
        def test_sub(self):
                self.assertEqual(calc.sub(5,3), 2)
        def test_edge_case_sub(self):
                self.assertEqual(calc.sub(1,5), -4)
        def test_type_sub(self):
                self.assertRaises(TypeError, calc.sub, 'dog', 2)


if __name__ == '__main__':
	unittest.main()
