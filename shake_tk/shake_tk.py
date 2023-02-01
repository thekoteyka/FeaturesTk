from tkinter import *

# Пример как сделать тряску окна Tkinter

window = Tk()

ROOT_SIZE_X = 300
ROOT_SIZE_Y = 200

window.geometry(f'{ROOT_SIZE_X}x{ROOT_SIZE_Y}')
window['bg'] = 'gray60'
window.title('Shake!')
window.resizable(False, False)

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
    POWER = 6

    # ---------------------

    # Checking Zone 
    assert(POWER % 2 == 0) # POWER must be even
    #

    def go():  # Движение
        x = window.winfo_x()  # Координаты окна
        window.wm_geometry(f'{ROOT_SIZE_X}x{ROOT_SIZE_Y}+{velocity+x}+{y}')  # Изменяем местоположение окна, добавляя к позиции <x>
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

        

    # Как функция меняет положение:
    # [] = Окно             | = Центр, то есть откуда начали тряску

    go_right() #         |        []
    go_left()  #  []     |          
    go_right() #         []

Button(text='Shake!', command=lambda: shake_now(window)).place(x=5, y=20)

window.mainloop()