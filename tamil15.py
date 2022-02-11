#data abstraction and data encapsulation in python
#data abstraction-->shows only the outside view (not the background works)
#                -->BLUEPRINT
#data encapsulation-->it is enclosed with data and code (shows  the entire things)
#                  -->ALL STORED VIEWS
 
class library:
    def __init__(self,books):
        self.books=books

    def listed_books(self):
        print("available books:")
        for books in self.books:
            print (books)

    def borrow_book(self,borrow_book):
        if  borrow_book in self.books:
            print("GET YOUR BOOK!")
            self.books.remove(borrow_book)
        else:
            print("OOPS!BOOK IS NOT AVAILABLE!")

    def recieved_book(self,received_book):
        print("YOU HAVE RECIEVE THE BOOK:) !")
        self.books.append(received_book)

a=['java','python','c++','c']

o=library(a)

b='''
   1.listed books
   2.borrowed books
   3.received books
'''
while True:
    print(b)
    books=int(input("enter your choice of the book : "))
    if books==1:
        o.listed_books()
    elif books==2:
        books=input("enter your book name to borrow: ")
        o.borrow_book(books)
    elif books==3:
         books=input("enter your book name to recieve: ")
         o.recieved_book(books)
    else:
        print("THANK YOU FOR COMING :) !")
        quit()


        







