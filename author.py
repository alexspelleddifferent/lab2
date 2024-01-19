class Author:
    #define a class with a name of an author and the books they have written
    #also has functions for how to print the object and how to add published books
    def __init__(self, name):
        self.name=name
        self.books=[]

    #makes a string out of the data in the class
    def __str__(self):
        final_string=f'Author name: {self.name}, their books:'
        for book in self.books:
            if self.books[-1]==book:
                final_string+=f' {book}.'
            else:
                final_string+=f' {book},'
        return final_string

    #adding new books to the class
    def publish(self, book):
        if book in self.books:
            print("Duplicate book")
            return
        else:
            self.books.append(book)

def main():
    me=Author("Alex") 
    me.publish("my first book")
    me.publish("my second book")
    me.publish("my last book")
    me.publish("my first book")
    print(me)

    you=Author("Clara")
    you.publish("How to teach python")
    you.publish("How to teach java")
    you.publish("How to teach android")
    you.publish("How to teach python")
    print(you)

if __name__=="__main__":
    main()