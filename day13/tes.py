from damo.test import TestCale
from damo.test1 import TestCale1
from HTMLTestRunner import HTMLTestRunner
import os
import unittest

suite = unittest.TestSuite()
'''
suite.addTest(TestCale("testAdd"))
suite.addTest(TestCale("testAdd1"))
suite.addTest(TestCale("testAdd2"))
suite.addTest(TestCale("testAdd3"))
suite.addTest(TestCale1("testinpary"))
suite.addTest(TestCale1("testinpary1"))
suite.addTest(TestCale1("testinpary2"))
suite.addTest(TestCale1("testinpary3"))
'''
test = unittest.defaultTestLoader.discover(os.getcwd(),"test*.py")
suite.addTest(test)
f = open("计算器测试报告.html","w+",encoding="utf-8")

runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    verbosity=1,
    title = "计算器测试报告"
)
runner.run(suite)






