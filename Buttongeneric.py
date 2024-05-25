from tkinter import *
import tkinter as tk

#Classe botão genérico
class CustomButton(tk.Button):
    def __init__(self, master, text, command,height = 10, width= 10, x = 10, y = 10, **kwargs):
        self.x = x
        self.y = y
        super().__init__(master, text = text, height = height , width = width, command = command, **kwargs)
        self.place(x = self.x, y = self.y)

#Botão de Start Menu
def start_function():
    print("Start button pressed")
    # Add your start functionality here

#Botão para sair
def quit_function(janela):
    print("Quit button pressed")
    janela.quit()  # This will close the application

##def back_function(janelaAnterior):

#resposta boa
def resposta1_function():
   print('qdfdfrg')
   
#resposta ruim
def resposta2_function():
    print('foi também')
    







'''# Create the main window
root = tk.Tk()
root.geometry("400x300")

# Create buttons using the CustomButton class
start_button = CustomButton(root, text="Start", command=start_function)
quit_button = CustomButton(root, text="Quit", command=quit_function)

# Start the Tkinter event loop
root.mainloop()'''