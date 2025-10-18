# Task 1: Library Management System with Custom Exceptions

# Custom Exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

# Member class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")

# Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = self.find_book(book_title)
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = self.find_book(book_title)
        if member:
            member.return_book(book)

# Testing
try:
    library = Library()

    # Add books
    b1 = Book("1984", "George Orwell")
    b2 = Book("The Hobbit", "J.R.R. Tolkien")
    library.add_book(b1)
    library.add_book(b2)

    # Add members
    m1 = Member("Alice")
    m2 = Member("Bob")
    library.add_member(m1)
    library.add_member(m2)

    # Borrow and return
    library.borrow_book("Alice", "1984")
    library.return_book("Alice", "1984")

    # Trigger exceptions
    library.borrow_book("Bob", "Unknown Book")  # BookNotFoundException

except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print("Error:", e)

# Task 2: Student Grades Management
import csv

# Step 1: Create the grades.csv file
grades_data = [
    ["Name", "Subject", "Grade"],
    ["Alice", "Math", 85],
    ["Bob", "Science", 78],
    ["Carol", "Math", 92],
    ["Dave", "History", 74]
]

with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(grades_data)

# Step 2: Read data from grades.csv
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Step 3: Calculate average grades
subject_grades = {}
for row in data:
    subject = row["Subject"]
    grade = int(row["Grade"])
    if subject not in subject_grades:
        subject_grades[subject] = []
    subject_grades[subject].append(grade)

average_grades = {sub: sum(grades)/len(grades) for sub, grades in subject_grades.items()}

# Step 4: Write average_grades.csv
with open("average_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in average_grades.items():
        writer.writerow([subject, round(avg, 2)])

print("average_grades.csv created successfully!")

# Task 3: JSON Handling
import json
import csv

# Step 1: Create tasks.json
tasks_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

with open("tasks.json", "w") as file:
    json.dump(tasks_data, file, indent=4)

# Step 2: Load tasks from JSON
with open("tasks.json", "r") as file:
    tasks = json.load(file)

# Display all tasks
print("\nAll Tasks:")
for t in tasks:
    print(f"ID: {t['id']} | Task: {t['task']} | Completed: {t['completed']} | Priority: {t['priority']}")

# Step 3: Calculate stats
def calculate_stats(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    avg_priority = sum(t["priority"] for t in tasks) / total
    return total, completed, pending, avg_priority

total, completed, pending, avg_priority = calculate_stats(tasks)
print("\n Task Statistics:")
print(f"Total Tasks: {total}")
print(f"Completed: {completed}")
print(f"Pending: {pending}")
print(f"Average Priority: {avg_priority:.2f}")

# Step 4: Convert JSON to CSV
with open("tasks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Task", "Completed", "Priority"])
    for t in tasks:
        writer.writerow([t["id"], t["task"], t["completed"], t["priority"]])

print("\n tasks.csv created successfully!")
