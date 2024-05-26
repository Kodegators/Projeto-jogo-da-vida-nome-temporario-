from tkinter import *
import tkinter as tk
from points import *


#Classe botão genérico
class CustomButton(tk.Button):
    def __init__(self, master, text, command,height = 10, width= 10, x = 10, y = 10, **kwargs):
        self.x = x
        self.y = y
        super().__init__(master, text = text, height = height , width = width, command = command, **kwargs)
        self.place(x = self.x, y = self.y)

#resposta boa
def resposta1_function(var,line,texto,resposta1_button,resposta2_button):
    points1 = str(var.sheetinit['C'+line].value).split(' ')
    var.he += int(points1[0])*10
    var.ha += int(points1[1])*10
    var.re += int(points1[2])*10
    var.mo += int(points1[3])*10
    Points(var.he,var.ha,var.re,var.mo)
    update_question(var,texto,resposta1_button,resposta2_button)    



#resposta ruim
def resposta2_function(var,line,texto,resposta1_button,resposta2_button):
    points1 = str(var.sheetinit['E'+line].value).split(' ')
    var.he += int(points1[0])*10
    var.ha += int(points1[1])*10
    var.re += int(points1[2])*10
    var.mo += int(points1[3])*10
    Points(var.he,var.ha,var.re,var.mo)
    update_question(var,texto,resposta1_button,resposta2_button)    


#Atualiza a tela, perceba que aqui informa a pergunta as respostas
def update_question(var,texto,resposta1_button,resposta2_button):
    question =  var.get_next_question()
    if question:
        line, pergunta, resposta1, resposta2 = question
        texto.config(text=pergunta)
        resposta1_button.config(text=resposta1, command = lambda : resposta1_function(var,line,texto,resposta1_button,resposta2_button))
        resposta2_button.config(text=resposta2, command= lambda : resposta2_function(var,line,texto,resposta1_button,resposta2_button))