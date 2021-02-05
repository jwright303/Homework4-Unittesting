import unittest
import fullName

class TestCase(unittest.TestCase):
	def test_volume(self):
		result = fullName.generateName("Jack", "Wilson")
		self.assertEqual(result, "Jack Wilson")

		with self.assertRaises(ValueError):
			fullName.generateName(177, 90)
		
		with self.assertRaises(TypeError):
			fullName.generateName("Jack", 90)
		
		return
