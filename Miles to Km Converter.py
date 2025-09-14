import tkinter as tk
from tkinter import *
from value import Value

value = Value()
win = tk.Tk()

def check_type():
    value.value = user_input.get()
    try:
        float(value.value)
        print_answer()
    except ValueError as ve:
        label2.config(text="Please enter numbers only.")
        win.after(2000, lambda:label2.config(text=""))

def print_answer():
    value.value = float(value.value)
    if format(value_inside.get()) == "Miles to Km":
        converted_to_km = value.value * 1.609344
        label2.config(text=f"{round(converted_to_km,2)} kms.")
    if format(value_inside.get()) == "Km to Miles":
        converted_to_miles = value.value / 1.609344
        label2.config(text=f"{round(converted_to_miles,2)} miles")
    if format(value_inside.get()) == "Select an Option":
        label2.config(text="Option required.")
        win.after(2000, lambda: label2.config(text=""))

win.title("KM ↔ Miles Converter")
win.geometry("400x400")
win.config(bg="light blue")

options_list = ["Miles to Km", "Km to Miles"]

value_inside = tk.StringVar(win)
value_inside.set("Select an Option")

question_menu = tk.OptionMenu(win, value_inside, *options_list)
question_menu.pack(pady=20)

label1 = Label(text= "Enter Value", font=("Arial",16,""), justify="center", bg="light blue", fg="black")
label1.pack(pady=20)

user_input = Entry(font=("Arial",16,""), justify="center")
user_input.pack(pady=20)
user_input.focus_set()

convert_button = Button(text= "Convert Value", font=("Arial",16,""), justify="center", bg="sky blue", fg="black", command = check_type)
convert_button.pack(pady=20)

label2 = Label( font=("Arial",16,""), justify="center", bg="light blue", fg="black")
label2.pack(pady=20)

win.mainloop()