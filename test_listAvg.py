import unittest
import listAvg

class TestCase(unittest.TestCase):
	def test_volume(self):
		result = listAvg.averageList([1, 6, 7, 1, 0])
		self.assertEqual(result, 3)

		result = listAvg.averageList([-1, 6.5, 7, 8, 0.25])
		self.assertEqual(result, 4.15)

		with self.assertRaises(ValueError):
			listAvg.averageList([])
		
		with self.assertRaises(ValueError):
			listAvg.averageList("hello")
		
		with self.assertRaises(TypeError):
			listAvg.averageList(["hello", 5])
		
		return
