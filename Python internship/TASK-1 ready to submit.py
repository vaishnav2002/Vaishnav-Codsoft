import tkinter as tk
from tkinter import *
import mysql.connector
from mysql.connector import Error

try:
    mycon = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="internship"
    )
    if mycon.is_connected():
        print("Connected to MySQL")
except Error as e:
    print("Error while connecting to MySQL", e)

root = tk.Tk()
root.geometry("800x800")
root.title("TO-DO LIST")
root.configure(bg='Linen')

title_label = tk.Label(root, text="TO-DO LIST", font=("Arial", 18), bg='Linen')
title_label.pack(padx=10, pady=10)

activity_frame = tk.Frame(root, bg='Linen')
activity_frame.pack(padx=20, pady=5, fill=tk.X)

activity_label = tk.Label(activity_frame, text="Activity:", font=("Arial", 15), bg='Linen')
activity_label.pack(side=LEFT, padx=5)

activity_entry = tk.Entry(activity_frame, width=50, bg='Antique White', bd=5)
activity_entry.pack(side=LEFT, padx=5)

date_frame = tk.Frame(root, bg='Linen')
date_frame.pack(padx=20, pady=5, fill=tk.X)

date_label = tk.Label(date_frame, text="Date:", font=("Arial", 15), bg='Linen')
date_label.pack(side=LEFT, padx=5)

date_entry = tk.Entry(date_frame, width=30, bg='Antique White', bd=5)
date_entry.pack(side=LEFT, padx=5)

description_frame = tk.Frame(root, bg='Linen')
description_frame.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

description_label = tk.Label(description_frame, text="Description:", font=("Arial", 15), bg='Linen')
description_label.pack(padx=5, pady=5, anchor='w')

textbox = tk.Text(description_frame, height=5, bg='Antique White', font=("Arial", 15))
textbox.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

def add_task():
    activity = activity_entry.get()
    date = date_entry.get()
    description = textbox.get("1.0", END).strip()
    
    if activity and date and description:
        try:
            cursor = mycon.cursor()
            insert_query = "INSERT INTO todolist (Activity, Date, Description) VALUES (%s, %s, %s)"
            task_data = (activity, date, description)
            cursor.execute(insert_query, task_data)
            mycon.commit()
            cursor.close()
            
            
            activity_entry.delete(0, END)
            date_entry.delete(0, END)
            textbox.delete("1.0", END)
            
            print("Task added successfully")
        except Error as e:
            print("Failed to insert into MySQL table", e)
    else:
        print("Please fill in all fields")

add_button = tk.Button(root, text="ADD", bg="Coral", font=("Arial", 15), command=add_task)
add_button.pack(padx=30, pady=10)

result_frame = tk.Frame(root, bg='Linen')
result_frame.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

result_label = tk.Label(result_frame, text="Result:", font=("Arial", 15), bg='Linen')
result_label.pack(padx=5, pady=5, anchor='w')

textbox1 = tk.Text(result_frame, height=10, bg='Antique White', font=("Arial", 15))
textbox1.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

def show_tasks():
    try:
        cursor = mycon.cursor()
        select_query = "SELECT * FROM todolist"
        cursor.execute(select_query)
        tasks = cursor.fetchall()
        cursor.close()
        
        textbox1.delete("1.0", END)
        
        for task in tasks:
            textbox1.insert(END, f"Activity: {task[0]}\nDate: {task[1]}\nDescription: {task[2]}\n\n")
    except Error as e:
        print("Failed to retrieve data from MySQL table", e)

show_button = tk.Button(root, text="SHOW", bg="Coral", font=("Arial", 15), command=show_tasks)
show_button.pack(padx=30, pady=10)

root.mainloop()

if mycon.is_connected():
    mycon.close()
    print("MySQL connection is closed")