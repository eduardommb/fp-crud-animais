import tkinter

window = tkinter.Tk() #janela
window.geometry("500x500") #tamanho da janela
window.title("Adoção +") #titulo da janela

#mudar icone
#icone = tkinter.PhotoImage(file="nome-do-arquivo.png") #caminho da imagem
#window.iconphoto(True, icone) #colocar imagem

#background
window.config(background = "#505050") #cinza

#label/div
titulo = tkinter.Label(window,
                        text = "Adoção +", #texto
                        font = ('Arial', 50, 'bold'), #estilo e tamanho da fonte
                        fg = "white", #cor do texto
                        bg = "#505050",#cor de fundo
                        relief = tkinter.RAISED, #borda
                        bd = 10, #tamanho da borda
                        padx = 20, #padding do x
                        pady = 20, #padding do y
                        #image = var_com_a_imagem,
                        #compound = 'bottom' #posicao da imagem em relacao ao texto
                        )
#titulo.pack() #colcoar o label na posição padrao
titulo.place(x=50, y=0) #colocar em uma posição especifica

def click():
    print("Botao apertado")

#botoes
botao = tkinter.Button(window,
                        text = "clique",
                        command = click, #ao apertar o botao, aciona a funcao 'click'
                        )
botao.pack() #aparecer o botao

window.mainloop() #rodar