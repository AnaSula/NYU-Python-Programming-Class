import unittest
from shape import Circle


def is_positive(num):
	if num>0:
		return True
	else:
		False

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.test_circle= Circle('Circle', 'Test Circle', -2)
        

    def testarea_public(self):
        self.assertTrue(is_positive(self.test_circle.area_public))

    def testperim_public(self):
        self.assertTrue(is_positive(self.test_circle.perim_public))


    def testrope_public(self):
    	self.assertEqual(self.test_circle.role_public, 'wise and noble')


    def testally_public(self):
    	self.assertEqual(self.test_circle.ally_public[0], 'Triangle')

    def testenemy_public(self):
    	self.assertEqual(self.test_circle.enemy_public[0], 'Square')






    

if __name__ == '__main__':
    unittest.main()
