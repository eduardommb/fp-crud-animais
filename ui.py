import tkinter as tk
#import customtkinter as ctk

window = tk.Tk()

#-----------------cores----------------------
verde = "#1FF094"
preto = "#000000"
branco = "#ffffff"
vermelho = "#f03d1f"
azul = "#441ff0"

#--------- configurações gerais--------------
window.geometry("700x400")
window.title("Adoção +")
window.config(
    background= verde
)

#---------------funções----------------------
def func_teste():
    return print("Hello World")

#def botao_normal():

#------------componentes---------------------
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
#botoes redondos
caminho_img_btn_normal = "img/itens/botao_fundo.png"
botao_normal_fundo = tk.PhotoImage(file=caminho_img_btn_normal)

caminho_img_btn_apertado = "img/itens/botao_fundo_apertado.png"
botao_apertado_fundo = tk.PhotoImage(file=caminho_img_btn_apertado)

def botao(texto, funcao, x, y):
    botao_item = tk.Button(
        window,
        image=botao_normal_fundo,
        text= texto,
        font=("Roboto", 15, "bold"),
        compound="center",
        bg=verde,
        fg=branco,
        padx=10,
        pady=10,
        borderwidth=0,
        relief="flat"
    )
    

    def botao_solto():
        botao_item.config(image=botao_normal_fundo)
        funcao
    def botao_apertado():
        botao_item.config(image=botao_apertado_fundo)

    #ler evento botoes
    botao_item.place(x= x, y=y)



#----------------paginas--------------------
def home():
    logo_grande()

    descricao = tk.Label(
        window,
        text="Um software de gerenciamento \nveterinário e de adoções.",
        font=("Roboto", 15),
        bg=verde,
        fg=preto,
        justify="left"
    )
    descricao.place(
        x=70,
        y=160
    )

    
    texto_botao = "Conferir os dados dos animais já cadastrados"
    func = func_teste

    botao(texto=texto_botao, x=70, y=300, funcao=func)



home()


window.mainloop()