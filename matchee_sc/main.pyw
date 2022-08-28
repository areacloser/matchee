import os.path
from tkinter import *
from time import time
from random import randint, shuffle
from tkinter.messagebox import *

if os.path.exists("config/config.ini"):
    with open("config/config.ini", "r", encoding="utf-8") as file:
        ls = file.readlines()
        length = int(ls[1].strip("\n"))
        width = int(ls[3].strip("\n"))
else:
    length = 16
    width = 10
    
starttime = 0
last = []
last2 = []
current = []
counter = 0
diss = 0
winseted = False

li1 = []
for e in range(int(length * width // 2)):
    li1.append(randint(1,8))
li1 *= 2
shuffle(li1)

win = Tk()
win.title("连连看 -- By lanlan2_")
win.geometry("+200+300")
win.config(bg="AliceBlue")
win.attributes("-topmost", 1)
win.resizable(0, 0)
win.iconbitmap("images/icon.ico")

img1 = PhotoImage(file="images/5.png")
img2 = PhotoImage(file="images/8.png")
img3 = PhotoImage(file="images/11.png")
img4 = PhotoImage(file="images/12.png")
img5 = PhotoImage(file="images/13.png")
img6 = PhotoImage(file="images/14.png")
img7 = PhotoImage(file="images/18.png")
img8 = PhotoImage(file="images/25.png")

f_st = Frame(win)
f_st.pack(expand=True,fill=BOTH)
f_mn = Frame(win)

lab1 = Label(f_st, text="连连看 V0.7.6", font="consolas 32 bold")
lab1.pack()

"""
sca1 = Scale(f_st,
             label="长度设置",
             from_=0,
             to=100,
             tickinterval=10,
             length=200,
             resolution=2,
             orient="horizontal")
sca1.pack()
sca2 = Scale(f_st,
             label="宽度设置",
             from_=0,
             to=100,
             tickinterval=10,
             length=200,
             resolution=1,
             orient="horizontal")
sca2.pack()
"""

but1 = Button(f_st, text="开始",
                relief=GROOVE,
                bg="LightBlue",
                activebackground="DeepSkyBlue",
                font="consolas 32 bold")
    
but1.pack(ipadx=10)

def setwin():
    global winseted
    if winseted == False:
        win.minsize(win.winfo_width(), win.winfo_height())
        winseted = True

def setcurrent(text):
    global length, width, last, last2, current, counter, diss, starttime
    setwin()
    if current == []:
        current = text.split()
        last2 = current
        globals()["but"+current[0]+"_"+current[1]]["relief"] = "sunken"
        counter += 1
    else:
        if current != text.split():
            last = current
            current = text.split()
            last2 = last
            globals()["but"+current[0]+"_"+current[1]]["relief"] = "sunken"
            counter += 1
            if counter % 2 == 0:
                if globals()["but"+last[0]+"_"+last[1]]["image"][-1] == globals()["but"+current[0]+"_"+current[1]]["image"][-1]:
                    globals()["but"+last[0]+"_"+last[1]].grid_forget()
                    globals()["but"+current[0]+"_"+current[1]].grid_forget()
                    diss += 2
                    if diss == length * width:
                        win.withdraw()
                        usedtime = time() - starttime
                        score = int(((length * width) / usedtime) * 10000)
                        showinfo("提示", "恭喜，您完成了连连看！\n用时：%f秒\n分数：%d" %(usedtime, score))
                        win.destroy()
                else:
                    globals()["but"+current[0]+"_"+current[1]]["relief"] = "raised"
                    globals()["but"+last[0]+"_"+last[1]]["relief"] = "raised"
                    globals()["but"+last2[0]+"_"+last2[1]]["relief"] = "raised"
                    current = []


index = 0
for i in range(width):
    for j in range(length):
        vars()["but"+str(i)+"_"+str(j)] = Button(f_mn, bg="Black",
                                                 bd=2,
                                                 activebackground="Black",
                                                 image=vars()["img"+str(li1[index])],
                                                 text="%d %d" %(i, j),
                                                 command=lambda text="%d %d" %(i, j): setcurrent(text))
        vars()["but"+str(i)+"_"+str(j)].grid(row=i, column=j)
        index += 1

def changeui(event):
    global starttime
    f_st.pack_forget()
    f_mn.pack(expand=True,fill=BOTH)
    starttime = time()


but1.bind("<ButtonRelease-1>", changeui)
win.mainloop()
