import unittest

from damo.demo import counter

class TestCale1(unittest.TestCase):

    def testride(self):
        c = counter()

        a = 9
        b = 8
        d = 72
        sum = c.ride(a, b)
        self.assertEquals(d, sum)

    def testride1(self):
        c = counter()

        a = -9
        b = 8
        d = -72
        sum = c.ride(a, b)
        self.assertEquals(d, sum)

    def testinpary2(self):
        c = counter()

        a = 9
        b = -8
        d = -72
        sum = c.ride(a, b)
        self.assertEquals(d, sum)

    def testride3(self):
        c = counter()

        a = -9
        b = -8
        d = 72
        sum = c.ride(a, b)
        self.assertEquals(d, sum)