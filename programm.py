from SPAK import*
from tkinter import *  
from tkinter import Menu  
from tkinter import ttk  
from tkinter.ttk import Checkbutton
import re
now_col1=2
now_col2=2
straight_vel = []
kriv_vel = []
  
window = Tk()  
window.title("ProgrammPython-EPE")  
window.geometry('600x400')  

menu = Menu(window)  
new_item = Menu(menu,tearoff=0)  
new_item.add_command(label='Новый')  
new_item.add_separator()  
new_item.add_command(label='Добавить')  
menu.add_cascade(label='История экспериментов', menu=new_item)  
new_item1 = Menu(menu,tearoff=0)  
chk_state = BooleanVar()  
chk_state.set(True)
new_item1.add_checkbutton(label='Построение графиков',var=chk_state)
menu.add_cascade(label='Настройки', menu=new_item1)  
menu.add_command(label="Выйти",command=window.destroy)

    
tab_control = ttk.Notebook(window)  
tab1 = Frame(tab_control,bd=5)
def is_valid(newval):
    result=  not(re.search(r'[^a-zA-Z0-9]', newval) is not None) and (len(newval)<2 or (not(re.search(r'[^a-zA-Z]', newval[0:len(newval)-2]) is not None) and( not newval[-2].isdigit() or newval[-1].isdigit()) ))
    for i in range(len(straight_vel)):
        if straight_vel[i].get()==newval:
            result = False
            break
    return result
check = (tab1.register(is_valid), "%P")
def add_new_vel():
    global now_col1
    global straight_vel
    butnew = Label(tab1,text = 'Величина №'+str(1+(now_col1-2)//4)+'  Обозначение')
    butnew.grid(column = 0,row = now_col1)  
    var = StringVar() 
    straight_vel.append(var)
    phone_entry = Entry(tab1,validate="key", validatecommand=check,textvariable=var) 
    phone_entry.grid(column = 0, row = now_col1+1)  
    now_col1+=4
tab2 = Frame(tab_control,bd=5)  
tab3 = Frame(tab_control,bd=5)
tab4 = Frame(tab_control,bd=5)
tab5 = Frame(tab_control,bd=5)
tab_control.add(tab1, text = 'Прямые измерения')  
tab_control.add(tab2, text='Косвенные измерения') 
tab_control.add(tab3, text='Результаты измерений') 
tab_control.add(tab4, text='Погрешности измерений') 
tab_control.add(tab5, text='График') 

lbl1 = Label(tab1, text='Добавить Новую величину прямого измерения')  
lbl1.grid(column=0, row=0)  
button1=Button(tab1,text=u'+', command = add_new_vel)
button1.grid(column=2,row=0)
lbl2 = Label(tab2, text='Вкладка 2')  
lbl2.grid(column=0, row=0)  

tab_control.pack(expand=1, fill='both')  
window.config(menu=menu)  
window.mainloop()
                     

    