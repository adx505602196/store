import unittest

from damo.demo import counter

class TestCale(unittest.TestCase):

    def testAdd(self):
        c = counter()

        a = 9
        b = 8
        d = 17
        sum = c.add(a,b)
        self.assertEquals(d,sum)

    def testAdd1(self):
        c = counter()

        a = 9
        b = -8
        d = 1
        sum = c.add(a, b)
        self.assertEquals(d, sum)


    def testAdd2(self):
        c = counter()

        a = -9
        b = 8
        d = -1
        sum = c.add(a,b)
        self.assertEquals(d,sum)

    def testAdd3(self):
        c = counter()

        a = -9
        b = -8
        d = -17
        sum = c.add(a,b)
        self.assertEquals(d,sum)


