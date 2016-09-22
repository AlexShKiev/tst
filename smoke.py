import unittest
from decorator import SearchTest



search_test= unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_test= unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
smoke_test= unittest.TestSuite([home_page_test, search_test])

unittest.TextTestRunner(verbosity=2).run(smoke_test)


