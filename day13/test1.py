import unittest

from damo.demo import counter

class TestCale1(unittest.TestCase):

    def testinpary(self):
        c = counter()

        a = 9
        b = 8
        d = 1
        sum = c.inpary(a, b)
        self.assertEquals(d, sum)

    def testinpary1(self):
        c = counter()

        a = -9
        b = 8
        d = -17
        sum = c.inpary(a, b)
        self.assertEquals(d, sum)

    def testinpary2(self):
        c = counter()

        a = 9
        b = -8
        d = 17
        sum = c.inpary(a, b)
        self.assertEquals(d, sum)

    def testinpary3(self):
        c = counter()

        a = -9
        b = -8
        d = -1
        sum = c.inpary(a, b)
        self.assertEquals(d, sum)