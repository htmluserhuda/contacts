import tkinter as tk
import pyodbc

root = tk.Tk()

entry_phone = tk.Entry(root)
entry_email = tk.Entry(root)
entry_name = tk.Entry(root)


root.configure(background="navy blue")
root.geometry("600x400")




DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'DESKTOP-IG0UQS9\SQLEXPRESS'
DATABASE_NAME = 'project'

conn = f"""DRIVER={{{DRIVER_NAME}}};
                    Server={SERVER_NAME};
                    Database={DATABASE_NAME};
                    Trusted_Connection=yes;"""

COOI = pyodbc.connect(conn)

cursor = COOI.cursor()
def save():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    cursor.execute("INSERT INTO persons (pname, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    COOI.commit()

label_name = tk.Label(root, text="اسم الشخص",width=17,height=2)


label_phone = tk.Label(root, text="رقم الهاتف",width=17,height=2)

label_email = tk.Label(root, text="البريد الإلكتروني",width=17,height=2)

button_text = "حفظ"
button_save = tk.Button(root, text="حفظ", command=save,width=17,height=2)
button_save.configure(foreground="navy blue",background="yellow")

button_cancel = tk.Button(root, text="إلغاء", command=root.destroy,width=17,height=2)
button_cancel.configure(foreground="navy blue",background="yellow")

name="Huda elsayed"
phone=1093185380
email='hdyalmsar@gmail.com'
COOI.commit()




label_name.pack(pady=10)
entry_name.pack(pady=10)

label_phone.pack(pady=10)
entry_phone.pack(pady=10)
label_email.pack(pady=10)
entry_email.pack(pady=10)
button_save.pack(pady=10)
button_cancel.pack(pady=10)
root.mainloop()