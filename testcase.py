import unittest

class Base94EncodeDecodeTestCase(unittest.TestCase):
	def test_base94_encode(self):
		self.assertEqual((94),'~')
		self.assertEqual((1),'!')
	def test_base94_decode(self):
		self.assertEqual('!',1)
		self.assertEqual(('*S|'),93246)


if __name__ == '__main__':
	unittest.main()
