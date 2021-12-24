class Bank:
    def __init__(self, year_percents):
        self.year_percents = year_percents


    def deposit(self, deposit):
        profit = deposit.amount * ((1 + ((self.year_percents / 100) / 12))
                                   ** (12 * deposit.term))
        print(round(profit, 3))


class Deposit:
    def __init__(self, amount, term):
        self.amount = amount
        self.term = term  # in years


alfabank = Bank(10)
free_cash = Deposit(1000, 1)
alfabank.deposit(free_cash)
priorbank = Bank(5)
priorbank.deposit(free_cash)


###

class Book:
    flag = 0  # 0: free, 1: reserved, 2: taken by some Client
    reserved_by = ''
    taken_by = ''

    def __init__(self, title, author, isbn, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn


class Client:
    def __init__(self, name):
        self.name = name

    def reservation(self, book):
        if book.flag == 1:
            if book.reserved_by != self.name:
                print('This book is already reserved')
            else:
                print('You have already reserved this book')
        elif book.flag == 2:
            if book.taken_by != self.name:
                print('Someone has already taken this book')
            else:
                print('You have already taken this book')
        else:
            book.flag = 1
            book.reserved_by = self.name


    def take_book(self, book):
        if book.flag == 0:
            book.flag = 2
            book.taken_by = self.name
            book.reserved_by = ''
        elif book.flag == 1:
            if book.reserved_by != self.name:
                print('This book is already reserved')
            else:
                book.flag = 2
                book.taken_by = self.name
                book.reserved_by = ''
        elif book.flag == 2:
            if book.taken_by != self.name:
                print('Someone has already taken this book')
            else:
                print('You have already taken this book')


war_and_peace = Book(title='War and peace',
                     author='Lev Tolstoy',
                     pages=5000,
                     isbn='978-5-389-06256-6')
alex = Client('Alex')
bob = Client('Bob')
alex.reservation(war_and_peace)
alex.take_book(war_and_peace)
alex.take_book(war_and_peace)
