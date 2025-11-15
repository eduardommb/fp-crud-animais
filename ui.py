import tkinter as tk
window = tk.Tk()

#cores
verde = "#1FF094"
branco = "#ffffff"
vermelho = "#f03d1f"


# configurações gerais
window.geometry("700x400")
window.title("Adoção +")
window.config(
    background= verde
)

#componentes
def logo_grande():
    logo_adocao = tk.Label(
        window, 
        text= "Adoção",
        font = ('Roboto', 40, 'bold'),
        fg= branco, 
        bg= verde
    )
    logo_adocao.place(
        x = 70,
        y = 50
    )

    logo_plus = tk.Label(
        window, 
        text="+",
        font=("Roboto", 50, "bold"),
        bg=verde,
        fg= vermelho
    )
    logo_plus.place(
        x=270,
        y=40
    )

#paginas
def home():
    logo_grande()



home()
window.mainloop()