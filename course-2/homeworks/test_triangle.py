import unittest
from shape import Triangle


def is_positive(num):
	if num>0:
		return True
	else:
		False

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.test_triangle = Triangle('Triangle', 'Test Triangle', 3)
        

    def testarea_public(self):
        self.assertTrue(is_positive(self.test_triangle.area_public))

    def testperim_public(self):
        self.assertTrue(is_positive(self.test_triangle.perim_public))


    def testrope_public(self):
    	self.assertEqual(self.test_triangle.role_public, 'aggressive and prone to violence')


    def testally_public(self):
    	self.assertEqual(self.test_triangle.ally_public[0], 'Circle')

    def testenemy_public(self):
    	self.assertEqual(self.test_triangle.enemy_public[0], 'Square')






    

if __name__ == '__main__':
    unittest.main()
