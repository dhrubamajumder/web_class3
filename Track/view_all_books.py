
def view_all_books(all_books):
    if all_books !=[]:
        for book in all_books:
            print(f"name:{book['name']}| email: {book['email']}| phone : {book['phone']}| address {book['address']}")
    
    else:
        print("No Book Found in All Books")






