from tkinter import *
from tkinter import messagebox, RIDGE, RIGHT, LEFT
import pymysql
import time


class EmployeeSystem:
    def __init__(self, root):
        self.root = root

        root.title('Employee Payroll Management System | Developed By Abrar/Hassan')
        root.geometry('1350x700+5+5')
        root.config(bg='white')
        title = Label(root, text='Employee Payroll Management System :', font=('times new roman', 20, 'bold'), bg='#262626', fg='white', justify=LEFT)
        title.place(x=0, y=0, relwidth=1)
        btn_emp_show = Button(self.root, text="All Employee's", font=('times new roman', 13), bg='gray', fg='white')
        btn_emp_show.place(x=1100, y=7, width=120, height=25)

        # =============== Frame 1 ===============
        # =============== variables ===============

        self.var_tmp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_pf_id = StringVar()
        self.var_contact = StringVar()
        self.var_experience = StringVar()
        self.var_address = StringVar()

        frame1 = Frame(root, bd=3, relief=RIDGE, bg='white')
        frame1.place(x=10, y=60, width=750, height=620)
        title1 = Label(frame1, text='Employee Details :', font=('times new roman', 18), bg='lightgray', fg='black', anchor='w', padx=10)
        title1.place(x=0, y=0, relwidth=1)

        # ================ row 1 ================
        label_code = Label(frame1, text='Employee Code :', font=('times new roman', 15), bg='white', fg='black')
        label_code.place(x=10, y=60)
        self.text_code = Entry(frame1, font=('times new roman', 15), textvariable=self.var_tmp_code, bg='white', fg='black')
        self.text_code.place(x=180, y=60, width=200)
        btn_search = Button(frame1, text='Search', command=self.search, font=('times new roman', 15), bg='gray', fg='black')
        btn_search.place(x=400, y=56, width=80, height=30)

        # ================ row 2 ================
        label_designation = Label(frame1, text='Designation :', font=('times new roman', 15), bg='white', fg='black')
        label_designation.place(x=10, y=130)
        text_designation = Entry(frame1, font=('times new roman', 12), textvariable=self.var_designation, bg='lightyellow', fg='black')
        text_designation.place(x=160, y=132, width=200)

        label_doj = Label(frame1, text='D.O.J :', font=('times new roman', 15), bg='white', fg='black')
        label_doj.place(x=400, y=130)
        text_doj = Entry(frame1, font=('times new roman', 12), textvariable=self.var_doj, bg='lightyellow', fg='black')
        text_doj.place(x=510, y=132, width=200)

        # ================ row 3 ================
        label_name = Label(frame1, text='Name :', font=('times new roman', 15), bg='white', fg='black')
        label_name.place(x=10, y=180)
        text_name = Entry(frame1, font=('times new roman', 12), textvariable=self.var_name, bg='lightyellow', fg='black')
        text_name.place(x=160, y=182, width=200)

        label_dob = Label(frame1, text='D.O.B :', font=('times new roman', 15), bg='white', fg='black')
        label_dob.place(x=400, y=180)
        text_dob = Entry(frame1, font=('times new roman', 12), textvariable=self.var_dob, bg='lightyellow', fg='black')
        text_dob.place(x=510, y=182, width=200)

        # ================ row 4 ================
        label_age = Label(frame1, text='Age :', font=('times new roman', 15), bg='white', fg='black')
        label_age.place(x=10, y=230)
        text_age = Entry(frame1, font=('times new roman', 12), textvariable=self.var_age, bg='lightyellow', fg='black')
        text_age.place(x=160, y=232, width=200)

        label_experience = Label(frame1, text='Experience :', font=('times new roman', 15), bg='white', fg='black')
        label_experience.place(x=400, y=230)
        text_experience = Entry(frame1, font=('times new roman', 12), textvariable=self.var_experience, bg='lightyellow', fg='black')
        text_experience.place(x=510, y=232, width=200)

        # ================ row 5 ================
        label_gender = Label(frame1, text='Gender :', font=('times new roman', 15), bg='white', fg='black')
        label_gender.place(x=10, y=280)
        text_gender = Entry(frame1, font=('times new roman', 12), textvariable=self.var_gender, bg='lightyellow', fg='black')
        text_gender.place(x=160, y=282, width=200)

        label_proof = Label(frame1, text='Proof ID :', font=('times new roman', 15), bg='white', fg='black')
        label_proof.place(x=400, y=280)
        text_proof = Entry(frame1, font=('times new roman', 12), textvariable=self.var_pf_id, bg='lightyellow', fg='black')
        text_proof.place(x=510, y=282, width=200)

        # ================ row 6 ================
        label_email = Label(frame1, text='Email :', font=('times new roman', 15), bg='white', fg='black')
        label_email.place(x=10, y=330)
        text_email = Entry(frame1, font=('times new roman', 12), textvariable=self.var_email, bg='lightyellow', fg='black')
        text_email.place(x=160, y=332, width=200)

        label_contact = Label(frame1, text='Contact No :', font=('times new roman', 15), bg='white', fg='black')
        label_contact.place(x=400, y=330)
        text_contact = Entry(frame1, font=('times new roman', 12), textvariable=self.var_contact, bg='lightyellow', fg='black')
        text_contact.place(x=510, y=332, width=200)

        # ================ row 7 ================
        label_address = Label(frame1, text='Address :', font=('times new roman', 15), bg='white', fg='black')
        label_address.place(x=10, y=380)
        self.text_address = Text(frame1, font=('times new roman', 12), bg='lightyellow', fg='black')
        self.text_address.place(x=160, y=382, width=550, height=200)

        # =============== Frame 1 ===============

        # =============== Frame 2 ===============
        # =============== variables ===============

        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_b_salary = StringVar()
        self.var_t_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_p_found = StringVar()
        self.var_convince = StringVar()
        self.var_net_salary = StringVar()

        frame2 = Frame(root, bd=3, relief=RIDGE, bg='white')
        frame2.place(x=770, y=60, width=580, height=300)

        title2 = Label(frame2, text='Employee Salary Details :', font=('times new roman', 18), bg='lightgray', fg='black', anchor='w', padx=10)
        title2.place(x=0, y=0, relwidth=1)

        # ================ row 1 ================
        label_month = Label(frame2, text='Month :', font=('times new roman', 15), bg='white', fg='black')
        label_month.place(x=10, y=70)
        label_month = Entry(frame2, font=('times new roman', 12), textvariable=self.var_month, bg='lightyellow', fg='black')
        label_month.place(x=80, y=70, width=100)

        label_year = Label(frame2, text='Year :', font=('times new roman', 15), bg='white', fg='black')
        label_year.place(x=185, y=70)
        label_year = Entry(frame2, font=('times new roman', 12), textvariable=self.var_year, bg='lightyellow', fg='black')
        label_year.place(x=245, y=70, width=100)

        label_b_salary = Label(frame2, text='Basic Salary :', font=('times new roman', 15), bg='white', fg='black')
        label_b_salary.place(x=350, y=70)
        label_b_salary = Entry(frame2, font=('times new roman', 12), textvariable=self.var_b_salary, bg='lightyellow', fg='black')
        label_b_salary.place(x=470, y=70, width=100)

        # ================ row 2 ================
        label_days = Label(frame2, text='Total Days :', font=('times new roman', 15), bg='white', fg='black')
        label_days.place(x=10, y=130)
        text_days = Entry(frame2, font=('times new roman', 12), textvariable=self.var_t_days, bg='lightyellow', fg='black')
        text_days.place(x=120, y=132, width=120)

        label_absent = Label(frame2, text='Absents :', font=('times new roman', 15), bg='white', fg='black')
        label_absent.place(x=270, y=130)
        text_absent = Entry(frame2, font=('times new roman', 12), textvariable=self.var_absent, bg='lightyellow', fg='black')
        text_absent.place(x=430, y=132, width=120)

        # ================ row 3 ================
        label_medical = Label(frame2, text='Medical :', font=('times new roman', 15), bg='white', fg='black')
        label_medical.place(x=10, y=170)
        text_medical = Entry(frame2, font=('times new roman', 12), textvariable=self.var_medical, bg='lightyellow', fg='black')
        text_medical.place(x=120, y=172, width=120)

        label_provident = Label(frame2, text='Provident Found :', font=('times new roman', 15), bg='white', fg='black')
        label_provident.place(x=270, y=170)
        text_provident = Entry(frame2, font=('times new roman', 12), textvariable=self.var_p_found, bg='lightyellow', fg='black')
        text_provident.place(x=430, y=172, width=120)

        # ================ row 4 ================
        label_convince = Label(frame2, text='Convince :', font=('times new roman', 15), bg='white', fg='black')
        label_convince.place(x=10, y=210)
        text_convince = Entry(frame2, font=('times new roman', 12), textvariable=self.var_convince, bg='lightyellow', fg='black')
        text_convince.place(x=120, y=212, width=120)

        label_n_salary = Label(frame2, text='Net Salary :', font=('times new roman', 15), bg='white', fg='black')
        label_n_salary.place(x=270, y=210)
        text_n_salary = Entry(frame2, font=('times new roman', 12), textvariable=self.var_net_salary, bg='lightyellow', fg='black')
        text_n_salary.place(x=430, y=212, width=120)

        # ================ row 5 save btn ================
        btn_calculate = Button(frame2, text='Calculate', command=self.cal_salary, font=('times new roman', 15), bg='orange', fg='black')
        btn_calculate.place(x=20, y=255, width=100, height=30)

        btn_clear = Button(frame2, text='Clear', command=self.clear, font=('times new roman', 15), bg='gray', fg='black')
        btn_clear.place(x=130, y=255, width=100, height=30)

        self.btn_save = Button(frame2, text='Save', command=self.add, font=('times new roman', 15), bg='green', fg='black')
        self.btn_save.place(x=240, y=255, width=100, height=30)

        self.btn_update = Button(frame2, text='Update', state=DISABLED, command=self.update, font=('times new roman', 15), bg='gray', fg='black')
        self.btn_update.place(x=350, y=255, width=100, height=30)

        self.btn_delete = Button(frame2, text='Delete', state=DISABLED, command=self.delete, font=('times new roman', 15), bg='red', fg='black')
        self.btn_delete.place(x=460, y=255, width=100, height=30)

        # =============== Frame 2 ===============

        # =============== Frame 3 ===============
        frame3 = Frame(root, bd=3, relief=RIDGE, bg='white')
        frame3.place(x=770, y=370, width=580, height=310)

        # =============== calculater frame ===============
        self.var_txt = StringVar()
        self.var_operator = ''

        def btn_click(num):
            self.var_operator = self.var_operator + str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator = ''

        def cal_clear():
            self.var_txt.set('')
            self.var_operator = ''

        cal_frame = Frame(frame3, bd=2, bg='white', relief=RIDGE)
        cal_frame.place(x=2, y=2, width=248, height=300)

        text_result = Entry(cal_frame, textvariable=self.var_txt, font=('times new roman', 20), bg='lightyellow',
                            justify=RIGHT)
        text_result.place(x=0, y=0, relwidth=1, height=50)

        # ================ cal row 1 ===============
        btn_7 = Button(cal_frame, text='7', command=lambda: btn_click(7), font=('times new roman', 18, 'bold'))
        btn_7.place(x=1, y=55, w=60, h=60)
        btn_8 = Button(cal_frame, text='8', command=lambda: btn_click(8), font=('times new roman', 18, 'bold'))
        btn_8.place(x=62, y=55, w=60, h=60)
        btn_9 = Button(cal_frame, text='9', command=lambda: btn_click(9), font=('times new roman', 18, 'bold'))
        btn_9.place(x=123, y=55, w=60, h=60)
        btn_div = Button(cal_frame, text='/', command=lambda: btn_click('/'), font=('times new roman', 20, 'bold'))
        btn_div.place(x=184, y=55, w=60, h=60)

        # ================ cal row 2 ===============
        btn_4 = Button(cal_frame, text='4', command=lambda: btn_click(4), font=('times new roman', 18, 'bold'))
        btn_4.place(x=1, y=115, w=60, h=60)
        btn_5 = Button(cal_frame, text='5', command=lambda: btn_click(5), font=('times new roman', 18, 'bold'))
        btn_5.place(x=62, y=115, w=60, h=60)
        btn_6 = Button(cal_frame, text='6', command=lambda: btn_click(6), font=('times new roman', 18, 'bold'))
        btn_6.place(x=123, y=115, w=60, h=60)
        btn_multi = Button(cal_frame, text='*', command=lambda: btn_click('*'), font=('times new roman', 20, 'bold'))
        btn_multi.place(x=184, y=115, w=60, h=60)

        # ================ cal row 3 ===============
        btn_1 = Button(cal_frame, text='1', command=lambda: btn_click(1), font=('times new roman', 18, 'bold'))
        btn_1.place(x=1, y=175, w=60, h=60)
        btn_2 = Button(cal_frame, text='2', command=lambda: btn_click(2), font=('times new roman', 18, 'bold'))
        btn_2.place(x=62, y=175, w=60, h=60)
        btn_3 = Button(cal_frame, text='3', command=lambda: btn_click(3), font=('times new roman', 18, 'bold'))
        btn_3.place(x=123, y=175, w=60, h=60)
        btn_sub = Button(cal_frame, text='-', command=lambda: btn_click('-'), font=('times new roman', 20, 'bold'))
        btn_sub.place(x=184, y=175, w=60, h=60)

        # ================ cal row 3 ===============
        btn_0 = Button(cal_frame, text='0', command=lambda: btn_click(0), font=('times new roman', 18, 'bold'))
        btn_0.place(x=1, y=235, w=60, h=60)
        btn_clr = Button(cal_frame, text='C', command=cal_clear, font=('times new roman', 18, 'bold'))
        btn_clr.place(x=62, y=235, w=60, h=60)
        btn_sum = Button(cal_frame, text='+', command=lambda: btn_click('+'), font=('times new roman', 18, 'bold'))
        btn_sum.place(x=123, y=235, w=60, h=60)
        btn_equal = Button(cal_frame, text='=', command=result, font=('times new roman', 20, 'bold'))
        btn_equal.place(x=184, y=235, w=60, h=60)

        # =============== calculater frame ===============

        # =============== salary frame ===============
        sal_frame1 = Frame(frame3, bd=2, bg='white', relief=RIDGE)
        sal_frame1.place(x=252, y=2, width=320, height=300)

        title_sal = Label(sal_frame1, text='Salary Receipt :', font=('times new roman', 18), bg='lightgray', fg='black', anchor='w', padx=10)
        title_sal.place(x=0, y=0, relwidth=1)

        sal_frame2 = Frame(sal_frame1, bg='white', bd=2, relief=RIDGE)
        sal_frame2.place(x=0, y=33, relwidth=1, height=230)

        # -----------------receipt_sample----------------

        self.sample = f'''\tCompony Name, XYZ\n\tAddress: Xyz, Floor4
------------------------------------------------
| Employee ID\t\t: 
| Salary Of\t\t: Mon-YYYY
| Generated On\t\t: DD-MM-YYYY
------------------------------------------------
| Total Days\t\t: DD
| Total Presents\t\t: DD
| Total Absents\t\t: DD
| Convince\t\t: Rs.----
| Medical\t\t: Rs.----
| P_Found\t\t: Rs.----
| Gross Payments\t\t: Rs.-----
| Net Salary\t\t: Rs.-----
------------------------------------------------
This is computer generated slip, not required
any signature
'''

        scroll_y = Scrollbar(sal_frame2, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_sal_receipt = Text(sal_frame2, font=('times new roman', 12), bg='lightyellow', yscrollcommand=scroll_y.set)
        self.txt_sal_receipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_sal_receipt.yview)
        self.txt_sal_receipt.insert(END, self.sample)

        btn_print = Button(sal_frame1, text='Print', font=('times new roman', 15), bg='lightblue', fg='black')
        btn_print.place(x=220, y=265, width=80, height=30)

        self.check_connection()

    def search(self):
        if self.var_tmp_code.get() == '':
            messagebox.showerror('Error', 'Employee ID Must Be Required')

        else:
            try:
                con = pymysql.Connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_tmp_code.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror('Error', 'Invalid Employee ID', parent=self.root)

                else:
                    self.var_tmp_code.set(row[0])
                    self.var_designation.set(row[1])
                    self.var_name.set(row[2])
                    self.var_age.set(row[3])
                    self.var_gender.set(row[4])
                    self.var_email.set(row[5])
                    self.var_doj.set(row[6])
                    self.var_dob.set(row[7])
                    self.var_experience.set(row[8])
                    self.var_pf_id.set(row[9])
                    self.var_contact.set(row[10])
                    self.text_address.delete('1.0', END)
                    self.text_address.insert(END, row[11])

                    self.var_month.set(row[12])
                    self.var_year.set(row[13])
                    self.var_b_salary.set(row[14])
                    self.var_t_days.set(row[15])
                    self.var_absent.set(row[16])
                    self.var_medical.set(row[17])
                    self.var_p_found.set(row[18])
                    self.var_convince.set(row[19])
                    self.var_net_salary.set(row[20])

                    file_ = open('Salary_Receipt/' + str(row[21]), 'r')
                    self.txt_sal_receipt.delete('1.0', END)
                    for i in file_:
                        self.txt_sal_receipt.insert(END, i)
                    file_.close()

                    self.btn_save.config(state=DISABLED)
                    self.btn_update.config(state=NORMAL)
                    self.btn_delete.config(state=NORMAL)
                    self.text_code.config(state='readonly')

            except Exception as e:
                messagebox.showerror('Search Error', f"{e}")

    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.text_code.config(state=NORMAL)

        self.var_tmp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_pf_id.set('')
        self.var_contact.set('')
        self.text_address.delete('1.0', END)

        self.var_month.set('')
        self.var_year.set('')
        self.var_b_salary.set('')
        self.var_t_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_p_found.set('')
        self.var_convince.set('')
        self.var_net_salary.set('')
        self.txt_sal_receipt.delete('1.0', END)
        self.txt_sal_receipt.insert(END, self.sample)

    def delete(self):
        if self.var_tmp_code.get() == '':
            messagebox.showerror('Error', 'Employee ID Must Be Required')

        else:
            try:
                con = pymysql.Connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_tmp_code.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror('Error', 'Invalid Employee ID', parent=self.root)

                else:
                    op = messagebox.askyesno("Confirm", "Do you want to delete?")
                    if op:
                        cur.execute('delete from emp_salary where e_id=%s', (self.var_tmp_code.get()))
                        con.commit()
                        con.close()

                        messagebox.showinfo('Delete', 'Deleted Successfully', parent=self.root)
                        self.clear()

            except Exception as e:
                messagebox.showerror('Delete Error', f"{e}")

    def add(self):
        if self.var_tmp_code.get() == '' or self.var_net_salary.get() == '' or self.var_name.get() == '':
            messagebox.showerror('Error', 'Employee details are required')

        else:
            try:
                con = pymysql.Connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_tmp_code.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror('Error', 'This Employee is already exist', parent=self.root)

                else:
                    cur.execute("insert into emp_salary values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                                "%s, %s, %s, %s, %s, %s, %s, %s)",
                                (
                                    self.var_tmp_code.get(),
                                    self.var_designation.get(),
                                    self.var_name.get(),
                                    self.var_age.get(),
                                    self.var_gender.get(),
                                    self.var_email.get(),
                                    self.var_doj.get(),
                                    self.var_dob.get(),
                                    self.var_experience.get(),
                                    self.var_pf_id.get(),
                                    self.var_contact.get(),
                                    self.text_address.get('1.0', END),

                                    self.var_month.get(),
                                    self.var_year.get(),
                                    self.var_b_salary.get(),
                                    self.var_t_days.get(),
                                    self.var_absent.get(),
                                    self.var_medical.get(),
                                    self.var_p_found.get(),
                                    self.var_convince.get(),
                                    self.var_net_salary.get(),
                                    self.var_tmp_code.get() + '.txt'
                                ))
                    con.commit()
                    con.close()

                    file_ = open('Salary_Receipt/' + str(self.var_tmp_code.get()) + '.txt', 'w')
                    file_.write(self.txt_sal_receipt.get('1.0', END))
                    file_.close()

                    messagebox.showinfo('Success', 'Record Added Successfully')

            except Exception as e:
                messagebox.showerror('Inserting Error', f"{e}")

    def update(self):
        if self.var_tmp_code.get() == '' or self.var_net_salary.get() == '' or self.var_name.get() == '':
            messagebox.showerror('Error', 'Employee details are required')

        else:
            try:
                con = pymysql.Connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_tmp_code.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror('Error', 'Employee ID is Invalid', parent=self.root)

                else:
                    cur.execute("UPDATE emp_salary SET designation=%s, name=%s, age=%s, gender=%s, email=%s, doj=%s,"
                                "dob=%s, experience=%s, proof_id=%s, contact=%s, address=%s, month=%s, year=%s,"
                                "basic_salary=%s, t_days=%s, absent_days=%s, medical=%s, p_found=%s, convince=%s,"
                                "net_salary=%s, salary_receipt=%s WHERE e_id=%s",
                                (
                                    self.var_designation.get(),
                                    self.var_name.get(),
                                    self.var_age.get(),
                                    self.var_gender.get(),
                                    self.var_email.get(),
                                    self.var_doj.get(),
                                    self.var_dob.get(),
                                    self.var_experience.get(),
                                    self.var_pf_id.get(),
                                    self.var_contact.get(),
                                    self.text_address.get('1.0', END),

                                    self.var_month.get(),
                                    self.var_year.get(),
                                    self.var_b_salary.get(),
                                    self.var_t_days.get(),
                                    self.var_absent.get(),
                                    self.var_medical.get(),
                                    self.var_p_found.get(),
                                    self.var_convince.get(),
                                    self.var_net_salary.get(),
                                    self.var_tmp_code.get() + '.txt',
                                    self.var_tmp_code.get()
                                ))
                    con.commit()
                    con.close()

                    file_ = open('Salary_Receipt/' + str(self.var_tmp_code.get()) + '.txt', 'w')
                    file_.write(self.txt_sal_receipt.get('1.0', END))
                    file_.close()

                    messagebox.showinfo('Success', 'Record Updated Successfully')

            except Exception as e:
                messagebox.showerror('Inserting Error', f"{e}")

    def cal_salary(self):
        if self.var_month.get() == '' or self.var_year.get() == '' or self.var_b_salary.get() == '':
            messagebox.showerror('Error', 'All fields are required')

        else:
            pre_day = int(self.var_b_salary.get()) / int(self.var_t_days.get())
            work_day = int(self.var_t_days.get()) - int(self.var_absent.get())
            sal_ = pre_day * work_day
            detect = int(self.var_medical.get()) + int(self.var_p_found.get())
            addition = int(self.var_convince.get())
            net_sal = sal_ - detect + addition
            self.var_net_salary.set(str(round(net_sal, 2)))

            new_sample = f'''\tCompony Name, XYZ\n\tAddress: Xyz, Floor4
------------------------------------------------
| Employee ID\t\t: {self.var_tmp_code.get()}
| Salary Of\t\t: {self.var_month.get()}-{self.var_year.get()}
| Generated On\t\t: {str(time.strftime("%d-%m-%Y"))}
------------------------------------------------
| Total Days\t\t: {self.var_t_days.get()}
| Total Presents\t\t: {str(int(self.var_t_days.get()) - int(self.var_absent.get()))}
| Total Absents\t\t: {self.var_absent.get()}
| Convince\t\t: Rs.{self.var_convince.get()}
| Medical\t\t: Rs.{self.var_medical.get()}
| P_Found\t\t: Rs.{self.var_p_found.get()}
| Gross Payments\t\t: Rs.{self.var_b_salary.get()}
| Net Salary\t\t: Rs.{self.var_net_salary.get()}
------------------------------------------------
This is computer generated slip, not required
any signature
'''
            self.txt_sal_receipt.delete('1.0', END)
            self.txt_sal_receipt.insert(END, new_sample)

    def check_connection(self):
        try:
            print('connecting...')
            con = pymysql.Connect(host='localhost', user='root', password='', db='ems')
            cur = con.cursor()
            cur.execute("select * from emp_salary where e_id=%s", (self.var_tmp_code.get()))
            cur.fetchone()

        except Exception as e:
            messagebox.showerror('Error connection', f"{e}")


win = Tk()
obj = EmployeeSystem(win)

win.mainloop()
