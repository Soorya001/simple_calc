#!/usr/bin/env python3




import tkinter as tk
calc = tk.Tk()

calc.title("Simple Calculator")
calc.geometry("350x370")

label = tk.Label(calc, text="", width=40, height=5, foreground='black' , anchor='se', font="Times 20 bold")

strt=""                         #stores the value for the  label which displays the present scenario
flag=0                          #allows clearing of screen off previous results when staring a new operation...
def changes(a):
 global strt
 global flag
 if(a!='z'):
    if(flag==1 and a not in ['+','-','/','x']):
        label["text"] = ""
    flag = 0
    label["text"] = label["text"]+a
    strt = label["text"]
 else:
     #print("back")
     strt = strt[:-1]
     label["text"] = strt

def clearscr():
    label["text"] = ""

def process():
    global strt
    global flag
    for i in range(len(strt) - 1):
        if (strt[i] == '+' or strt[i] == '-' or strt[i] == 'x' or strt[i]=='/'):
            equal(strt[:i], strt[i], strt[i + 1:])
            print("solved!!!")
            flag = 1

try:
 def equal(a,b,c):
   if(b=='+'):
    label["text"] = str(float(a)+float(c))
    #strt=""

   if(b=='-'):
    label["text"] = str(float(a)-float(c))
    #strt=""

   if(b=='x'):
    label["text"] = str(float(a)*float(c))
    #strt=""
   if(b=='/'):
    label["text"] = str(float(a)/float(c))

   label['text'] = label['text']
except:
    None

textbox = tk.Entry(calc, width=40, background='white')
def OnReturn(event):
    print("Enter key pressed")
    strt = textbox.get()
    textbox.delete(0,tk.END)
    for i in range(len(strt) - 1):
        if (strt[i] == '+' or strt[i] == '-' or strt[i] == 'x' or strt[i]=='/'):
            equal(strt[:i], strt[i], strt[i + 1:])
            print("solved!!!")

textbox.bind("<Return>",OnReturn)

label.pack()
textbox.pack(fill=tk.X)

line1 = tk.Frame(calc)
line1.pack(side='top')

line2 = tk.Frame(calc)
line2.pack(side='top')

line3 = tk.Frame(calc)
line3.pack(side='top')

line4 = tk.Frame(calc)
line4.pack(side='top')

_1 = tk.Button(line1, text="1", height=2, width=7, command=lambda: changes('1'))
calc.bind('1',lambda event: changes('1'))
_2 = tk.Button(line1, text="2", height=2, width=7, command=lambda: changes('2'))
calc.bind('2',lambda event: changes('2'))
_3 = tk.Button(line1, text="3", height=2, width=7, command=lambda: changes('3'))
calc.bind('3',lambda event: changes('3'))
_4 = tk.Button(line2, text="4", height=2, width=7, command=lambda: changes('4'))
calc.bind('4',lambda event: changes('4'))
_5 = tk.Button(line2, text="5", height=2, width=7, command=lambda: changes('5'))
calc.bind('5',lambda event: changes('5'))
_6 = tk.Button(line2, text="6", height=2, width=7, command=lambda: changes('6'))           #code by soorya!!!
calc.bind('6',lambda event: changes('6'))
_7 = tk.Button(line3, text="7", height=2, width=7, command=lambda: changes('7'))
calc.bind('7',lambda event: changes('7'))
_8 = tk.Button(line3, text="8", height=2, width=7, command=lambda: changes('8'))
calc.bind('8',lambda event: changes('8'))
_9 = tk.Button(line3, text="9", height=2, width=7, command=lambda: changes('9'))
calc.bind('9',lambda event: changes('9'))
_0 = tk.Button(line4, text="0", height=2, width=7, command=lambda: changes('0'))
calc.bind('0',lambda event: changes('0'))


_equal = tk.Button(line4, text="=", height=2, width=7, bg='lightgreen' , command=process)
calc.bind("<Return>",lambda event: process())
_minus = tk.Button(line2, text='-', height=2, width=7, command=lambda: changes('-'))
calc.bind('-',lambda event: changes('-'))
_add = tk.Button(line1, text='+', height=2, width=7, command=lambda: changes('+'))
calc.bind('+',lambda event: changes('+'))
_prod = tk.Button(line3, text='x', height=2, width=7, command=lambda: changes('x'))
calc.bind('*',lambda event: changes('x'))
_div = tk.Button(line4, text='/', height=2, width=7, command=lambda: changes('/'))
calc.bind('/',lambda event: changes('/'))
_clear = tk.Button(line4, text="clear", height=2, width=7, command=clearscr)
calc.bind("<Delete>",lambda event: clearscr())
calc.bind("<BackSpace>",lambda event: changes('z'))

_1.pack(fill=tk.BOTH, side='left')
_2.pack(fill=tk.BOTH, side='left')
_3.pack(fill=tk.BOTH, side='left')
_add.pack(fill=tk.BOTH, side='left')

_4.pack(fill=tk.BOTH, side='left')
_5.pack(fill=tk.BOTH, side='left')
_6.pack(fill=tk.BOTH, side='left')
_minus.pack(fill=tk.BOTH, side='left')

_7.pack(fill=tk.BOTH, side='left')
_8.pack(fill=tk.BOTH, side='left')
_9.pack(fill=tk.BOTH, side='left')
_prod.pack(fill=tk.BOTH, side='left')

_0.pack(fill=tk.BOTH, side='left')
_clear.pack(fill=tk.BOTH, side='left')
_equal.pack(fill=tk.BOTH, side='left')
_div.pack(fill=tk.BOTH, side='left')

calc.mainloop()


