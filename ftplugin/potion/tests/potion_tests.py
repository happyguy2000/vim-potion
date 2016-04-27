import unittest
import potion as sut


@unittest.skip("Don't forget to test!")
class PotionTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.potion_example()
        self.assertEqual("Happy Hacking", result)
