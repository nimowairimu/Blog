import unittest
from models import Quote
Quote = quote.Quote

class QuoteTest(unittest.TestCase):

    def setUp(self):
        '''
        set up method that rruns before each test
        '''
        self.new_quote = Quote('Jeremy','34','You got this')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_quote,Quote))

if __name__ == '__main__':
    unittest.main()