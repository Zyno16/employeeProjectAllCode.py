from tools import *

from mysqldb import *

frm = form("800x600")

cols = ['Employee_ID','Employee_Name','address','Salary']

data = dbget("select * from employee")

tbl = table(frm, cols,data)

tbl.bind()

def f():

#print("All Columns:",tbl.columns_count())

#print("All Rows:",tbl.rows_count())

#print("index:",tbl.table_index)

curRow = tbl.current_row()

print(curRow[0]['text'],curRow[1]['text'],curRow[2]['text'],curRow[3]['text'])

button(frm,"Test",f).pack()

fontall(frm,'verdana 16')

bgall(frm,'lightblue')

fgall(frm,'navy')

frm.mainloop()

if i wana do the table in listbox how i change firt code this is the tool

def combine_funcs(*funcs):

def combined_func(*args,**kwargs):

for f in funs:

f(*args, **kwargs)

return combined_func

class table:

tbl = None

columns = None

rows = None

table_index = -1

all_labels = []

def init(this,form,columns,rows):

this.tbl = Frame(form)

this.columns = columns

this.rows = rows

def columns_count(this):

return len(this.columns)-1

def rows_count(this):

return len(this.rows)

def get_index(this):return this.table_index

def current_row(this):

return this.all_labels[this.table_index]

def bind(this):

r = len(this.rows)

c = len(this.columns)

this.columns.insert(0,"...")

colcount = 0

for col in this.columns:

lbl = label(this.tbl,col)

lbl.config(borderwidth=2,relief ="solid")

lbl.grid(row=0,column=colcount,sticky="nsew")

colcount +=1

for x in range(r):

btnselect = button(this.tbl,"...")

btnselect.config(width =2)

btnselect.grid(row=x+1,column = 0,sticky ="nsew")

lbls =[]

for y in range(c):

lbl = label(this.tbl,str(this.rows[x][y]))

lbl.config(borderwidth=2,relief="solid")

lbl.grid(row=x+1,sticky="nsew")

lbls.append(lb1)

this.all_labels.append(lbls)

def clear_lbl():

for lbl in this.all_labels:

for lbl2 in lbl:

lbls.config(background=this.tbl["background"])

def mark_lbl(labels,index):

this.table_index =index

for lb in labels:

lb.config(background="#e1e1e1")

btncount = 0

for c in this.tbl.winfo_children():

if c.__class__.__name__.lower()=="button":

c.config(

command = combine_funcs(

clear_lbl ,

lambda btncount=btncount:

mark_lbl(this.all_labels[btncount],btncount)

)

)

btncount += 1

this.tbl.pack()

import mysql.connector

all_err =""

myhost = "localhost"

myuser = "userpython"

mypass = "123456"

mydatabase ="mycompany1"

try:

cn = mysql.connector.connect(

host = myhost,

user = myuser,

passwd = mypass

)

cu =cn.cursor()

cu.execute("""

CREATE DATABASE IF NOT EXISTS mycompany1 DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci

""")

except mysql.connector.Error as e:

all_err += str(e) +", PLEASE CHECH THE SERVER AND USERNAME ,"

try:

conn = mysql.connector.connect(

host = myhost,

user = myuser,

passwd =mypass ,

database = mydatabase

)

except mysql.connector.Error as e:

all_err += str(e) +", "

def dbrun(sql):

try:

if 'conn' in globals():

cur = conn.cursor()

cur.execute( sql )

conn.commit()

return True

else:

return False

except mysql.connector.Error as e:

all_err += str(e) + ","

return False

def dbget(sql):

try:

if "conn" in globals():

cur =conn.cursor()

cur.execute(sql)

all_rows =cur.fetchall()

return all_rows

else:

return []

except mysql.connector.Error as e:

all_err += str(e) +","

return []

def dbautonum(table, column):

try:

if "conn" in globals():

cur = conn.cursor()

cur.execute("SELECT MAX(%s)+1 FROM %s" % (column ,table))

row = cur.fetchone()

