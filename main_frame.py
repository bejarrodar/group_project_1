
from tkinter import StringVar, ttk
from turtle import clear

import add_emp_frame
import query_frame
import remove_emp_frame
import update_emp_frame


def create_frame(frame):
    
    for child in frame.winfo_children():
        child.destroy()
    
    add_button = ttk.Button(frame,text="Add Employee", command=lambda : add_emp(frame))
    update_button = ttk.Button(frame,text="Update Employee", command=lambda : update_emp(frame))
    remove_button = ttk.Button(frame, text="Remove Employee", command=lambda : remove_emp(frame))
    query_button = ttk.Button(frame,text="Query Employee", command=lambda : query_emp(frame))
    
    add_button.grid(column=0,row=0)
    update_button.grid(column=0,row=1)
    remove_button.grid(column=1,row=0)
    query_button.grid(column=1,row=1)
    
    def clear_frame(frame):
        for child in frame.winfo_children():
            child.destroy()
    
    def add_emp(frame):
        clear_frame(frame)
        add_emp_frame.create_frame(frame)
    
    def update_emp(frame):
        clear_frame(frame)
        update_emp_frame.create_frame(frame)
    
    def remove_emp(frame):
        clear_frame(frame)
        remove_emp_frame.create_frame(frame)
    
    def query_emp(frame):
        clear_frame(frame)
        query_frame.create_frame(frame)
