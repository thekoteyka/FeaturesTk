import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
from tkinter import messagebox as mb

from playsound import playsound

# !! Use playsound v1.2.2 !!

# u can use   pip install -r r.txt   to install all requarement libraries

# Анимация оплаты в Apple, для Touch ID используйте Enter
# (c) Apple

close_after_pay = True

def usePay() -> bool:
    """
    Запустить оплату, создав новое окно

    return:

    True если оплата произведена; False если отменена нажатим BackSpase
    """
    class ImageLabel(tk.Label):
        """a label that displays images, and plays them if they are gifs"""
        def load(self, im):
            self.im = im
            if isinstance(self.im, str):
                self.im = Image.open(self.im)
                self.ph = ImageTk.PhotoImage(self.im)
            self.loc = 40
            self.frames = []

            try:
                for i in count(1):
                    self.frames.append(ImageTk.PhotoImage(master=root_pay, image=self.im.copy()))
                    self.im.seek(i)
            except EOFError:
                pass

            try:
                self.delay = self.im.info['duration']
            except:
                self.delay = 100

            if len(self.frames) == 1:
                self.config(image=self.frames[0])
            else:
                self.config(image=self.frames[0])

        def unload(self):
            self.config(image="")
            self.frames = None

        def next_frame(self):
            root_pay.unbind('<BackSpace>')
            if self.frames: 
                if self.loc == len(self.frames) - 57:
                    playsound('apple-pay-succes.mp3', False)
                if self.loc == len(self.frames) - 8:
                    self.config(image=self.frames[len(self.frames)-8])
                    nonlocal payed
                    payed = True
                    if close_after_pay:
                        root_pay.destroy()
                else:
                    self.loc += 1
                    self.config(image=self.frames[self.loc])
                    self.after(self.delay, self.next_frame)

    pressed_times = 0
    payed = False

    def pay(q=None):
        nonlocal pressed_times
        if pressed_times == 0:
            lbl.next_frame()
        pressed_times += 1

    def cancel(q=None):
        root_pay.destroy()

    def on_closing():
        mb.showinfo('Помощь', 'Для отмены нажмите Backspace\nДля оплаты удерживайте Return (Enter)')
        try:
            root_pay.focus_force()
        except:
            pass

    root_pay = tk.Tk()
    root_pay.title('Pay')
    root_pay.eval('tk::PlaceWindow . center')
    root_pay.resizable(False,  False)
    root_pay.iconbitmap('apple.ico')
    lbl = ImageLabel(root_pay)
    lbl.pack()
    lbl.load('pay.gif')

    root_pay.protocol("WM_DELETE_WINDOW", on_closing)
    root_pay.bind('<BackSpace>', cancel)
    root_pay.bind('<Return>', pay)


    root_pay.wait_window() 
    return payed

if __name__ == '__main__':
    def payNow():
        payed = usePay()
        print(payed)

    root = tk.Tk()
    q = tk.StringVar()
    tk.Button(text='Pay!', command=payNow, width=5, height=5, bg='cyan').pack()
    root.mainloop()