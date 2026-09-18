class Books:
    #Note: The __init__() method is called automatically every time the class is being used to create a new object. 
    title=""
    author=""
    genre=""
    def __init__(self,title,author,genre,):
        self.title=title
        self.author=author
        self.genre=genre
        self.num_pages=230
    
    #methods
    def num_page(self):
        print(f"this book name is {self.title} has {self.num_pages} pages.")
    def describing_book(self):
        print(f"{self.title} by {self.author}, genre:{self.genre}")
    def read_book(self):
        print(f"Reading {self.title} by {self.author}")
    def __str__(self):
        print(f"Book Object: Title{self.title},Author{self.author}")
        
        
book = Books("saket mishra","yash mishra","both are greate man")

print(book.num_page())
