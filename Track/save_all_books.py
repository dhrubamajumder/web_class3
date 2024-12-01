

def save_all_books(all_books):
    with open("all_books.csv", "w") as fp:
        for book in all_books:
            line = f'{book['name']}, {book['email']}, {book['number']}, {book['address']}\n'
            fp.write(line)


