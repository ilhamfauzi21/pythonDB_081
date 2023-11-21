import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

uiApp = tk.Tk()
uiApp.configure(background='black')
uiApp.geometry("500x500")
uiApp.resizable(False,False)
uiApp.title("Multiplatform kelas A")

#make canvas
inputFrame = tk.Frame(uiApp)
inputFrame.pack(padx=10,fill="x", expand=True)

#make label
inputLabel = ttk.Label(inputFrame,text="Zodiak")
inputLabel.pack(padx=10, fill="x", expand=True)

uiApp.mainloop()
#1. Membuat Input Tanggal lahir
labelInputTgl = ttk.Label(inputFrame, text="Masukan Tanggal Lahir Kamu")
labelInputTgl.pack(padx=10, pady=5, fill="x", expand=true)

entryInputTgl = ttk.Entry(inputFrame)
entryInputTgl.pack(padx=10, pady=5, fill="x", expand=True)

#2. Membuat Input Bulan lahir
labelInputBln = ttk.Label(inputFrame, text="Masukan Bulanl Lahir Kamu")
labelInputBln.pack(padx=10, pady=5, fill="x", expand=true)

entryInputBln = ttk.Entry(inputFrame)
entryInputBln.pack(padx=10, pady=5, fill="x", expand=True)


#3. Membuat Button
#membuat fungsi dialog
def klikButton():
    TanggalLahir = entryInputTgl.get()
    bulanLahir = entryInputBln.get()
    messagebox.showinfo("Ramalan Zodiak",
                        "Tanggal Lahir Kamu adalah: " + tanggalLahir +
                        ",Bulan Lahir Kamu adalah: " + bulanLahir +
                        "\n Ramalan Zodiak Kamu : Kamu akan menikah dengan Zee JKT48")
    
buttonSumbit = ttk.Button(inputFrame, text="CEK RAMALAN ZODIAK KAMU SEKARANG !!!!!!!")
buttonSumbit.pack(pady=10, padx=10, fill="x", expand=True)
uiApp.mainloop()

