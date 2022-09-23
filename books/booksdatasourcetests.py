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
        self.assertTrue(author[0] == Author('Austen', 'Jane'))
        self.assertTrue(author[1] == Author('Gaiman', 'Neil'))
        self.assertTrue(author[2] == Author('Melville', 'Herman'))
        
    # Checks if authors with three names are sorted correctly
    def test_three_names(self):
        author_three_names = BooksDataSource('authorthreenames.csv')
        author = author_three_names.authors()
        self.assertTrue(len(author) == 3)
        self.assertTrue(author[0] == Author('Bujold', 'Lois McMaster'))
        self.assertTrue(author[1] == Author('Wodehouse', 'Pelham Grenville'))
        self.assertTrue(author[2] == Author('Wodehouse', 'Pelham Grenville'))
        
    # Tests if authors with the same surname are sorted correctly by given name
    def test_tie_break(self):
        author_tie_break = BooksDataSource('breakingtiesauthor.csv')
        author = author_tie_break.authors()
        self.assertTrue(len(author) == 3)
        self.assertTrue(author[0] == Author('Wodehouse', 'Carl'))
        self.assertTrue(author[1] == Author('Wodehouse', 'Jack'))
        self.assertTrue(author[2] == Author('Wodehouse', 'Pelham'))

    # Test if authors are returned in order regardless of case in search parameter
    def test_case_sensitivity(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        author = tiny_data_source.authors('AN')
        self.assertTrue(len(author) == 3)
        self.assertTrue(author[0] == Author('Austen', 'Jane'))
        self.assertTrue(author[1] == Author('Gaiman', 'Neil'))
        self.assertTrue(author[2] == Author('Melville', 'Herman'))
    
# Author
#   Done: checks if method works with assert that it equals a premade correct output csv
#   Done: alphabetize works (use smaller premade list)
#   Done: Checks if method still works w 2/3 names
#   Done: Break ties using given name
#   Done: Test if case-insensitivety works

# Books tests

    # Checks if method sorts alphabetically by title given an empty search string
    def test_empty_search(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        titles = tiny_data_source.books()
        self.assertTrue(len(titles) == 3)
        self.assertTrue(titles[0].title == 'Emma')
        self.assertTrue(titles[1].title == 'Neverwhere')
        self.assertTrue(titles[2].title == 'Omoo')

    # Test if titles are returned in order regardless of case in search parameter
    def test_case_sensitivity(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        titles = tiny_data_source.books('M')
        self.assertTrue(len(titles) == 2)
        self.assertTrue(titles[0].title == 'Emma')
        self.assertTrue(titles[1].title == 'Omoo')

    # Test if sort_by year parameter works
    def test_case_sensitivity(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        titles = tiny_data_source.books(sort_by = 'year')
        self.assertTrue(len(titles) == 3)
        self.assertTrue(titles[0].title == 'Emma')
        self.assertTrue(titles[1].title == 'Omoo')
        self.assertTrue(titles[2].title == 'Neverwhere')

    # Test if breaking ties with title for sort_by year parameter works
    def test_case_sensitivity(self):
        breaking_ties_title = BooksDataSource('breakingtiestitle.csv')
        titles = breaking_ties_title.books(sort_by = 'year')
        self.assertTrue(len(titles) == 3)
        self.assertTrue(titles[0].title == 'Omoo')
        self.assertTrue(titles[1].title == 'Omoy')
        self.assertTrue(titles[2].title == 'Omoz')

    # Test if breaking ties with year for sort_by title parameter works
    def test_case_sensitivity(self):
        breaking_ties_year = BooksDataSource('breakingtiesyear.csv')
        year = breaking_ties_year.books(sort_by = 'title')
        self.assertTrue(len(year) == 3)
        self.assertTrue(year[0].publication_year == 1947)
        self.assertTrue(year[1].publication_year == 1948)
        self.assertTrue(year[2].publication_year == 1949)



# Books (title)
#   checks if method works with assert that it equals a premade correct output csv
#   checks if special punctuation searches match premade correct output csv
#   Given options (publication year/title) sort with respect to the chosen option
#       year (2 tests)
#       title (2 tests)
#   Test if case-insensitivity works

    # Test if user inputs switched years
    def test_switched_years(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        titles = tiny_data_source.books_between_years(start_year = 1984, end_year = 12)
        self.assertTrue(len(titles) == 0)

    # Test if user inputs the same years that it breaks ties with alphabetical
    def test_same_year(self):
        breaking_ties_title = BooksDataSource('breakingtiestitle.csv')
        titles = breaking_ties_title.books_between_years(start_year = 1847, end_year = 1847)
        self.assertTrue(titles[0].title == 'Omoo')
        self.assertTrue(titles[1].title == 'Omoy')
        self.assertTrue(titles[2].title == 'Omoz')

    # Test if books are correctly sorted between given years (also tests inclusivity)
    def test_between_years_works_general(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        titles = tiny_data_source.books_between_years(start_year = 1800, end_year = 1847)
        self.assertTrue(len(titles) == 2)
        self.assertTrue(titles[0].title == 'Emma')
        self.assertTrue(titles[1].title == 'Omoo')

    # Test if list sorts correctly with no input dates
    def test_empty_search_pb_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        years = tiny_data_source.books_between_years()
        self.assertTrue(len(years) == 3)
        self.assertTrue(years[0].publication_year == 1815)
        self.assertTrue(years[1].publication_year == 1847)
        self.assertTrue(years[2].publication_year == 1996)

    # Test if list sorts correctly with only start date
    def test_only_start_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        years = tiny_data_source.books_between_years(start_year = 1820)
        self.assertTrue(len(years) == 2)
        self.assertTrue(years[0].publication_year == 1847)
        self.assertTrue(years[1].publication_year == 1996)

    # Test if list sorts correctly with only end date
    def test_only_end_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        years = tiny_data_source.books_between_years(end_year = 1950)
        self.assertTrue(len(years) == 2)
        self.assertTrue(years[0].publication_year == 1815)
        self.assertTrue(years[1].publication_year == 1847)

# Books_between_years
#   start year end year correctly inputed switched years
#   If start and end years the same check if it matches premade correct output csv
#   checks if method works with assert that it equals a premade correct output csv

# General
#   Tests help function

if __name__ == '__main__':
    unittest.main()
