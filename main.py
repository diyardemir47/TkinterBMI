import tkinter
from tkinter import messagebox

# windows
window = tkinter.Tk()

window.title("dasdas")
window.minsize(width=500, height=300)

def hesapla():
    boy = my_entry.get()
    kilo = my_entry2.get()

    if not boy or not kilo:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
        return

    boy = float(boy)
    kilo = float(kilo)
    sonuc = boy * kilo
    print(sonuc)

my_label = tkinter.Label()
my_label.config(text="BOYUNUZ", font=("Arial", 30, "bold"))
my_label.pack()

my_entry = tkinter.Entry()
my_entry.config(width=50, bg="red")
my_entry.pack()

my_label2 = tkinter.Label()
my_label2.config(text="KİLO", font=("Arial", 30, "bold"))
my_label2.pack()

my_entry2 = tkinter.Entry()
my_entry2.config(width=50, bg="red")
my_entry2.pack()

my_button = tkinter.Button(
    text="Hesapla", font=("Arial", 15, "bold"), command=hesapla
)
my_button.pack()

window.mainloop()  # Ana döngüyü başlat
