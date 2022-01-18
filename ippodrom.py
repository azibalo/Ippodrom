from tkinter import *
from tkinter import messagebox
from pygameip import init
root = Tk() #создание окна
root.title("Ипподром")  #изменение заголовка
root.geometry("500x500") #определение размеров окна
root.resizable(False, False) #запрещение изменения размеров
def getV(arg): #Запуск игры
    a = scale1.get()
    b = scale2.get()
    if b>a: 
        messagebox.showerror("Ошибка!", "Несуществующая лошадь...") #проверка на существование лошади
        return
    else:
        win=init(a) #запуск гонки
        if b==win: #проверка результата
            messagebox.showinfo("Результат", "Вы победили!")
        else:
            messagebox.showinfo("Результат", "Вы проиграли... Первой пришла лошадь №{}".format(win))

scale1 = Scale(root,orient=HORIZONTAL,length=300,from_=2,to=10,tickinterval=1,
               resolution=1)  #создание полосы прокрутки для выбора количества лошадей
lab1=Label(root,text='Количество лошадей',width=25,height=5,fg='black',font='arial 14')
scale2 = Scale(root,orient=HORIZONTAL,length=300,from_=1,to=10,tickinterval=1,
               resolution=1)
lab2=Label(root,text='Ставка на лошадь:',width=25,height=5,fg='black',font='arial 14') #создание полосы прокрутки для выбора лошади
button1 = Button(root,text=u"Начать гонку!") #создание кнопки
lab1.pack() #отображение всего
scale1.pack()
lab2.pack()
scale2.pack()
button1.pack()
button1.bind("<Button-1>",getV) #присваивание кнопке функции
root.mainloop()