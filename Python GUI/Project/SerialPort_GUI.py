from tkinter import *
import tkinter 
import tkinter as tk
from tkinter import ttk
window = Tk()
window.title("SerialPort GUI V.1")
window.geometry('500x500')

def Connect_Port():
    text.insert(END, "Connect!!!")
    text.insert(END,"\n")
    text.insert(END, combo_Port.get())
    text.insert(END,"\n")
    text.insert(END, combo_BondRate.get())
    text.insert(END,"\n")
def Connect_Start():
    text.insert(END, "Start!!!")
    text.insert(END,"\n")
def Connect_Stop():
    text.insert(END, "Stop!!!")
    text.insert(END,"\n")

def changePort(event):
     print(combo_Port.get())
def changeBondRate(event):
     print(combo_BondRate.get())
#<------------------------Main Funtion Start Here -------------------------------------------------------------->                              
if __name__ == "__main__":
#<------------------------Start Label Name , Port -------------------------------------------------------------->
    Label_Name = Label(window, 
                            text="SerialPort GUI Version 1", 
                            font=("Arial", 14)).place(x = 10, y = 0)
    Label_Port = Label(window, 
                            text="Port :", 
                            font=("Arial", 12)).place(x = 10, y = 40)
#<-------------------------------------------------------------------------------------------------------------->
    combo_Port = ttk.Combobox(window, 
                            values=[
                                    "Com0", 
                                    "Com1",
                                    "Com2",
                                    "Com3"])
    combo_Port.place(x = 95, y = 42)
    combo_Port.current(1)
    combo_Port.bind("<<ComboboxSelected>>", changePort)
#<-------------------------------------------------------------------------------------------------------------->
    Label_BondRate = Label(window, 
                            text="Bondrate :", 
                            font=("Arial", 12)).place(x = 10, y = 70)
    combo_BondRate = ttk.Combobox(window, 
                            values=[
                                    "300", 
                                    "600",
                                    "1200",
                                    "2400", 
                                    "4800",
                                    "9600",
                                    "14400", 
                                    "19200",
                                    "28800",
                                    "38400", 
                                    "57600",
                                    "115200"])
    combo_BondRate.place(x = 95, y = 72)
    combo_BondRate.current(1)                              
    combo_BondRate.bind("<<ComboboxSelected>>", changeBondRate)
#<-------------------------------------------------------------------------------------------------------------->
    button_Connect = Button(window,
                            height = 1, 
                            width = 7 , 
                            text = "Connect", 
                            command = Connect_Port,
                            font=(10)).place(x = 10, y = 100)
    button_Start = Button(window,
                            height = 1, 
                            width = 7, 
                            text = "Start", 
                            command = Connect_Start,
                            font=(10)).place(x = 100, y = 100)
    button_Stop = Button(window,
                            height = 1, 
                            width = 7, 
                            text = "Stop", 
                            command = Connect_Stop,
                            font=(10)).place(x = 200, y = 100)
#<-------------------------------------------------------------------------------------------------------------->
    frame_1 = Frame(height = 285, width = 480, bd = 3, relief = 'groove').place(x = 10, y = 150)
    text = Text(width = 57, height = 16)
    text.place(x = 20, y = 160)
    window.mainloop()
