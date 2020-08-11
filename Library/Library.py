import datetime


class Library:
    books_available = ["Black", "Iron Man", "Captain America", "Wembra", "Animals",
                       "Sky History", "quarantine", "Viruses", "Biology", "Physics"]
    lend_item_list = {}

    @staticmethod
    def display_books():
        print('Books List:', *Library.books_available, sep='\n- ')


def lend_book():
    print("Please Enter Your Name:")
    user_name = str(input())
    lend_book_input = str(input("Please Tell The Name of Book: \n"))
    if lend_book_input in Library.lend_item_list:
        print(f"Sorry The Book {lend_book_input} is reserved by {Library.lend_item_list.get(lend_book_input)}")
        main()
    if lend_book_input in Library.books_available:
        Library.lend_item_list.__setitem__(lend_book_input, user_name)
        f = open("Book_Reservation", "a")
        f.write(f"The Book {lend_book_input} is Given To {user_name} on {datetime.datetime.today()}")
        f.close()
        print("Okay The Book Is Given To You")
    else:
        print("The Book Is Not Available")


def donate_book():
    donate_user = str(input("Please Enter Your Name:\n"))
    donated_book = str(input("Please Enter The Book Name:\n"))
    if donated_book not in Library.books_available:
        Library.books_available.append(donated_book)
        a = open("donating book", "w")
        a.write(f"The Book {donated_book} is donated by {donate_user} on {datetime.datetime.today()}")
        a.close()
        print("Thanks For Donating The Book")
    else:
        print("The Book Is Already Available in The Catalog")

def return_book():
    print("Please tell the name of the book")
    return_user = str(input())
    if return_user in Library.lend_item_list:
        Library.lend_item_list.pop(return_user)
        print("Thanks you have successfully returned the book")
        a = open("return.txt","w")
        a.write(f"The book {return_user} is returned at {datetime.datetime.today()}")
        a.close()
    else:
        print("The Book IS not Reserved")

def main():
    if __name__ == '__main__':
        i = 1
        while i > 0:
            print("Welcome To The Grand Library \nPlease Enter The Commands To Continue")
            man_input = str(input())
            if man_input == "show books":
                Library.display_books()

            elif man_input == "borrow book":
                lend_book()

            elif man_input == "return book":
                return_book()

            elif man_input == "donate book":
                donate_book()
            else:
                print("Please Enter Correct Command")


main()

