import tkinter as tk
from tkinter import PhotoImage, Label, Entry, Frame, Button, messagebox
import mysql.connector
from PIL import Image, ImageTk

data_barang = []
menu = ["Input Barang", "Update Barang", "Hapus Barang", "Tampilkan Data Barang", "Keluar"]
connection = None

def connect_database():
    try:
        connector = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kelompok"
        )
        print("Database terhubung")
        return connector
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def input_barang(nama_barang, jumlah, harga):
    data_barang.append({"nama_barang": nama_barang, "jumlah": jumlah, "harga": harga})

def insert_barang_to_database(nama_barang, jumlah, harga):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO stok_barang (nama_barang, jumlah, harga) VALUES (%s,%s,%s)", (nama_barang, jumlah, harga))
    connection.commit()

def update_barang(id, jumlah, harga):
    cursor = connection.cursor()
    cursor.execute("UPDATE stok_barang SET jumlah = %s, harga = %s WHERE id = %s", (jumlah, harga, id))
    connection.commit()

def delete_barang(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stok_barang WHERE id = %s", (id,))
    deleted_record = cursor.fetchone()

    if deleted_record:
        cursor.execute("DELETE FROM stok_barang WHERE id = %s", (id,))
        cursor.execute("INSERT INTO history_deleted (id, nama_barang, jumlah, harga) VALUES (%s, %s, %s, %s)",
                       (deleted_record[0], deleted_record[1], deleted_record[2], deleted_record[3]))  
        connection.commit()
    cursor.close()

def show_history_deleted():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM history_deleted")
    result = cursor.fetchall()

    if not result:
        messagebox.showinfo("Info", "Belum ada data barang.")
    else:
        data = "\n==== HISTORY DELETED ====\n"
        for row in result:
            data += f"ID: {row[0]}, Nama Barang: {row[1]}, Jumlah: {row[2]}, Harga: {row[3]}\n"
        messagebox.showinfo("Data Barang", data)

def show_stok_barang():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stok_barang")
    result = cursor.fetchall()

    if not result:
        messagebox.showinfo("Info", "Belum ada data barang.")
    else:
        data = "\n====DATA BARANG ====\n"
        for row in result:
            data += f"ID: {row[0]}, Nama Barang: {row[1]}, Jumlah: {row[2]}, Harga: {row[3]}\n"
        messagebox.showinfo("Data Barang", data)

def input_barang_rekursif(iterasi):
    if iterasi > 0:
        nama_barang = entry_nama.get()
        jumlah = int(entry_jumlah.get())
        harga = int(entry_harga.get())
        input_barang(nama_barang, jumlah, harga)
        insert_barang_to_database(nama_barang, jumlah, harga)
        show_stok_barang()
        entry_nama.delete(0, tk.END)
        entry_jumlah.delete(0, tk.END)
        entry_harga.delete(0, tk.END)
        return input_barang_rekursif(iterasi - 1)

def input_update_barang():
    id = int(entry_id.get())
    jumlah = int(entry_jumlah_update.get())
    harga = int(entry_harga_update.get())
    update_barang(id, jumlah, harga)
    show_stok_barang()
    entry_jumlah_update.delete(0, tk.END)
    entry_harga_update.delete(0, tk.END)

def input_delete_barang_by_id():
    id_to_delete = entry_id_delete.get()
    if id_to_delete.isdigit():
        id_to_delete = int(id_to_delete)
        delete_barang(id_to_delete)
        show_stok_barang()
        entry_id_delete.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "ID harus berupa angka.")

def on_enter_username(e):
    user.delete(0, 'end')

def on_leave_username(e):
    if not user.get():
        user.insert(0, 'Username')

def on_enter_password(e):
    code.delete(0, 'end')
    code.config(show='*')  

def on_leave_password(e):
    if not code.get():
        code.insert(0, 'password')
        code.config(show='')  

def main_menu():
    print("Main menu berjalan.")

def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '666666':
        messagebox.showinfo("Login Berhasil", "Login sukses!")
        root.destroy()  
        main_menu()     
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah!")

root = tk.Tk()
root.title("Login")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img_pil = Image.open("asli1.jpg")
img_tk = ImageTk.PhotoImage(img_pil)

