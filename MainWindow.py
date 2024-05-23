from tkinter import * 

#Gerando janela
janela = Tk()
janela.title("Life´s game")
janela.geometry('1200x800')



#Gerando pergunta
texto = Label(janela, text = "Pergunta teste", font=('TkDefaultFont', 28))
texto.grid(column = 0, row=0,  padx=450, pady=200)

#Gerando botões
buttonA = Button(janela, text= 'Escolha 1')
ButtonB = Button(janela, text = 'Escolha 2')
buttonA.grid(column=2, row=1, padx=100, pady=10)


janela.resizable(False,False)
janela.mainloop()