def isbn_dictionary(filename):
    
    book_dict = {}
    
    try: 
        with open(filename, mode='r', encoding='utf-8') as file:
            for line in file:
                if not line.isspace():
                    striped_line = line.strip()
                    
                    author, title, isbn = striped_line.split(',')
                    
                    book_dict[isbn] = (author, title)
                    
                    
            return book_dict
    except FileNotFoundError as e:
        print(f"The file {filename} was not found.")
        
    

your_dict = isbn_dictionary('books.csv')
if your_dict != None:
    for isbn in sorted(your_dict.keys()):
        print(isbn + ':', your_dict[isbn])
        
         
your_dict = isbn_dictionary('loads_of_books.csv')
if your_dict != None:
    for isbn in sorted(your_dict.keys()):
        print(isbn + ':', your_dict[isbn])