Label(root, image=img_tk, bg='white').place(x=100, y=100)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='sign in', fg='#57a1f8', bg='white', font=("Microsoft YaHei UI Light", 23, 'bold'))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_username)
user.bind('<FocusOut>', on_leave_username)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11), show='*')
code.place(x=30, y=150)
code.insert(0, 'password')
code.bind('<FocusIn>', on_enter_password)
code.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg="white", border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg="white", font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign_up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

root.mainloop()

def main_menu():
    global connection
    connection = connect_database()

    if connection:
        root = tk.Tk()
        root.title("Aplikasi Pengelolaan Stok Barang")

        bg_image = Image.open("asli1.jpg")
        bg_photo = ImageTk.PhotoImage(bg_image)

        background_label = tk.Label(root, image=bg_photo)
        background_label.place(relwidth=1, relheight=1, anchor=tk.NW)

        frame_input = tk.Frame(root, bg='#DCF2F1')
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="NAMA BARANG : ", bg='#DCF2F1', fg='navy').grid(row=0, column=0)
        tk.Label(frame_input, text="JUMLAH : ", bg='#DCF2F1', fg='navy').grid(row=1, column=0)
        tk.Label(frame_input, text="HARGA : ", bg='#DCF2F1', fg='navy').grid(row=2, column=0)

        root.configure(bg='#DCF2F1')

        global entry_nama, entry_jumlah, entry_harga
        entry_nama = tk.Entry(frame_input)
        entry_jumlah = tk.Entry(frame_input)
        entry_harga = tk.Entry(frame_input)

        entry_nama.grid(row=0, column=1)
        entry_jumlah.grid(row=1, column=1)
        entry_harga.grid(row=2, column=1)

        btn_input = tk.Button(frame_input, text="Input Barang", command=lambda: input_barang_rekursif(1), font=('Arial', 12, 'bold'), fg='white', bg='#7FC7D9')
        btn_input.grid(row=3, column=0, columnspan=2, pady=10)

        frame_update_delete = tk.Frame(root, bg='#DCF2F1')
        frame_update_delete.pack(pady=10)

        tk.Label(frame_update_delete, text="ID BARANG : ", bg='#DCF2F1', fg='navy').grid(row=0, column=0)
        tk.Label(frame_update_delete, text="JUMLAH BARU : ", bg='#DCF2F1', fg='navy').grid(row=1, column=0)
        tk.Label(frame_update_delete, text="HARGA BARU : ", bg='#DCF2F1', fg='navy').grid(row=2, column=0)

        global entry_id, entry_jumlah_update, entry_harga_update
        entry_id = tk.Entry(frame_update_delete)
        entry_jumlah_update = tk.Entry(frame_update_delete)
        entry_harga_update = tk.Entry(frame_update_delete)

        entry_id.grid(row=0, column=1)
        entry_jumlah_update.grid(row=1, column=1)
        entry_harga_update.grid(row=2, column=1)

        btn_update = tk.Button(frame_update_delete, text="Perbarui Stok", command=input_update_barang, font=('Arial', 12, 'bold'), fg='white', bg='#7FC7D9')
        btn_update.grid(row=3, column=0, pady=10, columnspan=2)

        frame_delete = tk.Frame(root, bg='#DCF2F1')
        frame_delete.pack(pady=10)

        tk.Label(frame_delete, text="ID BARANG (HAPUS) : ", bg='#DCF2F1', fg='navy').grid(row=0, column=0)

        global entry_id_delete
        entry_id_delete = tk.Entry(frame_delete)
        entry_id_delete.grid(row=0, column=1)

        btn_delete_id = tk.Button(frame_delete, text="Hapus Barang by ID", command=input_delete_barang_by_id, font=('Arial', 12, 'bold'), fg='white', bg='#7FC7D9')
        btn_delete_id.grid(row=1, column=0, columnspan=2, pady=10)

        btn_tampilkan_data_history = tk.Button(root, text="Tampilkan history delete", command=show_history_deleted, font=('Arial', 12, 'bold'), fg='white', bg='#7FC7D9')
        btn_tampilkan_data_history.pack(pady=10)

        btn_tampilkan_data = tk.Button(root, text="Tampilkan Data Barang", command=show_stok_barang, font=('Arial', 12, 'bold'), fg='white', bg='#7FC7D9')
        btn_tampilkan_data.pack(pady=10)

        root.mainloop()

if __name__ == "__main__":
    main_menu()