
class BookStore:

    NoOfBooks = 0
    
    def __init__(self,BookName,BookAuthor):
        self.name = BookName
        self.author = BookAuthor
        BookStore.NoOfBooks += 1

    def Display(self):
        print("BookName is : ",self.name,", BookAuthor is : ",self.author,", Total Number of Books are : ",self.NoOfBooks)       

    
def main():

    obj1 = BookStore("Linux System Programming","Robert Love")
    obj2 = BookStore("C Programming","Dennis Ritchie")
    obj3 = BookStore("C++ Programming","C++ Creator")
    
    obj1.Display()

    obj2.Display()

    obj3.Display()
    

if __name__ == "__main__":
    main()