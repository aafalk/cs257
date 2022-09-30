'''
    books.py
    Alex Falk and Carl Zhang, 29 September 2022
    CS 257 Software Design class, Fall 2022.
'''

import sys
import booksdatasource
#from booksdatasource import BooksDataSource

#if system inputted arguments too little
if len(sys.argv) < 2:
    sys.exit('wrong number of arguments, check help')
else:
    subcommand = sys.argv[1]

if subcommand == 'author':
    print('Searching for authors\n')
    data_source = booksdatasource.BooksDataSource('books1.csv')

    #no search text
    if (len(sys.argv) == 2):
        authors = data_source.authors()

    #search text specified
    elif (len(sys.argv) == 3):
        search_text = sys.argv[2]
        authors = data_source.authors(search_text)
    
    #throw error wrong number of arguments
    else:
        sys.exit('wrong number of arguments, check help')
    data_source.print_authors(authors)

elif subcommand == 'title':
    print('Searching for books\n')
    data_source = booksdatasource.BooksDataSource('books1.csv')

    #no search text
    if (len(sys.argv) == 2):
        books = data_source.books()

    #search text specified
    elif (len(sys.argv) == 3):
        if sys.argv[2].isalpha():
            search_text = sys.argv[2]
            books = data_source.books(search_text)
        else:
            #search text is not appropriate
            sys.exit('search text argument is not a character string')
    elif (len(sys.argv) == 4):
        search_text = sys.argv[2]
        sort_by = sys.argv[3]
        if sort_by == 'title':
            books = data_source.books(search_text, 'title')
        elif sort_by == 'year':
            books = data_source.books(search_text, 'year')
        else:
            sys.exit('wrong sort by argument for title search, check help')
    #throw error wrong number of arguments
    else:
        sys.exit('wrong number of arguments, check help')
    data_source.print_books(books)

elif subcommand == 'year':
    print('Searching by year\n')
    data_source = booksdatasource.BooksDataSource('books1.csv')
    if (len(sys.argv) != 4):
        sys.exit('wrong number of arguments, check help')
    
    #no years specified
    elif (sys.argv[2] == '-' and sys.argv[3] == '-'):
        books = data_source.books_between_years()
    #if start year is not specified
    elif (sys.argv[2] == '-'):
        books = data_source.books_between_years(end_year = sys.argv[3])
    #if end year is not specified
    elif (sys.argv[3] == '-'):
        books = data_source.books_between_years(start_year = sys.argv[2])
    #throws error if start or end year is not an integer
    elif (not float(sys.argv[2]).is_integer() or not float(sys.argv[3]).is_integer()):
        sys.exit('wrong between years input, check help')
    else:
        #if both years specified
        books = data_source.books_between_years(start_year = sys.argv[2], end_year = sys.argv[3])
    data_source.print_books(books)
    
#help subcommandx
elif subcommand == '-h' or subcommand == 'help':
    with open('usage.txt', 'r') as f:
        print(f.read())
else:
    print('Uh-oh')
