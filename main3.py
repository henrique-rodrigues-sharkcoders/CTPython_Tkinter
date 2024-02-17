import tkinter as tk

cor_azul= "#198e9e"
cor_vermelho= "#e91414"
cor_verde= "#50e11e"
cor_preto= "#000000"

def event_logger(color):
    print(f"O botão {color}, foi clicado.")

def change_to_azul():
    root.configure(bg=cor_azul)
    event_logger(cor_azul)

def change_to_vermelho():
    root.configure(bg=cor_vermelho)
    event_logger(cor_vermelho)

def change_to_verde():
    root.configure(bg=cor_verde)
    event_logger(cor_verde)

def change_to_preto():
    root.configure(bg=cor_preto)
    event_logger(cor_preto)

root =tk.Tk()

root.title("Color Changer")
root.geometry("500x300+200+200")
root.wm_resizable(width=False, height=False)

lb1 =tk.Label(root, text="Hello World", font="Time 20 bold")
lb1.place(width=200, height=50, x=(500/2)-(200/2)+5, y=(0+100)-80/2)

bt1 = tk.Button(root, text="Azul", command=change_to_azul,font="Times 20 bold")
bt1.place(width=110, height=30, x=(0+80)-(80/2), y=(30+(30/2)))

bt2 = tk.Button(root, text="Vermelho", command=change_to_vermelho, font="Times 20 bold")
bt2.place(width=110, height=30, x=(500-80)-(110/2), y=(30+(30/2)))

bt3 = tk.Button(root, text="Verde", command=change_to_verde, font="Times 20 bold")
bt3.place(width=110, height=30, x=(0+80)-(80/2), y=300-80)

bt4 = tk.Button(root, text="Preto", command=change_to_preto, font="Times 20 bold")
bt4.place(width=110, height=30, x=(500-80)-(110/2), y=300-80)

bt_msg = tk.Button(root, text="OK", font="Times 20 bold")
bt_msg.place(width=110, height=30, x=200 + 5, y=300-80)

text_box = tk.Text(
    root,
    height=12,
    width=40
)
text_box.pack(expand=True)
text_box.insert('end', "Batatinha")
text_box.config(state='disabled')

text_box.place(width=250, height=40, x= 250+5-(250/2), y=150)

root.mainloop()
