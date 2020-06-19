
import tkinter as tk
calc = tk.Tk()

calc.title("Simple Calculator")
calc.geometry("350x370")




label = tk.Label(calc, text="", width=40, height=5, foreground='black' , anchor='se', font="Times 20 bold")


strt=""
def changes(a):
 if(a!='='):

   label["text"] = label["text"]+a
   global strt
   strt = label["text"]



def clearscr():
    label["text"] = ""

def process():
    global strt
    print("processing", len(strt))
    for i in range(len(strt) - 1):
        if (strt[i] == '+' or strt[i] == '-' or strt[i] == 'x'):
            equal(strt[:i], strt[i], strt[i + 1:])
            print("solved!!!")


try:
 def equal(a,b,c):
   if(b=='+'):
    label["text"] = str(int(a)+int(c))
    #strt=""

   if(b=='-'):
    label["text"] = str(int(a)-int(c))
    #strt=""

   if(b=='x'):
    label["text"] = str(int(a)*int(c))
    #strt=""
   if(b=='/'):
    label["text"] = str(int(a)/int(c))

except:
    None


textbox = tk.Entry(calc, width=40, background='white')
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
_2 = tk.Button(line1, text="2", height=2, width=7, command=lambda: changes('2'))
_3 = tk.Button(line1, text="3", height=2, width=7, command=lambda: changes('3'))
_4 = tk.Button(line2, text="4", height=2, width=7, command=lambda: changes('4'))
_5 = tk.Button(line2, text="5", height=2, width=7, command=lambda: changes('5'))
_6 = tk.Button(line2, text="6", height=2, width=7, command=lambda: changes('6'))
_7 = tk.Button(line3, text="7", height=2, width=7, command=lambda: changes('7'))
_8 = tk.Button(line3, text="8", height=2, width=7, command=lambda: changes('8'))
_9 = tk.Button(line3, text="9", height=2, width=7, command=lambda: changes('9'))
_0 = tk.Button(line4, text="0", height=2, width=7, command=lambda: changes('10'))


_equal = tk.Button(line4, text="=", height=2, width=7, bg='lightgreen' , command=process)
_minus = tk.Button(line2, text='-', height=2, width=7, command=lambda: changes('-'))
_add = tk.Button(line1, text='+', height=2, width=7, command=lambda: changes('+'))
_prod = tk.Button(line3, text='x', height=2, width=7, command=lambda: changes('x'))
_div = tk.Button(line4, text='/', height=2, width=7, command=lambda: changes('/'))
_clear = tk.Button(line4, text="clear", height=2, width=7, command=clearscr)


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


