from tkinter import *
import json

loggined = False

def shake_now(window):
    '''
    Трясёт окно
    '''
    # Danger Zone, dont change anything in this area ===
    velocity = 0  # Ускорение для вектора движения окна, не менять значение для корректной работы
    y = window.winfo_y()  # Получаем координаты окна относительно начала координат на мониторе (левый верхний край)
    # ==================================================

    # Settings ------------

    # Насколько сильной будет тряска, эксперементируйте. Должно быть чётным
    POWER = 4

    # ---------------------

    # Checking Zone 
    assert(POWER % 2 == 0) # POWER must be even
    #

    def go():  # Движение
        x = window.winfo_x()  # Координаты окна
        window.wm_geometry(f'300x200+{velocity+x}+{y}')  # Изменяем местоположение окна, добавляя к позиции <x>
                                                                            # текущее ускорение
        window.after(1)  # Чуть чуть ждём для плавности
        window.update()  # Обновляем позицию окна (Важно)

    def go_right():  # Движение направо
        nonlocal velocity
        for i in range(POWER):
            
            if i >= POWER / 2:  # Если уже дошли до середины, начинаем сбрасывать ускорение, чтобы замедлить движения для плавной остановки
                velocity -= 2  # Уменьшаем на 2 тк go_left делает в 2 раза больше, и чтобы уравнять нужно так
            else:              # Если ещё не дошли, ускоряемся, увеличивая скорость движения окна
                velocity += 2
            go()

    def go_left():  # Движение налево
        nonlocal velocity
        for i in range(POWER*2):  # Едем в 2 раза больше, ведь нам нужно не только вернуться в первоначальную точку, но и уехать ещё левее
            if i >= POWER: # Тут серединой будет POWER, ведь мы едем в 2 раза больше
                velocity += 1
            else:
                velocity -= 1
            go() # Двигаемся с конкретным ускорением, velocity

    def go_right_double():
        nonlocal velocity
        for i in range(POWER*2):
            if i >= POWER:     # Если уже дошли до середины, начинаем сбрасывать ускорение, чтобы замедлить движения для плавной остановки
                velocity -= 1  # Уменьшаем на 2 тк go_left делает в 2 раза больше, и чтобы уравнять нужно так
            else:              # Если ещё не дошли, ускоряемся, увеличивая скорость движения окна
                velocity += 1
            go()

        

    # Как функция меняет положение:
    # [] = Окно             | = Центр, то есть откуда начали тряску
    go_right() #         |        []
    go_left()  #  []     |          
    go_right_double()
    go_left()
    go_right()


def _login(_access=None):
    user = None
    def send():
        nonlocal user
        nonlocal usernameVar, passwordVar 
        username = usernameVar.get()
        password = passwordVar.get()
        userF = find_user(username, password)

        if userF:
            global loggined
            loggined = True
            user = userF
            loginRoot.destroy()

    def find_user(userToCheck, passwordToCheck):
        with open('data.json', 'r') as f:
            users = json.load(f)
            for user in users:
                if user == userToCheck:
                    if users[user]['password'] == passwordToCheck:
                        data_user = users[user]
                        data_user['user'] = user
                        return data_user
            return None

    def register():
        reg = Tk()
        reg.title('Register')
        reg['bg'] = BG
        reg.eval('tk::PlaceWindow . center')
        reg.geometry('300x200')

        def allow_access():
            nonlocal adminB, vipB, accessBtn
            if _login(True)['role'] == 'admin':
                adminB['state'] = NORMAL
                vipB['state'] = NORMAL
                accessBtn.destroy()

        def createUser():
            name = usernameVar.get()
            password = passwordVar.get()
            role = roleVar.get()

            with open('data.json') as f:
                data = json.load(f)

            if name.replace(' ', '') == '':
                shake_now(reg)
                return
            if 'w' in data:
                shake_now(reg)
                return
            if role == '':
                shake_now(reg)
                return

            data[name] = {'password': password, 'role': role}

            with open('data.json', 'w') as f:
                json.dump(data, f)
        
        roleVar = StringVar(reg)
        usernameVar = StringVar(reg)
        passwordVar = StringVar(reg)

        Label(reg, text='Уровень доступа:', bg=BG, font='Arial 13').place(x=5,  y=0)
        Label(reg, text='Логин:', font='Arial 12', bg=BG).place(x=5, y=115)
        Label(reg, text='Пароль:', font='Arial 12', bg=BG).place(x=5, y=145)


        adminB = Radiobutton(reg, bg=BG, text='Администратор', variable=roleVar, activebackground=BG, value='admin', font='Arial 13', state=DISABLED)
        adminB.place(x=5, y=25)

        vipB = Radiobutton(reg, bg=BG, text='Премиум пользователь', variable=roleVar, activebackground=BG, value='vip', font='Arial 13', state=DISABLED)
        vipB.place(x=5, y=55)

        Radiobutton(reg, bg=BG, text='Пользователь', variable=roleVar, activebackground=BG, value='user', font='Arial 13').place(x=5, y=85)


        accessBtn = Button(reg, text='Назначить права', bg=BG_BTN, activebackground=BG, command=allow_access)
        accessBtn.place(x=170, y=5)

        Entry(reg, width=25, textvariable=usernameVar).place(x=70, y=117)
        Entry(reg, width=25, textvariable=passwordVar).place(x=70, y=147)

        Button(reg, text='Готово', bg=BG_BTN, activebackground=BG, width=20, command=createUser).place(x=73, y=170)
        


    BG = 'gray60'
    BG_BTN = 'gray70'
    ALLOW_REGISTER = True
    ADMIN_PASSWORD = '32725'
    
    loginRoot = Tk()
    loginRoot.title('Login')
    loginRoot['bg'] = BG
    loginRoot.eval('tk::PlaceWindow . center')

    usernameVar = StringVar(loginRoot)
    passwordVar = StringVar(loginRoot)

    if _access:
        ALLOW_REGISTER = False
        Label(loginRoot, text='Войдите админом', font='Arial 17', bg=BG).place(x=0, y=5)
    else:
        Label(loginRoot, text='Войдите в аккаунт', font='Arial 17', bg=BG).place(x=0, y=5)

    Label(loginRoot, text='Логин:', font='Arial 12', bg=BG).place(x=5, y=40)
    Label(loginRoot, text='Пароль:', font='Arial 12', bg=BG).place(x=5, y=95)

    Entry(loginRoot, width=25, textvariable=usernameVar).place(x=5, y=70)
    Entry(loginRoot, width=25, textvariable=passwordVar).place(x=5, y=120)

    Button(loginRoot, text='Готово', width=25, bg=BG_BTN, activebackground=BG, command=send).place(x=5, y=160)

    if ALLOW_REGISTER:
        reg_btn = Button(loginRoot, text='Регистрация', bg=BG_BTN, activebackground=BG, command=register)
        reg_btn.place(x=115, y=38)

    loginRoot.wait_window()
    return user

def login_required(func):

    if loggined:
        func()
    else:
        _login()
        if loggined:
            func()
            

@login_required
def add():
    print(1)
