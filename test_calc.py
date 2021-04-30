import unittest
import calc

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calc.add(1,3), 4)
	def test_edge_case_add(self):
                self.assertEqual(calc.add(0,0), 0)
	def test_fail_type_add(self):
		self.assertEqual(calc.add("dog", 3), 3)
class testCaseSub(unittest.TestCase):
        def test_sub(self):
                self.assertEqual(calc.sub(5,3), 2)
        def test_edge_case_sub(self):
                self.assertEqual(calc.sub(1,5), -4)
        def test_fail_type_sub(self):
                self.assertEqual(calc.sub("dog", 3), 3)
class testCaseMul(unittest.TestCase):
        def test_mul(self):
                self.assertEqual(calc.mul(5,3), 15)
        def test_edge_case_mul(self):
                self.assertEqual(calc.mul(1,0), 0)
        def test_fail_type_mul(self):
                self.IsInstance(calc.mul("dog", 5), (int, float))
class testCaseDiv(unittest.TestCase):
        def test_div(self):
                self.assertEqual(calc.div(15,3), 5)
        def test_edge_case_div(self):
                self.assertEqual(calc.div(-1,-1), 1)
        def test_fail_div_by_zero(self):
                self.assertEqual(calc.div(15, 0), 0)

if __name__ == '__main__':
	unittest.main()
