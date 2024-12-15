from tkinter import *
import string

root = Tk()
root.geometry("400x400")
root.title("Password Strength Checker")
root.config(background="#cbccc4")

ans_label = Label(root, text ="Please Enter a Password", font=("Times New Roman", 12), width=40, borderwidth= 10, bg="#cbccc4")
ans_label.grid(row=3, column=2, rowspan=1, columnspan=2, padx= 5, pady=5)
password = Entry(root, width=25, borderwidth=5)
password.grid(row=2, column=2, rowspan=1, columnspan=2, padx=20)

score = 0


upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
special = string.punctuation
digits = string.digits


characters = [upper_case, lower_case, special, digits]
try:
    with open("common_passwords.txt", "r") as file:
        common = file.read()
except FileNotFoundError:
        ans_label.configure(text = "This file does not exist.")

def calc():
    global score, common, characters
    score = 0
    output = password.get()
    if output not in common:
        score = score + 1   
        if len(output) < 6:
            ans_label.config(text= "This password is too short.")
            score == 0
        if len(output) >= 6:
            score = score + len(output)-5
        if upper_case in output:
            score = score + 1
        if lower_case in output:
            score += 1
        if score >= 8:
            ans_label.configure(text = "Your score is "+ str(score) + ". This password is secure.")
        if score < 6:
            ans_label.configure(text = "This password is not secure.")
    else:
        output in common
        ans_label.configure(text = ("This password is a common password.\nPlease choose something else."))
        
def clear():
    global score, common, characters
    password.delete(END, score)
    password.delete(0, END)
    ans_label.configure(text="Please Enter a Password")
    score = 0
    file.close()

check = Button(root, text = 'Check Password', font=("Times New Roman", 10), width = 15, borderwidth = 5, command = calc)
check.grid(row=4, column=2, rowspan=1,columnspan=2)
erase = Button(root, text = "Clear", font = ("Times New Roman", 10), width = 15, borderwidth = 5, command = clear)
erase.grid(row=5, column=2, rowspan=1, columnspan=2)

root.mainloop()