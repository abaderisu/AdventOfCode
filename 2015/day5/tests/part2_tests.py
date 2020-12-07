import unittest
from part2 import count_nice_strings

class Part2Tests(unittest.TestCase):
    def test(self):
        self.assertEqual( 1, count_nice_strings(['xyxy']) )
        self.assertEqual( 0, count_nice_strings(['aaa']) )
        self.assertEqual( 1, count_nice_strings(['qjhvhtzxzqqjkmpb']))
        self.assertEqual( 1, count_nice_strings(['xxyxx']))
        self.assertEqual( 0, count_nice_strings(['uurcxstgmygtbstg']))
        self.assertEqual( 0, count_nice_strings(['ieodomkazucvgmuy']))
