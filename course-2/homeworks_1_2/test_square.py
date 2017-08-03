import unittest
from shape import Square


def is_positive(num):
	if num>0:
		return True
	else:
		False

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.test_square = Square('Square', 'Test Square', 3)
        

    def testarea_public(self):
        self.assertTrue(is_positive(self.test_square.area_public))

    def testperim_public(self):
        self.assertTrue(is_positive(self.test_square.perim_public))


    def testrope_public(self):
    	self.assertEqual(self.test_square.role_public, 'complacent and bureaucratic')


    def testally_public(self):
    	self.assertEqual(self.test_square.ally_public[0], 'None')

    def testenemy_public(self):
    	self.assertEqual(self.test_square.enemy_public[0], 'Triangle, Circle')






    

if __name__ == '__main__':
    unittest.main()
