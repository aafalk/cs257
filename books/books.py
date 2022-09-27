'''
    python3 books.py author search_text
    python3 books.py title search_text [-t, -p]
    python3 books.py year A B
    python3 books.py [-h --help]

    Plan
    - Create a simple command-line parsing with stubs
    - For each stub, what do I need BooksDataSource to do
        make it do that
        call it from books.py
    - [could be helpful] make sure your booksdatasourcetests.py works
    
    Things to learn
    - How to do command-line parsing
    - How to deal with a CSV file
    - How to put a multi-file multi-class thing together
'''

import sys
import booksdatasource
#from booksdatasource import BooksDataSource

#print(sys.argv)
subcommand = sys.argv[1]
if subcommand == 'author':
    search_text = sys.argv[2]
    print('Searching for authors')
elif subcommand == 'title':
    search_text = sys.argv[2]
    data_source = booksdatasource.BooksDataSource('books1.csv')
    books = data_source.books(search_text)
#    data_source = BooksDataSource('books1.csv')
    print('Searching for books')
elif subcommand == 'year':
    start_year = int(sys.argv[2])
    end_year = int(sys.argv[3])
    print('Searching by year')
else:
    print('Uh-oh')
