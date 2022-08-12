import datetime
import tkinter
from tkinter import StringVar, ttk

import Employee
import main_frame


def create_frame(frame):
        
    W = tkinter.W

    day_low_label = ttk.Label(frame, text="What is the begin date(MM/DD/YYYY)? ")
    day_high_label = ttk.Label(frame, text=" What is the end date(MM/DD/YYYY)? ")

    day_low = StringVar()
    day_high = StringVar()

    day_low_entry = ttk.Entry(frame, textvariable = day_low)
    day_high_entry = ttk.Entry(frame, textvariable = day_high)

    search_button = ttk.Button(frame, text = "Search", command= lambda: search_sal())
    nxt_bttn = ttk.Button(frame,text="Next",command= lambda: nxt_set())
    last_bttn = ttk.Button(frame,text="Last",command= lambda:  last_set())
    back_bttn = ttk.Button(frame,text="Cancel",command=lambda : back())

    day_low_label.grid(column = 0, row = 0)
    day_low_entry.grid(column= 1, row = 0)
    day_high_label.grid(column= 0, row = 1)
    day_high_entry.grid(column = 1, row =1)
    search_button.grid(column = 0, row =2)
    last_bttn.grid(column = 0, row =3)
    nxt_bttn.grid(column= 1, row = 3)
    back_bttn.grid(column= 2, row =3)
    
    emp_list = []
    listEmp = Employee.Employee.emp_list
    for x in listEmp:
        emp_list.append(x.return_dict())
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
        nonlocal emp_list
        low_date_obj = datetime.datetime.strptime(day_low.get(),"%m/%d/%Y")
        high_date_obj = datetime.datetime.strptime(day_high.get(),"%m/%d/%Y")
        search_list = [x for x in emp_list if datetime.datetime.strptime(x["Date"],"%m/%d/%Y") > low_date_obj and datetime.datetime.strptime(x["Date"],"%m/%d/%Y") < high_date_obj]
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
        
    def back():
        main_frame.create_frame(frame)
