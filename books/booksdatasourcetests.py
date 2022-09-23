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
    
    # Author tests
        
    # Checks that authors alphabetizes and generally works
    def test_if_authors_works(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        author = tiny_data_source.authors('an')
        self.assertTrue(len(author) == 3)
        self.assertTrue(author[0].authors == 'Austen', 'Jane')
        self.assertTrue(author[1].authors == 'Gaiman', 'Neil')
        self.assertTrue(author[2].authors == 'Melville', 'Herman')
        
    # Checks if authors with three names are sorted correctly
    def test_three_names(self):
        author_three_names = BooksDataSource('authorthreenames.csv')
        author = author_three_names.authors()
        self.assertTrue(len(author) == 3)
        self.assertTrue(author[0].authors == 'Bujold', 'Lois McMaster')
        self.assertTrue(author[1].authors == 'Wodehouse', 'Pelham Grenville')
        self.assertTrue(author[2].authors == 'Wodehouse', 'Pelham Grenville')
        
    # Tests if authors with the same surname are sorted correctly by given name
    def test_tie_break(self):
        author_tie_break = BooksDataSource('breakingtiesauthor.csv')
        author = author_tie_break.authors()
        self.assertTrue(len(author) == 3)
        self.assertTrue(author[0].authors == 'Wodehouse', 'Carl')
        self.assertTrue(author[1].authors == 'Wodehouse', 'Jack')
        self.assertTrue(author[2].authors == 'Wodehouse', 'Pelham')

    # Test if authors are returned in order regardless of case in search parameter
    def test_case_sensitivity(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        author = tiny_data_source.authors('AN')
        self.assertTrue(len(author) == 3)
        self.assertTrue(author[0].authors == 'Austen', 'Jane')
        self.assertTrue(author[1].authors == 'Gaiman', 'Neil')
        self.assertTrue(author[2].authors == 'Melville', 'Herman')
    
# Author
#   Check if input is a string (assert #, expect failure)
#   Done: checks if method works with assert that it equals a premade correct output csv
#   Done: alphabetize works (use smaller premade list)
#   Done: Checks if method still works w 2/3 names
#   Done: Break ties using given name
#   Done: Test if case-insensitivety works

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
