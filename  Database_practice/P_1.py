from tkinter import *
root=Tk()
root.title("database ")
conn=sqlite3
# Create a databases or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# query of the database
c.execute("SELECT *, oid FROM addresses")
records = c.fetchall()
print(records)

# Loop through the results
print_record=''
for record in records:
    print_record += str(record) + "\n"
query_label = Label(root, text=print_record)
query_label.grid(row=8, column=0, columnspan=2)

conn.commit()
conn.close()