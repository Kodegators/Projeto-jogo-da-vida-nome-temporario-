from tkinter import * 
from Buttongeneric import *
 
#Gerando janela
janela = Tk()
janela.title("Life´s game")
janela.geometry('1200x800')



#Gerando pergunta
texto = Label(janela, text = "Pergunta teste", font=('TkDefaultFont', 28))
texto.place(x = 475, y=100)

#Gerando botões
resposta1_button = CustomButton(janela, text = "Você diz que ele deveria ter estudado e se recusa a ajudar.", command = resposta1_function, height=20, width=60, x =35, y =300)
resposta2_button = CustomButton(janela, text = 'resposta2', command = resposta2_function, height=20, width=60, x = 725, y = 300)


janela.resizable(False,False)
janela.mainloop()


