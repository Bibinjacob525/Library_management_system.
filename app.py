import streamlit as st     # used to build web apps in python.
import pandas as pd        # used for data manipulation and creating data frames to display data in tables
import book
import member
import borrow

from datetime import datetime

# Set the title of the app
st.title("Library Management System")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose an action",
                              ("Add Book", "View Books", "Add Member", "View Members", "Borrow Book", "Return Book"))

if option == "Add Book":
    st.subheader("Add New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    publisher = st.text_input("Publisher")
    genre = st.text_input("Genre")
    year = st.number_input("Year Published", min_value=0)
    copies = st.number_input("Number of Copies", min_value=1)

    if st.button("Add Book"):
        book.add_book(title, author, publisher, genre, year, copies)
        st.success("Book added successfully!")

elif option == "View Books":
    st.subheader("List of Books")
    books = book.fetch_books()
    if books:
        books=pd.DataFrame(books,columns=["book_id","title","author","publisher","genre","year_published","copies_available"])
        st.dataframe(books)
    else:
        st.write("No books available.")

elif option == "Add Member":
    st.subheader("Add New Member")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    start_date = st.date_input("Membership Start Date", datetime.today())
    end_date = st.date_input("Membership End Date", datetime.today())

    if st.button("Add Member"):
        member.add_member(name, email, phone, start_date, end_date)
        st.success("Member added successfully!")

elif option == "View Members":
    st.subheader("List of Members")
    members = member.fetch_members()

    if members:
        # for m in members:
        members = pd.DataFrame(members,
                               columns=["member_id", "name", "email", "phone", "membership start", "membership end"])
        st.dataframe(members)
    else:
        st.write("No member"
                 "s available.")

elif option == "Borrow Book":
    st.subheader("Borrow Book")
    member_id = st.number_input("Member ID", min_value=1)
    book_id = st.number_input("Book ID", min_value=1)
    borrow_date = st.date_input("Borrow Date", datetime.today())
    return_date = st.date_input("Return Date", datetime.today())

    if st.button("Borrow Book"):
        success = borrow.borrow_book(member_id, book_id, borrow_date, return_date)
        if success:
            st.success("Book borrowed successfully!")
        else:
            st.error("Sorry, this book is not available.")

elif option == "Return Book":
    st.subheader("Return Book")
    record_id = st.number_input("Borrow Record ID", min_value=1)
    book_id = st.number_input("Book ID", min_value=1)

    if st.button("Return Book"):
        borrow.return_book(record_id, book_id)
        st.success("Book returned successfully!") 

