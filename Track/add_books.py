from save_all_books import save_all_books

def add_books(all_books):
    name = input("Enter the Name :  ")
    email = input("Enter Your Email : ").strip()
    number = input("Enter Your Phone Number : ").strip()
    address = input("Enter Your Address : ").strip()
    


    book = {
        "name" : name,
        "email" : email,
        "number" : number,
        "address" : address,
        
    }

    all_books.append(book)
    save_all_books(all_books)

    print("Books Added Successully")
    return all_books





