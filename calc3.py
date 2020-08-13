#!/usr/bin/env python3


import tkinter as tk

calc = tk.Tk()

calc.title("Simple Calculator")
calc.geometry("420x370")

label = tk.Label(calc, text="", width=40, height=5, foreground='black', anchor='se', font="Times 20 bold")
textbox = tk.Entry(calc, width=40, background='white')

strt = ""  # stores the value for the  label which displays the present scenario
flag = 0  # allows clearing of screen off previous results when staring a new operation...


def changes(a):
    global strt
    global flag
    if (a != 'z'):
        if (flag == 1 and a not in ['+', '-', '/', 'x',
                                    '^']):  # clears previous result as new expression is being entered
            label["text"] = ""
        flag = 0
        label["text"] = label["text"] + a
        strt = label["text"]
    else:

        strt = strt[:-1]
        label["text"] = strt


def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == 'x' or op == '/' or op == '^':
        return 2
    return 0


def applyOp(a, b, op):
    if op == '+': return round(a + b, 4)
    if op == '-': return round(a - b, 4)
    if op == 'x': return round(a * b, 4)
    if op == '/': return round(a / b, 4)
    if op == '^': return round(a ** b, 4)


def clearscr():
    label["text"] = ""


def process():
    global strt  # strt has the entire string...
    global flag

    values = []  # stack to hold the values
    ops = []  # stack to hold the operators
    nextisneg = 0
    i = 0
    minus = 0
    print("length of strt: ", len(strt), strt)
    if (len(strt) < 3):
        print("no operations entered!!!")
        return

    while i < len(strt):

        print("i: ", i)

        if strt[0] == '-' and minus == 0:
            minus = 1
            i += 1
            continue

        if strt[i] == '(':
            ops.append(strt[i])
            print("braces found")

        elif strt[i].isdigit():
            val = 0
            dot = 0  # to check if a dot was encountered or not
            c = 1  # for the precision control
            while i < len(strt) and strt[i] not in ['+', '-', '/', 'x', '^', '(', ')']:
                if (strt[i] != '.'):
                    if (dot == 0):
                        val = val * 10 + float(strt[i])

                    elif (dot == 1):
                        if (c < 5):
                            val = val + float(strt[i]) / (10 ** c)
                            c += 1


                elif (strt[i] == '.'):
                    dot = 1
                i += 1

            i -= 1

            if (minus == 1 or nextisneg == 1):
                values.append(-val)
                minus = 2
                nextisneg = 0
            else:
                values.append(val)
            print("after append: ", val, ": ", values)
            print("ops is: ", ops)


        elif strt[i] == ')':

            print("close braces")
            while (len(ops) != 0 and ops[-1] != '('):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(applyOp(val1, val2, op))

            ops.pop()


        else:
            # While top of 'ops' has same or  greater precedence to current token,
            # which is an operator. Apply operator on top of 'ops' to top two elements in values stack.
            print("new operator to be added: ", strt[i])
            while (len(ops) != 0 and precedence(ops[-1]) >= precedence(strt[i]) and strt[i] in ['+', '-', '/', 'x']):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))
                print("after append: ", val, ": ", values)
                print("after removing: ", op, ": ", ops)

            ops.append(strt[i])  # appends the operations
            if (strt[i + 1] == '-'):
                nextisneg = 1
                i += 1

            print(ops)
        i += 1

    while len(ops) != 0:
        print("in here")
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()

        values.append(applyOp(float(val1), float(val2), op))
        print(values)

    label['text'] = str(values[-1])
    strt = label['text']
    print(values)
    print(ops)
    flag = 1


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
calc.bind('1', lambda event: changes('1'))
_2 = tk.Button(line1, text="2", height=2, width=7, command=lambda: changes('2'))
calc.bind('2', lambda event: changes('2'))
_3 = tk.Button(line1, text="3", height=2, width=7, command=lambda: changes('3'))
calc.bind('3', lambda event: changes('3'))
_LB = tk.Button(line1, text="(", height=2, width=7, command=lambda: changes('('))
calc.bind('(', lambda event: changes('('))

_4 = tk.Button(line2, text="4", height=2, width=7, command=lambda: changes('4'))
calc.bind('4', lambda event: changes('4'))
_5 = tk.Button(line2, text="5", height=2, width=7, command=lambda: changes('5'))
calc.bind('5', lambda event: changes('5'))
_6 = tk.Button(line2, text="6", height=2, width=7, command=lambda: changes('6'))
calc.bind('6', lambda event: changes('6'))
_RB = tk.Button(line2, text=")", height=2, width=7, command=lambda: changes(')'))
calc.bind(')', lambda event: changes(')'))

_7 = tk.Button(line3, text="7", height=2, width=7, command=lambda: changes('7'))
calc.bind('7', lambda event: changes('7'))
_8 = tk.Button(line3, text="8", height=2, width=7, command=lambda: changes('8'))
calc.bind('8', lambda event: changes('8'))
_9 = tk.Button(line3, text="9", height=2, width=7, command=lambda: changes('9'))
calc.bind('9', lambda event: changes('9'))
_dot = tk.Button(line3, text='.', height=2, width=7, command=lambda event: changes('.'))
calc.bind('.', lambda event: changes('.'))

_pow = tk.Button(line4, text="^", height=2, width=7, command=lambda: changes('^'))
_pow.bind('^', lambda event: changes('^'))
_0 = tk.Button(line4, text="0", height=2, width=7, command=lambda: changes('0'))
calc.bind('0', lambda event: changes('0'))
_equal = tk.Button(line4, text="=", height=2, width=7, bg='lightgreen', command=lambda: process())
calc.bind("<Return>", lambda event: process())
_minus = tk.Button(line2, text='-', height=2, width=7, command=lambda: changes('-'))
calc.bind('-', lambda event: changes('-'))
_add = tk.Button(line1, text='+', height=2, width=7, command=lambda: changes('+'))
calc.bind('+', lambda event: changes('+'))
_prod = tk.Button(line3, text='x', height=2, width=7, command=lambda: changes('x'))
calc.bind('*', lambda event: changes('x'))
_div = tk.Button(line4, text='/', height=2, width=7, command=lambda: changes('/'))
calc.bind('/', lambda event: changes('/'))
_clear = tk.Button(line4, text="clear", height=2, width=7, command=clearscr)
calc.bind("<Delete>", lambda event: clearscr())
calc.bind("<BackSpace>", lambda event: changes('z'))

_1.pack(fill=tk.BOTH, side='left')
_2.pack(fill=tk.BOTH, side='left')
_3.pack(fill=tk.BOTH, side='left')
_add.pack(fill=tk.BOTH, side='left')
_LB.pack(fill=tk.BOTH, side='left')

_4.pack(fill=tk.BOTH, side='left')
_5.pack(fill=tk.BOTH, side='left')
_6.pack(fill=tk.BOTH, side='left')
_minus.pack(fill=tk.BOTH, side='left')
_RB.pack(fill=tk.BOTH, side='left')

_7.pack(fill=tk.BOTH, side='left')
_8.pack(fill=tk.BOTH, side='left')
_9.pack(fill=tk.BOTH, side='left')
_prod.pack(fill=tk.BOTH, side='left')
_dot.pack(fill=tk.BOTH, side='left')

_0.pack(fill=tk.BOTH, side='left')
_clear.pack(fill=tk.BOTH, side='left')
_equal.pack(fill=tk.BOTH, side='left')
_div.pack(fill=tk.BOTH, side='left')
_pow.pack(fill=tk.BOTH, side='left')

calc.mainloop()


