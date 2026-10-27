# Library Borrowing and Fine Reconciliation

# (Book ID, Borrowing Days, Return Delay Days)
records = [
    ("B101", 7, 0),
    ("B102", 10, 3),
    ("B103", 5, 2),
    ("B104", 8, 0)
]

fine_per_day = 5
borrowed_books = []

for book_id, days, delay in records:
    fine = delay * fine_per_day

    print("\nBook ID:", book_id)
    print("Borrowing Days:", days)
    print("Return Delay:", delay, "days")
    print("Fine: Rs.", fine)

    if delay > 0:
        print("Status: Overdue")
    else:
        print("Status: Returned on time")

    borrowed_books.append(book_id)

# Reconcile book availability
print("\n--- Book Availability ---")

all_books = ["B101", "B102", "B103", "B104", "B105"]

for book in all_books:
    if book in borrowed_books:
        print(book, "- Borrowing record found")
    else:
        print(book, "- Available")

total_fine = sum(record[2] * fine_per_day for record in records)
print("\nTotal Fine: Rs.", total_fine)
