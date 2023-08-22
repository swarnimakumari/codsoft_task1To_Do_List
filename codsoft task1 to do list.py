#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog

root = Tk()

root.title('To-Do-List-App')
root.geometry("500x500")

# Define our font
my_font = Font(
    family="Brush Script MT",
    size=30,
    weight="bold")
# Create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Create listbox
my_list = Listbox(my_frame,
                  font=my_font,
                  width=25,
                  height=5,
                  bg="#EBEDEF",
                  bd=0,
                  fg="#464646", borderwidth=5
                  , highlightthickness=0,
                  selectbackground="#a6a6a6",
                  activestyle="none"
                  )  # systemButtonFace

my_list.pack()
# Create dummy list
stuff = ["Wake up at 6 am","Go to College", "Buy notebook", "Came to home", "Complete the project", "Complete task2",
         "Take medicines"]
# Add dummy list to the list box
for item in stuff:
    my_list.insert(END, item)
# Add scroll bar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# create an entry box to add items to the list
my_entry = Entry(root, font=("Helvetica", 24), width=26, borderwidth=5)
my_entry.pack(pady=20)

# create button frame
button_frame = Frame(root)
button_frame.pack(pady=20)


# Functions
def delete_item():
    my_list.delete(ANCHOR)


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


def cross_off_item():
    # cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    # get rid of selection bar
    my_list.select_clear(0, END)


def uncross_item():
    # cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")
    # get rid of selection bar
    my_list.select_clear(0, END)


def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1


def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="D:\Python_Projects\info_aidtech_task\data"
        , title="Save File", filetypes=(("Dat Files", "*.dat")
                                        , ("All Files", "*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
        # Delete crossed off items before saving
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count += 1
            # Grab all the stuff from the list
        my_list.get(0, END)

        # Open the file
        output_file = open(file_name, 'wb')

        # Actually add the stuff to the file
        pickle.dump(stuff, output_file)


def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="D:\Python_Projects\info_aidtech_task\data"
        , title="Save File", filetypes=(("Dat Files", "*.dat")
                                        , ("All Files", "*.*")))
    if file_name:
        # Delete currently open list
        my_list.delete(0, END)
        input_file = open(file_name, 'rb')
        # Load the data the data from the file
        stuff = pickle.load(input_file)

        # Output the stuff to the screen
        for item in stuff:
            my_list.insert(END, item)


def clear_list():
    my_list.delete(0, END)


# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu, bg="#808B96")

# Add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# Add drop down items
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)

# Add some buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross off Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)
delete_crossed_button = Button(button_frame, text="Delete Crossed", command=delete_crossed)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()


# In[ ]:


# In[ ]:





# In[ ]:




