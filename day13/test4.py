import unittest

from damo.demo import counter

class TestCale1(unittest.TestCase):

    def testdivide(self):
        c = counter()

        a = 9
        b = 9
        d = 1
        sum = c.divide(a, b)
        self.assertEquals(d, sum)

    def testdivide1(self):
        c = counter()

        a = -9
        b = 9
        d = -1
        sum = c.divide(a, b)
        self.assertEquals(d, sum)

    def testdivide2(self):
        c = counter()

        a = 9
        b = -9
        d = -1
        sum = c.divide(a, b)
        self.assertEquals(d, sum)

    def testdivide3(self):
        c = counter()

        a = -9
        b = -9
        d = 1
        sum = c.divide(a, b)
        self.assertEquals(d, sum)