'''
   booksdatasourcetest.py
   Jeff Ondich, 24 September 2021
   Modified by Alex Falk and Carl Zhang, 21 September 2022
'''

from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

# Author
#   Check if input is a string (assert #, expect failure)
#   checks if method works with assert that it equals a premade correct output csv
#   alphabetize works (use smaller premade list)
#   Checks if method still works w 2/3 names
#   Check empty result

# Books (title)
#   Check if input is a string (assert #, expect failure)
#   checks if method works with assert that it equals a premade correct output csv
#   checks if special punctuation searches match premade correct output csv
#   Check empty result
#   Given options (publication year/title) sort with respect to the chosen option

# Books_between_years
#   Check if input are numbers (assert number, expect failure)
#   start year end year correctly inputed switched years
#   If start and end years the same check if it matches premade correct output csv
#   checks if method works with assert that it equals a premade correct output csv
#   Check empty result

# General
#   Tests help function

if __name__ == '__main__':
    unittest.main()