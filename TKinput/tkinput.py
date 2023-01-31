from tkinter import *

def safeInput():
    pinq = Tk()
    pinq.title('Enter pin')
    pinq.geometry('190x290')
    pinq['bg'] = 'cyan'
    inputq = ''

    def qqww(): print(inputq)

    def clear():
        nonlocal inputq
        inputq = ''
        entry.config(state="normal")
        entry.delete(0,END)
        entry.config(state="readonly")

    def add(n):
        nonlocal entry
        nonlocal inputq
        inputq += str(n)
        entry.config(state="normal")
        entry.delete(0,END)
        entry.insert(0, inputq)
        entry.config(state="readonly")
        
    def ret():
        pinq.destroy()

    entry = Entry(pinq, width=25)
    entry.place(x=16, y=5)

    Button(pinq, command=qqww, text='More', bg='yellow').place(x=350, y=220)
    Button(pinq, command=lambda: add(1), text='1', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=10, y=30)
    Button(pinq, command=lambda: add(2), text='2', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=30)
    Button(pinq, command=lambda: add(3), text='3', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=130, y=30)
    Button(pinq, command=lambda: add(4), text='4', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=10, y=95)
    Button(pinq, command=lambda: add(5), text='5', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=95)
    Button(pinq, command=lambda: add(6), text='6', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=130, y=95)
    Button(pinq, command=lambda: add(7), text='7', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=10, y=160)
    Button(pinq, command=lambda: add(8), text='8', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=160)
    Button(pinq, command=lambda: add(9), text='9', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=130, y=160)
    Button(pinq, command=lambda: add(0), text='0', width=5, bg='lemon chiffon', activebackground='orange',
           height=3).place(x=70, y=225)
    Button(pinq, command=lambda: clear(), text='Reset', width=5, bg='light grey', activebackground='grey',
           height=3).place(x=10, y=225)
    Button(pinq, command=lambda: ret(), text='Готово', width=5, bg='light grey', activebackground='grey',
           height=3).place(x=130, y=225)

    pinq.wait_window()  # Ждем уничтожения окна
    return inputq

def run(quest, typeOf='Any'):
    tkinp = Tk()
    tkinp.geometry('200x100')
    tkinp['bg'] = 'cyan'
    tkinp.resizable(0, 0)
    tkinp.title('Enter')

    var = StringVar(tkinp)
    entryIn = Entry(tkinp, textvariable=var)
    entryIn.place(x=10, y=70, width=180)
    entryIn.focus()

    Label(tkinp, text=f'{quest}:', bg='cyan').place(x=10, y=40)
    Label(tkinp, text=f'Тип: {typeOf}', bg='cyan').place(x=10, y=20)

    result = None
    def end(event):
        nonlocal result
        result = var.get()  # Записываем результат в переменную result внешней функции
        tkinp.destroy()  # Уничтожаем окно

    tkinp.bind('<Return>', end)
    tkinp.wait_window()  # Ждем уничтожения окна
    return result  # Возвращаем результат

# print(run('Вопрос'))
print(safeInput())