if row[0] == None: return "1"

else: return row[0]

else:

return ""

except mysql.connector.Error as e:

all_err += str(e) +","

return ""

from mysqldb import *

from tools import *

def create_table():

is_create =dbrun("""

CREATE TABLE IF NOT EXISTS employee(

employee_id int PRIMARY KEY,

employee_name varchar (99),

address varchar(99),

salary int

)

""")

if is_create: msgbox("table is created")

bg = "light blue"

fg = "navy"

ft = "verdana 16"

pad =3

frm =form("800x600","ebay report")

button(frm,"create table",create_table).pack(pady=pad)

empno_var = intVar()

empname_var = strVar()

address_var = strVar()

salary_var = intVar()

def check_emp():

if frm.winfo_children()[2].get().strip()=="":

msgbox("Employee ID is Empty!")

frm.winfo_children()[2].focus()

return False

elif empname_var.get().strip()=="":

msgbox("Employee name is Empty!")

frm.winfo_children()[4].focus()

return False

elif address_var.get().strip() =="":

msgbox("adress is empty!")

frm.winfo_children()[6].focus()

return False

elif frm.winfo_children()[8].get().strip() =="":

msgbox("salary Empty")

frm.winfo_children()[8].focus()

return False

else:

return True

def clear_emp():

empno_var.set(dbautonum("employee","employee_id"))

empname_var.set("")

address_var.set("")

salary_var.set(0)

frm.winfo_children()[9].config(state="enable")

frm.winfo_children()[11].config(state="disable")

frm.winfo_children()[12].config(state="disable")

frm.winfo_children()[4].focus()

def add_emp():

if check_emp():

is_add = dbrun("insert into employee values(%d,'%s','%s',%d)" % ( empno_var.get(),empname_var.get(),address_var.get(),salary_var.get() ))

if is_add ==True: msgbox("employee is added...")

clear_emp()

def find_emp():

enum= inbox("Enter employee ID")

if enum =="": enum=0

print(enum)

rows = dbget("select * from employee where employee_id="+str(enum))

if len(rows) < 1:

msgbox("Employee ID not find!")

else:

row = rows[0]

empno_var.set( row[0] )

empname_var.set( row[1] )

address_var.set( row[2] )

salary_var.set( row[3] )

frm.winfo_children()[9].config(state="disable")

frm.winfo_children()[11].config(state="enable")

frm.winfo_children()[12].config(state="enable")

def edit_emp():

if check_emp():

is_edit = dbrun("update employee set employee_name='"+empname_var.get()+"',address='"+str(address_var.get())+"',salary="+str(salary_var.get())+" where employee_id="+str(empno_var.get()))

if is_edit:msgbox("employee is edited...")

clear_emp()

def del_emp():

if msgask("Do you want to delete"):

is_del = dbrun("delete from employee where employee_id=" +str(empno_var.get()))

if is_del:msgbox("Employee is deleted....")

clear_emp()

label(frm,"employee_id:").pack()

textbox(frm,empno_var,True,True).pack(pady=pad)

empno_var.set(dbautonum("employee","employee_id"))

label(frm,"employee name:").pack()

textbox(frm,empname_var).pack(pady=pad)

label(frm,"address:").pack()

textbox(frm,address_var).pack(pady=pad)

label(frm,"salary:").pack()

textbox(frm,salary_var,True).pack(pady=pad)

button(frm,"Add employee",add_emp).pack(pady=pad)

button(frm,"Find employee",find_emp).pack(pady=pad)

button(frm,"Edit employee",edit_emp).pack(pady=pad)

button(frm,"Delete employee",del_emp).pack(pady=pad)

button(frm,"Clear fields",clear_emp).pack(pady=pad)

button(frm,"Exit",lambda:frm.destroy).pack(pady=pad)

tkcenter(frm )

bgall(frm,bg)

fgall(frm,fg)

fontall(frm,ft)

justall(frm,"center")

widthall(frm,30)

clear_emp()

frm.mainloop
