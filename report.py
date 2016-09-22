import unittest
from io import StringIO
import HTMLTestRunner
import os
from decorator import SearchTest
from suit import HomePageTest

dir= os.getcwd()
search_test= unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_test= unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

smoke_test= unittest.TestSuite([home_page_test, search_test])
outfile = open(os.path.join(dir, "TestResult.html"), "wb")
runner=HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='test report',
    description='Smoke tests'
)

runner.run(smoke_test)