from tkinter import * 
from sisplan import *
from openpyxl import *
from Buttongeneric import *

janela = Tk()
janela.title("Life´s game")
janela.geometry('1200x800')

#consultando variaveis
var = CurrentQuestion()

for i in range(3):
    var.load_init_table('perguntasinicio.xlsx')

for i in range(3):    
    var.load_mid_table('perguntasmeio.xlsx')

var.load_end_table('perguntasfim.xlsx')  

#Gerando pergunta
texto = Label(janela, text = f"", font=('TkDefaultFont',14), wraplength=500)
texto.place(x = 400, y=100)

#Gerando botões
resposta1_button = CustomButton(janela, text = "", command = lambda : None, height=20, width=60, x =35, y =300)
resposta2_button = CustomButton(janela, text = "", command = lambda : None, height=20, width=60, x = 725, y = 300)

#Indo para a próxima pergunta
update_question(var,texto,resposta1_button,resposta2_button)

janela.resizable(False,False)
janela.mainloop()


