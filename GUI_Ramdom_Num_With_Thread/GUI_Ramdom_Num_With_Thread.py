#โปรแกรมสุ่มเลขโดยใช้ Thread เข้ามาช่วยในการทำงาน
from tkinter import *
import tkinter 
import threading
import time
from random import seed
from random import randint

Random_Num      = 0
seed(1)
State_Thread1   = False

window = Tk()
window.title("Test Threading Program With Python Tkinter")
window.geometry('500x500')

def Button_Start():
    global State_Thread1
    State_Thread1 = True
    # Start  thread1 as follows สำหรับการอ่านค่ามาจากแหล่งอื่นๆ
    # ลองสร้าง Thread 1
    try:
        Thread1 = threading.Thread(target = get_data) #สร้าง thread1 โดยมีเป้าหมายไปยัง FN() get_data
        # สำเร็จจะแสดงข้อความด้านล่าง
        print("Create Thread 1")
    except:
        # ไม่สำเร็จจะแสดงข้อความด้านล่าง
        print("Can not create Thread 1")
    Thread1.daemon = True # อันนี้คืออะไร?
    Thread2.daemon = True # อันนี้คืออะไร?
    # เริ่มสร้าง Thread 1 , 2
    Thread1.start()
    Thread2.start()
    print("Start thread 1,2")

def get_data():
    global Random_Num
    while(1):
        value = randint(0, 10) # สุ่มเลข 0-10
        Random_Num = value

def Update_NUM(ThreadName,Delay):
    global State_Thread1
    global Random_Num
    while(1):
        time.sleep(Delay)
        if State_Thread1:# ถ้ายังไม่กดเริ่ม Thread 2 จะยังไม่ทำงาน 
            try:
                Label_Display_Thread1_Random_Num = Label(window, text=Random_Num, font=("Arial", 10)).place(x = 60, y = 50)
                print("Add Data to Frame")
            except:
                print("Can not Add Data to Frame")


if __name__ == "__main__":
# Create  Label_Thread1 as folows
    Label_Thread1 = Label(window, text="Thread 1 Start Here ....", font=("Arial", 10)).place(x = 0, y = 0)
# สร้างปุ่ม Start เพื่อเริ่มการทำงานของ Thread 1
    bt_Start = Button(text = "Start", command = Button_Start).place(x = 5, y = 20)
    Label_Display_Thread1 = Label(window, text="Num :", font=("Arial", 10)).place(x = 10, y = 50)
# ลองสร้าง Thread สำหรับแสดงผลค่าที่สุ่มได้
    try:
        Thread2 = threading.Thread(target=Update_NUM, args=("Thread-2",2)) #(FN()ปลายทาง Update_NUM สามารถส่งตัวแปรไปได้)
        print("Create Thread 2")
    except:
        print("Can not create Thread 2")
    window.mainloop()