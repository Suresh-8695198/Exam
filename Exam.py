import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

def missing(missing, st_list):
    for i in missing:
        for j in st_list:
            if j == i:
                st_list.remove(i)
    return st_list

def run(el_list, ec_list, it_list, col, row):
    el = len(el_list)
    ec = len(ec_list)
    it = len(it_list)
    temp_matrix = []

    while it_list or el_list or ec_list:
        if it == ec == el:
            temp_matrix.append(ec_list[:1])
            ec_list = ec_list[1:]
            temp_matrix.append(el_list[:1])
            el_list = el_list[1:]
            temp_matrix.append(it_list[:1])
            it_list = it_list[1:]
        elif el >= ec and el > it:
            if ec > it:
                if it_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
                elif ec_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
                elif el_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
            elif it > ec:
                if ec_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
                elif it_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
                elif el_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
        elif ec >= it and ec > el:
            if el > it:
                if it_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
                elif el_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
                elif ec_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
            elif it > el:
                if el_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
                elif it_list:
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
                elif ec_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
        elif it >= el and it > ec:
            if ec > el:
                if el_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
                elif ec_list:
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
                elif it_list:
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
            elif el > ec:
                if ec_list:
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                    temp_matrix.append(ec_list[:1])
                    ec_list = ec_list[1:]
                elif el_list:
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]
                elif it_list:
                    temp_matrix.append(it_list[:1])
                    it_list = it_list[1:]
                    temp_matrix.append(el_list[:1])
                    el_list = el_list[1:]

    matrix = []
    for i in range(row):
        a = []
        for j in range(col):
            b = temp_matrix[:1]
            b = str(b)[1:-1]
            b = str(b)[1:-1]
            a.append(b)
            temp_matrix = temp_matrix[1:]
        matrix.append(a)

    result = []
    for i in range(col):
        b = []
        for j in range(row):
            b.append(0)
        result.append(b)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]

    return result

def write(result, room_no):
    data = result
    writer = pd.ExcelWriter('static/execl/' + room_no + '.xlsx', engine='xlsxwriter')
    df = pd.DataFrame(data)
    df.to_excel(writer, sheet_name=room_no, header=None, index=False)
    writer.save()

def read(room_no):
    temp = pd.read_excel('static/execl/' + room_no + '.xlsx', header=None, index_col=False).astype(str)
    return temp

class SeatingManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seating Management")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Upload Excel Sheet:").pack(pady=10)
        ttk.Button(self.root, text="Upload", command=self.upload_excel).pack(pady=10)

        ttk.Button(self.root, text="Generate Seating Arrangement", command=self.generate_seating).pack(pady=10)

        ttk.Button(self.root, text="Show Result", command=self.show_result).pack(pady=10)

    def upload_excel(self):
        # Placeholder logic for uploading an Excel sheet
        messagebox.showinfo("Upload", "Upload Excel Sheet functionality to be implemented.")

    def generate_seating(self):
        # Placeholder logic for generating seating arrangement
        messagebox.showinfo("Generate Seating", "Generate Seating Arrangement functionality to be implemented.")

    def show_result(self):
        # Placeholder logic for showing the result
        messagebox.showinfo("Show Result", "Show Result functionality to be implemented.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SeatingManagementApp(root)
    root.mainloop()
