'''class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other


item_1 = Item('Монитор', 20_000, 5)
item_2 = Item('Видеокарта', 15_000, 0.8)
# print(item_1.price + 5000)
print(item_1 + 10)
# print(type(500), isinstance(500, Item), sep='\n')'''


from tkinter import *
from random import randint


window = Tk()
window.geometry('600x600')
canvas = Canvas(window, width=600, height=600)
canvas.pack()


class Fire:
    image = PhotoImage(file='fire.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay


class Earth:
    image = PhotoImage(file='earth.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay


class Wind:
    image = PhotoImage(file='wind.png').subsample(4, 4)


class Water:
    image = PhotoImage(file='water.png').subsample(4, 4)


class Clay:
    image = PhotoImage(file='clay.png').subsample(4, 4)


def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_id) == 2:
        elem_1 = elements[images_id[0] - 1]
        elem_2 = elements[images_id[1] - 1]
        new_elem = elem_1 + elem_2
        if new_elem and new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)
    canvas.coords(images_id, event.x, event.y)


elements = [Fire(), Water(), Wind(), Earth()]
for elem in elements:
    canvas.create_image(randint(50, 350), randint(50, 350), image=elem.image)

window.bind('<B1-Motion>', move)

window.mainloop()

























