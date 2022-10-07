#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022
    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''
import csv

#importing packages to help with sorting(attrgetter used in line 213)
from operator import itemgetter, attrgetter

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

    #Book Representation to help with sorting
    def __repr__(self):
        return repr((self.title, self.publication_year, self.authors))

    # def __lt__(self, other):
    #     if self.title < other.title:
    #         return True
    #     if self.publication_year < other.publication_year:
    #         return True
    #     if self.title == other.title and self.publication_year < other.publication_year:
    #         return True
    #     if self.publication_year == other.publication_year and self.title < other.title:
    #         return True
    #     return False

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
        #temp book list (output)
        self.book_list = []
        self.csv_file_name = books_csv_file_name

        #iterating through csv by line
        with open(self.csv_file_name) as f:
            for line in f:
                #temp author list for each book object
                author_list = []
                #book attributes in each line delimitted by commas
                book_fields = line.rsplit(',',2)
                #setting book attributes to variables
                title = book_fields[0].strip('"')
                publication_year = book_fields[1]
                #for multiple authors splitting them up
                author_fields = book_fields[2].split(' and ')
                #iterating through split up authors
                for i in author_fields:
                    #author attributes delimitted by commas
                    author_string = i.rsplit(' ',2)
                    #setting book attributes to variables
                    given_name = author_string[0]
                    surname = author_string[1]
                    year = author_string[2].split('-')
                    birth_year = year[0].strip('(')
                    death_year = year[1].strip(')\n')
                    #creating author object with the variables
                    author = Author(surname, given_name, birth_year, death_year)
                    #appending authors to temp authors list
                    author_list.append(author)
                #creating book object with title and pub year variables and list of author(s)
                book = Book(title, publication_year, author_list)
                #appending book object to outputted bok list
                self.book_list.append(book)

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        #temp author list (output)
        author_output = []

        #iterating through books accessing the authors list attribute in book object and searching for matching authors
        for book in self.book_list:
            for author in book.authors:
                if search_text != None:
                    if author.surname.upper().__contains__(search_text.upper()) or author.given_name.upper().__contains__(search_text.upper()):
                        #making sure that the author added isn't already in the list. Allows for list outputed to have no duplicates
                        if author not in author_output:
                            author_output.append(author)
                else:
                    if author not in author_output:
                        author_output.append(author)

        return sorted(author_output)

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
        #temp books list (output)
        book_output = []

        #searches matching book titles with search text
        if search_text != None:
            for x in self.book_list:
                if x.title.upper().__contains__(search_text.upper()):
                    book_output.append(x)
        else:
            book_output = self.book_list

        #sorting by specified sorting method
        if sort_by == 'title':
            book_output = sorted(book_output,key=lambda book: book.title)
        elif sort_by == 'year':
            book_output = sorted(book_output,key=lambda book: book.publication_year)
        else:
            #error if sorting method is not within given options
            sys.exit('Not a valid sorting specification')

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
        #temp book list (output)
        bookbtw_output = []

        #covers all options for start year end year inputs
        if start_year != None and end_year != None:
            for book in self.book_list:
                if int(book.publication_year) >= int(start_year) and int(book.publication_year) <= int(end_year):
                    bookbtw_output.append(book)
        elif start_year == None and end_year != None:
            for book in self.book_list:
                if int(book.publication_year) <= int(end_year):
                    bookbtw_output.append(book)
        elif end_year == None and start_year != None:
            for book in self.book_list:
                if int(book.publication_year) >= int(start_year):
                    bookbtw_output.append(book)
        else:
            bookbtw_output = self.book_list

        #returns sorted list with attrgetter method (imported method)
        return sorted(bookbtw_output, key=attrgetter('publication_year', 'title'))