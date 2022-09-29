#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022
    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''
import csv

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

    def __lt__(self, other):
        if self.surname < other.surname:
            return True
        if self.surname == other.surname and self.given_name < other.given_name:
            return True
        return False
    # For sorting authors, you could add a "def __lt__(self, other)" method
    # to go along with __eq__ to enable you to use the built-in "sorted" function
    # to sort a list of Author objects.

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

##FUCKING FIX SORT BY SPECIFIED
    def __lt__(self, other):
        print('entered __lt__')
        print(sort_by)
        if self.title < other.title:
            return True
        return False

    # For sorting books, you could add a "def __lt__(self, other)" method
    # to go along with __eq__ to enable you to use the built-in "sorted" function
    # to sort a list of Book objects.

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:
                title,publication_year,author_description
            For example:
                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)
            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
        print('Hi from BooksDataSource.__init__')
        self.book_list = []
        self.csv_file_name = books_csv_file_name
        with open(self.csv_file_name) as f:
            for line in f:
                book_fields = line.rsplit(',',2)
                title = book_fields[0]
                publication_year = book_fields[1]
                author = book_fields[2]
                book = Book(title, publication_year)
                self.book_list.append(book)

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        print(self.books[2].publication_year)
        return []

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.
            The list of books is sorted in an order depending on the sort_by parameter:
                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        print('in books')
        book_output = []
        #not case insensitive yet
        for x in self.book_list:
            if x.title.__contains__(search_text):
                book_output.append(x)
        
        #sorting
        

        return book_output

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).
            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''
        return []

if __name__ == '__main__':
    # Experimental test code as needed. In this case, I'm checking to see
    # whether my __lt__ and __eq__ methods in class Author are up to the job of
    # sorting a list of Author objects. Turns out, yes. Run this code by just
    # typing "python3 booksdatasource.py" at the command line.
    authors = [Author("Ondich", "Jeff Wilbert"),
                Author("Ondich", "Jeff Dilbert"),
               Author("Rafferty", "Anna"),
               Author("Oesper", "Layla"),
               Author("Ondich", "Elena")]
    
    for author in sorted(authors ):
        print(author.given_name, author.surname)

    books = [Book('p'),
            ]