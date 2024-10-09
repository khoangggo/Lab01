import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Ô kết quả
        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Grid số và thao tác
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)
        self.create_button('C', 1, 4)

        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)
        self.create_button('√', 2, 4)

        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)
        self.create_button('x²', 3, 4)

        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('=', 4, 2)
        self.create_button('+', 4, 3)
        self.create_button('PT Bậc 2', 4, 4)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, width=9, height=3,
                           command=lambda: self.click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=2, pady=2)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Lỗi")
        elif key == 'C':
            self.display.delete(0, tk.END)
        elif key == 'PT Bậc 2':
            self.phuongtrinhbac2()
        elif key == '√':
            self.canbachai()
        elif key == 'x²':
            self.binhphuong()
        else:
            self.display.insert(tk.END, key)

    def binhphuong(self):
        try:
            value = float(self.display.get())
            result = value ** 2
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Lỗi")

    def canbachai(self):
        try:
            value = float(self.display.get())
            if value < 0:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Lỗi")
            else:
                result = math.sqrt(value)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Lỗi")


    def phuongtrinhbac2(self):
        solver_window = tk.Toplevel(self.master)
        solver_window.title("Giải phương trình bậc 2")

        tk.Label(solver_window, text="ax² + bx + c = 0").grid(row=0, column=0, columnspan=2)

        tk.Label(solver_window, text="a =").grid(row=1, column=0)
        a_entry = tk.Entry(solver_window)
        a_entry.grid(row=1, column=1)

        tk.Label(solver_window, text="b =").grid(row=2, column=0)
        b_entry = tk.Entry(solver_window)
        b_entry.grid(row=2, column=1)

        tk.Label(solver_window, text="c =").grid(row=3, column=0)
        c_entry = tk.Entry(solver_window)
        c_entry.grid(row=3, column=1)

        solve_button = tk.Button(solver_window, text="Giải", command=lambda: self.giaiphuongtrinh(a_entry.get(), b_entry.get(), c_entry.get()))
        solve_button.grid(row=4, column=0, columnspan=2)

    def giaiphuongtrinh(self, a, b, c):
        try:
            a, b, c = float(a), float(b), float(c)
            discriminant = b**2 - 4*a*c

            if discriminant > 0:
                x1 = (-b + math.sqrt(discriminant)) / (2*a)
                x2 = (-b - math.sqrt(discriminant)) / (2*a)
                messagebox.showinfo("Kết quả", f"Phương trình có hai nghiệm phân biệt:\nx1 = {x1:.2f}\nx2 = {x2:.2f}")
            elif discriminant == 0:
                x = -b / (2*a)
                messagebox.showinfo("Kết quả", f"Phương trình có nghiệm kép:\nx = {x:.2f}")
            else:
                messagebox.showinfo("Kết quả", "Phương trình vô nghiệm")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")
        except ZeroDivisionError:
            messagebox.showerror("Lỗi", "a không thể bằng 0")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()