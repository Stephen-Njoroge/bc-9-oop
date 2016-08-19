import unittest
from Simple_Library import NotesApplication


class NotesApplicationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
    	cls.juma = NotesApplication("Juma")

    def test_init_author(self):
    	self.assertIsInstance(self.juma, NotesApplication)
    	self.assertIsInstance(self.juma, NotesApplication)

    def test_if_within(self):
    	x = NotesApplication("NJ0RO")	
    	x.create('ONE')  
    	self.assertIn('ONE', x.list())

if __name__ == '__main__':
    unittest.main()