import unittest
import cube

class TestCase(unittest.TestCase):
	def test_volume(self):
		result = cube.calcCubeVol(3, 4, 2)
		self.assertEqual(result, 24)

		result = cube.calcCubeVol(1.5, 4, 2)
		self.assertEqual(result, 12)
		
		with self.assertRaises(ValueError):
			cube.calcCubeVol(-3, 1.5, 0)
		
		with self.assertRaises(ValueError):
			cube.calcCubeVol(4, 1.5, "hello")
		
		return
