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
    
    def test_valid_author_input(self):
        Execution
        
        Validation
        
    # Checks that authors alphabetizes and generally works
    def test_if_authors_works:
        tiny_data_source = BooksDataSource('tinybooks.csv')
        author = tiny_data_source.authors('an')
        self.assertTrue(len(author) == 3)
        self.assertTrue(author[0].authors == 'Austen', 'Jane')
        self.assertTrue(author[1].authors == 'Gaiman', 'Neil')
        self.assertTrue(author[2].authors == 'Melville', 'Herman')
        
    def test_three_names:
        author_three_names = BooksDataSource('authorthreenames.csv')
        author = author_three_names.authors()
        self.assertTrue(len(author) == 3)
        self.assertTrue(author[0].authors == 'Bujold', 'Lois McMaster')
        self.assertTrue(author[1].authors == 'Wodehouse', 'Pelham Grenville')
        self.assertTrue(author[2].authors == 'Wodehouse', 'Pelham Grenville')
        
    

    
# Author
#   Check if input is a string (assert #, expect failure)
#   Done: checks if method works with assert that it equals a premade correct output csv
#   Done: alphabetize works (use smaller premade list)
#   Done: Checks if method still works w 2/3 names
#   Break ties using given name

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
