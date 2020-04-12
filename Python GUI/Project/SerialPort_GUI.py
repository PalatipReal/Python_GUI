from tkinter import *
import tkinter 
import tkinter as tk
from tkinter import ttk
import threading
import time

window = Tk()
window.title("SerialPort GUI V.1")
window.geometry('500x500')
def Connect_Port():
    global Thread_GetData
    try:
        print("Create Thread_GetData")
        Thread_GetData = threading.Thread(target=GetData, args=("Thread_GetData",2)) #(FN()ปลายทาง Update_NUM สามารถส่งตัวแปรไปได้)
    except:
        print("Can not create Thread_GetData")
    Thread_GetData.daemon = True
    Thread_GetData.start()
    print("Thread_GetData Start")
    text.insert(END, "Connect!!!")
    text.insert(END,"\n")
    text.insert(END, "Port : ")
    text.insert(END, combo_Port.get())
    text.insert(END,"\n")
    text.insert(END, "BondRate : ")
    text.insert(END, combo_BondRate.get())
    text.insert(END,"\n")
def Disconnect_Port():
    #global Thread_GetData
    #Thread_GetData.stop()
    text.insert(END, "Disconnect!!!")
    text.insert(END,"\n")
def Connect_Start():
    #global Thread_Update_GUI
    #Thread_Update_GUI.start()
    text.insert(END, "Start!!!")
    text.insert(END,"\n")
def Connect_Stop():
    #global Thread_Update_GUI
    #Thread_Update_GUI.stop()
    text.insert(END, "Stop!!!")
    text.insert(END,"\n")

def changePort(event):
    print(combo_Port.get())
def changeBondRate(event):
    print(combo_BondRate.get())

def Update_GUI(ThreadName,Delay):
    while(1):
        time.sleep(Delay)
        try:
            print("Updata to GUI")
        except:
            print("Can not Updata to GUI")

def GetData(ThreadName,Delay):
    while(1):
        time.sleep(Delay)
        try:
            print("Getdata to GUI")
        except:
            print("Can Getdata to GUI")

#<------------------------Main Funtion Start Here -------------------------------------------------------------->                              
if __name__ == "__main__":
    try:
        Thread_Update_GUI = threading.Thread(target=Update_GUI, args=("Thread_Update_GUI",2)) #(FN()ปลายทาง Update_NUM สามารถส่งตัวแปรไปได้)
        print("Create Thread_Update_GUI")
    except:
        print("Can not create Thread_Update_GUI")

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
                            font=(10)).place(x = 10, y = 105)
    button_DisConnect = Button(window,
                            height = 1, 
                            width = 9 , 
                            text = "Disconnect", 
                            command = Disconnect_Port,
                            font=(10)).place(x = 100, y = 105)
    button_Start = Button(window,
                            height = 1, 
                            width = 7, 
                            text = "Start", 
                            command = Connect_Start,
                            font=(10)).place(x = 220, y = 105)
    button_Stop = Button(window,
                            height = 1, 
                            width = 7, 
                            text = "Stop", 
                            command = Connect_Stop,
                            font=(10)).place(x = 320, y = 105)
#<-------------------------------------------------------------------------------------------------------------->
    frame_1 = Frame(height = 285, width = 480, bd = 3, relief = 'groove').place(x = 10, y = 150)
    text = Text(width = 57, height = 16)
    text.place(x = 20, y = 160)
    # ลองสร้าง Thread สำหรับแสดงผลค่าที่สุ่มได้
    window.mainloop()
