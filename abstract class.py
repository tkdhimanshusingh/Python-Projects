class MyBook():
    def __init__(self,title,author,price):
        pass
    def display(self):
        print("Title:",title)
        print("Author:",author)
        print("Price:",price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
