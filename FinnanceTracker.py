
# Input: Users will input transactions, including the amount, category, 
# and description. They may also input commands to generate reports 
# or perform other actions within the application.

# Output: The application will display information about the user's 
# finances, such as a list of transactions, summary statistics 
# (e.g., total income, total expenses), and 
# reports (e.g., spending by category, monthly expenses).

class tracker:
    def __init__(self,amount,cat,dec):
        self.amount=amount
        self.cat=cat
        self.dec=dec

class finapp:
    def __init__(self):
        self.books=[]
    
    def add_transaction(self,amount,cat,dec):
        book=tracker(amount,cat,dec)
        self.books.append(book)
    
    def view_transaction(self):
        for idx,books in enumerate(self.books,start=1):
            print(f"{idx},{books.amount},{books.cat},{books.dec}")
        



app=finapp()

# app.add_transation(100,'timepas','movie')

# app.view_transaction()


def main():
    while True
        print("1. add expense \n2. view expense. \n3. Quit :")
        n=input("selct below option :")
        if n == '1':
            print("add expense :")
            amount=input("enter the amout :")
            catagory=input("enter the catagory :")
            reason=input("Enter the reason :")
            app.add_transaction(amount,catagory,reason)

        if n =='2':
            print("Look at the expens--->")
            app.view_transaction()

        if n == '3':
            print("Good Bye")
            break

if __name__ == '__main__':
    main()
