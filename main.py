import tkinter as tk
from tkinter import RIDGE

root = tk.Tk()
root.title('Employee Payroll Management System | Developed By Abrar/Hassan')
# root.geometry("1250*700")

title = tk.Label(root, text='Employee Payroll Management System :', font=('times new roman', 20, 'bold'), bg='#262626',
                 fg='white')

# =============== Frame 1 ===============
frame1 = tk.Frame(root, bd=3, relief=RIDGE, bg='white')
frame1.place(x=10, y=30, width=750, height=620)
title1 = tk.Label(frame1, text='Employee Details :', font=('times new roman', 15), bg='lightgray', fg='black',
                  anchor='w', padx=10)

# ================ row 1 ================
label_code = tk.Label(frame1, text='Employee Code :', font=('times new roman', 15), bg='white', fg='black')
label_code.place(x=10, y=60)
label_designation = tk.Entry(frame1, font=('times new roman', 15), bg='white', fg='black')
label_designation.place(x=180, y=60, width=200)
btn_search = tk.Button(frame1, text='Search', font=('times new roman', 12), bg='gray', fg='black')
btn_search.place(x=400, y=56, width=80, height=30)

# ================ row 2 ================
label_designation = tk.Label(frame1, text='Designation :', font=('times new roman', 15), bg='white', fg='black')
label_designation.place(x=10, y=130)
text_designation = tk.Entry(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
text_designation.place(x=160, y=132, width=200)

label_doj = tk.Label(frame1, text='D.O.J :', font=('times new roman', 15), bg='white', fg='black')
label_doj.place(x=400, y=130)
text_doj = tk.Entry(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
text_doj.place(x=510, y=132, width=200)

# ================ row 3 ================
label_name = tk.Label(frame1, text='Name :', font=('times new roman', 15), bg='white', fg='black')
label_name.place(x=10, y=180)
text_name = tk.Entry(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
text_name.place(x=160, y=182, width=200)

label_dob = tk.Label(frame1, text='D.O.B :', font=('times new roman', 15), bg='white', fg='black')
label_dob.place(x=400, y=180)
text_dob = tk.Entry(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
text_dob.place(x=510, y=182, width=200)

# ================ row 4 ================
label_age = tk.Label(frame1, text='Age :', font=('times new roman', 15), bg='white', fg='black')
label_age.place(x=10, y=230)
text_age = tk.Entry(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
text_age.place(x=160, y=232, width=200)

label_experience = tk.Label(frame1, text='Experience :', font=('times new roman', 15), bg='white', fg='black')
label_experience.place(x=400, y=230)
text_experience = tk.Entry(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
text_experience.place(x=510, y=232, width=200)

# ================ row 5 ================
label_gender = tk.Label(frame1, text='Gender :', font=('times new roman', 15), bg='white', fg='black')
label_gender.place(x=10, y=280)
text_gender = tk.Entry(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
text_gender.place(x=160, y=282, width=200)

label_proof = tk.Label(frame1, text='Proof ID :', font=('times new roman', 15), bg='white', fg='black')
label_proof.place(x=400, y=280)
text_proof = tk.Entry(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
text_proof.place(x=510, y=282, width=200)

# ================ row 6 ================
label_email = tk.Label(frame1, text='Email :', font=('times new roman', 15), bg='white', fg='black')
label_email.place(x=10, y=330)
text_email = tk.Entry(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
text_email.place(x=160, y=332, width=200)

label_contact = tk.Label(frame1, text='Contact No :', font=('times new roman', 15), bg='white', fg='black')
label_contact.place(x=400, y=330)
text_contact = tk.Entry(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
text_contact.place(x=510, y=332, width=200)

# ================ row 7 ================
label_address = tk.Label(frame1, text='Address :', font=('times new roman', 15), bg='white', fg='black')
label_address.place(x=10, y=380)
text_address = tk.Text(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
text_address.place(x=160, y=382, width=550, height=200)


root.mainloop()
