from tkinter import *

loggined = False

def _login():
    def send():
        nonlocal usernameVar, passwordVar 
        username = usernameVar.get()
        password = passwordVar.get()
        if check_data(username, password):
            user = {'username': username, 'password': password}
            global loggined
            loggined = True
            loginRoot.destroy()
            return user

    def check_data(user, password):  # Later
        return True

    BG = 'gray60'
    
    loginRoot = Tk()
    loginRoot.title('Login')
    loginRoot['bg'] = BG
    loginRoot.eval('tk::PlaceWindow . center')

    usernameVar = StringVar(loginRoot)
    passwordVar = StringVar(loginRoot)
    Label(loginRoot, text='Войдите в аккаунт', font='Arial 17', bg=BG).place(x=0, y=5)
    Label(loginRoot, text='Логин:', font='Arial 12', bg=BG).place(x=5, y=40)
    Label(loginRoot, text='Пароль:', font='Arial 12', bg=BG).place(x=5, y=95)

    Entry(loginRoot, width=25, textvariable=usernameVar).place(x=5, y=70)
    Entry(loginRoot, width=25, textvariable=passwordVar).place(x=5, y=120)

    Button(loginRoot, text='Готово', width=25, bg='gray70', activebackground=BG, command=send).place(x=5, y=160)

    loginRoot.wait_window()

def login_required(func):

    if loggined:
        print(func())
    else:
        _login()

@login_required
def add():
    print(2)
    return 1
