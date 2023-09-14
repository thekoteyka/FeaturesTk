from tkinter import *
from threading import Thread

class ProgressBar:
    def __init__(self, window, bg:str, x:int, y:int, lenght:int, max_value:int) -> None:

        max_value += 3

        self.window = window
        self.marker_value = 0
        self.real_value = 0
        self.max = max_value
        self.canvas = None

        # 300x200+52+52
        self.canvas = Canvas(window, bg='white', highlightthickness=0)
        self.canvas.place(x=x, y=y, height=20, width=x+lenght)

        canvas = self.canvas

        canvas.create_rectangle(0, 0, x+lenght, 20,
                                              fill=bg,
                                              outline='lightgray',
                                              width=4)
        
        self.value_in_pixel = lenght / max_value
        print(self.value_in_pixel)

        self.marker = canvas.create_rectangle(4, 4, 16, 16, fill='purple', width=0)

    def _true_position(self, val):
        return int(self.value_in_pixel * val)
        return val
    
    def _go(self):
        if self._true_position(self.real_value) < self.marker_value:
            while self._true_position(self.real_value) < self.marker_value:
                self._move(-1)
                self.marker_value = self.canvas.coords(self.marker)[0]

                realvalue_lbl.configure(text=f'Real Value: {self.real_value}')
                markervalue_lbl.configure(text=f'Marker Value: {int(self.marker_value)}')

        elif self._true_position(self.real_value) > self.marker_value:
            while self._true_position(self.real_value) > self.marker_value:
                self._move(1)
                self.marker_value = self.canvas.coords(self.marker)[0]

                realvalue_lbl.configure(text=f'Real Value: {self.real_value}')
                markervalue_lbl.configure(text=f'Marker Value: {int(self.marker_value)}')
    
    def _move(self, x:int):
        self.canvas.move(self.marker, x, 0)
        self.window.update()
        self.window.after(5)
    
    def set_value(self, value:int):
        self.real_value = value
        self._go()



BG = 'gray60'

root = Tk()
root.geometry('300x200')
root['bg'] = BG
root.resizable(False, False)
s = ProgressBar(root, BG, 10, 20, 250, 100)

realvalue_lbl = Label(text='Real Value: 0')
markervalue_lbl = Label(text='Marker Value: 0')
realvalue_lbl.place(x=5, y=100)
markervalue_lbl.place(x=5, y=121)

s.set_value(100)
s.set_value(2)

for i in range(5):
    s.set_value(30)
    s.set_value(2)




    root.mainloop()
