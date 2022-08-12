import tkinter
from re import I
from tkinter import StringVar, ttk

import Employee


def create_frame(frame):
    
    W = tkinter.W

    sal_low_label = ttk.Label(frame, text="What is the low end salary? ")
    sal_high_label = ttk.Label(frame, text=" What is the high end Salary? ")

    sal_low = StringVar()
    sal_high = StringVar()

    sal_low_entry = ttk.Entry(frame, textvariable = sal_low)
    sal_high_entry = ttk.Entry(frame, textvariable = sal_high)

    search_button = ttk.Button(frame, text = "Search", command= lambda: search_sal())
    nxt_bttn = ttk.Button(frame,text="Next",command= lambda: nxt_set())
    last_bttn = ttk.Button(frame,text="Last",command= lambda:  last_set())

    sal_low_label.grid(column = 0, row = 0)
    sal_low_entry.grid(column= 1, row = 0)
    sal_high_label.grid(column= 0, row = 1)
    sal_high_entry.grid(column = 1, row =1)
    search_button.grid(column = 0, row =2)
    last_bttn.grid(column = 0, row =3)
    nxt_bttn.grid(column= 1, row = 3)
    
    emp_list = Employee.Employee.emp_list
    pages = 0 
    current_page = 0
    output_var = []
    output_list = []
    search_list = []

    for x in range(10):
        output_var.append(StringVar())
        output_list.append(ttk.Label(frame,textvariable=output_var[x]))
        output_list[x].grid(column=0,row=x+4,sticky=W,columnspan=4)

    def search_sal():
        nonlocal search_list
        nonlocal pages
        try:
            sal_low_int = int(sal_low.get())
            sal_high_int = int(sal_high.get())

        except ValueError as e:
            print("You probably didn't enter an int")
        for emp in emp_list:
            if emp.salary >= sal_low_int and emp.salary <= sal_high_int:
                search_list.append(emp)
        pages = int(len(search_list)/ 10)
        for x in range(10):
            try:
                output_var[x].set(search_list[x])
            except IndexError:
                pass
    
    def nxt_set():
        nonlocal current_page
        if current_page < pages-1:
            for y in range(10*current_page,10*(current_page+1)):
                try:
                    output_var[y%10].set(search_list[y])
                except IndexError:
                    pass
            current_page += 1
    
    def last_set():
        nonlocal current_page
        if current_page > 0:
            for y in range(10*(current_page-1),10*(current_page)):
                try:
                    output_var[y%10].set(search_list[y])
                except IndexError as e:
                    pass
            current_page -= 1
        
