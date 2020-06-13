from tkinter import *
from math import *

# Inicializar Ventana de aplicacion
root = Tk()
root.title("Calculadora")
img_icon = PhotoImage(file = 'LogoE256.png')
root.tk.call('wm', 'iconphoto', root._w, img_icon)
root.geometry("315x390")
root.resizable(False, False)
root.configure(bg = "gray60")

# configuracion colores botones numericos y operadores
color_btn_num = "gray75"
color_btn_oper = "SlateGray1"
color_btn_equal = "OrangeRed2"

# Configuracion botones operadores
height_btn = '2'
width_btn = '7'

# Declaracion de Variables
operator = ''
text_display = StringVar()

# Funcion limpiar display
def clear():
    global operator
    operator = ''
    text_display.set('0')

# Tomar valores con evento click sobre los botones
def click(x):
    global operator
    operator += str(x)
    text_display.set(operator)

# Borra el ultimo caracter del string
def undo():
    global operator
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        display.delete(0, END)
        display.insert(0, display_new_state)
        operator = display_new_state
    else:
        clear()

# ejecuta la evaluacion del string
def result():
    global operator
    # Verifica previamente si hay una operacion de porcentaje
    if "*" in operator:
        if '%' in operator:
            operator = operator.replace("%", "/100")
    # Evalua el string del display y muestra el resultado
    try:
        exp = str(eval(operator))
    except:
        exp = 'ERROR'
    text_display.set(exp)
    operator = ""

# Llamado de funcion para colocar cero al iniciar la aplicacion
clear()

# Botones Fila 1

button_C = Button(root, text ='C', bg = color_btn_oper, width = width_btn, height = height_btn, command = clear).grid(row = 8, column = 1, padx = 6, pady = 4)
button_Back = Button(root, text ='⇦', bg = color_btn_oper, width = width_btn, height = height_btn, command = undo).grid(row = 8, column = 2, padx = 6, pady = 4)
button_perc = Button(root, text ='%', bg = color_btn_oper, width = width_btn, height = height_btn, command = (lambda: click('%'))).grid(row = 8, column = 3, padx = 6, pady = 4)
button_div = Button(root, text ='/', bg = color_btn_oper, width = width_btn, height = height_btn, command = lambda:click('/')).grid(row = 8, column = 4, padx = 6, pady = 4)

# Botones Fila 2

button_Pleft = Button(root, text ='(', bg = color_btn_oper, width = width_btn, height = height_btn, command = lambda:click('(')).grid(row = 9, column = 1, padx = 6, pady = 4)
button_Pright = Button(root, text =')', bg = color_btn_oper, width = width_btn, height = height_btn, command = lambda:click(')')).grid(row = 9, column = 2, padx = 6, pady = 4)
button_Mod = Button(root, text ='mod', bg = color_btn_oper, width = width_btn, height = height_btn, command = lambda:click('%')).grid(row = 9, column = 3, padx = 6, pady = 4)
button_Exp = Button(root, text ='exp', bg = color_btn_oper, width = width_btn, height = height_btn, command = lambda:click('exp')).grid(row = 9, column = 4, padx = 6, pady = 4)

# Botones Fila 3

button_7 = Button(root, text ='7', bg = color_btn_num, width = width_btn, height = height_btn, command = lambda:click(7)).grid(row = 10, column = 1, padx = 6, pady = 4)
button_8 = Button(root, text ='8', bg = color_btn_num, width = width_btn, height = height_btn, command = lambda:click(8)).grid(row = 10, column = 2, padx = 6, pady = 4)
button_9 = Button(root, text ='9', bg = color_btn_num, width = width_btn, height = height_btn, command = lambda:click(9)).grid(row = 10, column = 3, padx = 6, pady = 4)
button_mult = Button(root, text ='X', bg = color_btn_oper, width = width_btn, height = height_btn, command = lambda:click('*')).grid(row = 10, column = 4, padx = 6, pady = 4)

# Botones Fila 4

button_4 = Button(root, text ='4', bg = color_btn_num, width = width_btn, height = height_btn, command = lambda:click(4)).grid(row = 11, column = 1, padx = 6, pady = 4)
button_5 = Button(root, text ='5', bg = color_btn_num, width = width_btn, height = height_btn, command = lambda:click(5)).grid(row = 11, column = 2, padx = 6, pady = 4)
button_6 = Button(root, text ='6', bg = color_btn_num, width = width_btn, height = height_btn, command = lambda:click(6)).grid(row = 11, column = 3, padx = 6, pady = 4)
button_res = Button(root, text ='-', bg = color_btn_oper, width = width_btn, height = height_btn, command = lambda:click('-')).grid(row = 11, column = 4, padx = 6, pady = 4)

# Botones Fila 5

button_1 = Button(root, text ='1', bg = color_btn_num, width = width_btn, height = height_btn, command = lambda:click(1)).grid(row = 12, column = 1, padx = 6, pady = 4)
button_2 = Button(root, text ='2', bg = color_btn_num, width = width_btn, height = height_btn, command = lambda:click(2)).grid(row = 12, column = 2, padx = 6, pady = 4)
button_3 = Button(root, text ='3', bg = color_btn_num, width = width_btn, height = height_btn, command = lambda:click(3)).grid(row = 12, column = 3, padx = 6, pady = 4)
button_add = Button(root, text ='+', bg = color_btn_oper, width = width_btn, height = height_btn, command = lambda:click('+')).grid(row = 12, column = 4, padx = 6, pady = 4)

# Botones Fila 6

button_Mn = Button(root, text ='+/-', bg = color_btn_oper, width = width_btn, height = height_btn, command = lambda:click('-')).grid(row = 13, column = 1, padx = 6, pady = 4)
button_0 = Button(root, text ='0', bg = color_btn_num, width = width_btn, height = height_btn, command = lambda:click(0)).grid(row = 13, column = 2, padx = 6, pady = 4)
button_dot = Button(root, text ='.', bg = color_btn_oper, width = width_btn, height = height_btn, command = lambda:click('.')).grid(row = 13, column = 3, padx = 6, pady = 4)
button_result = Button(root, text = '=', bg = color_btn_equal, width = width_btn, height = height_btn, command = result).grid(row = 13, column = 4, padx = 6, pady = 4)

# Pantalla
display = Entry(root, justify = 'right', font =('arial', 19, 'bold'), width = 19, borderwidth = 5, bg = 'sky blue', textvariable = text_display)
display.grid(row = 0, column = 0, columnspan = 5, padx = 16, pady = 16)


root.mainloop()