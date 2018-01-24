#!/usr/bin/env python
# -*- coding:utf-8 -*-
import Tkinter
from Tkinter import *
from PIL import ImageGrab


root = Tkinter.Tk()
root.overrideredirect(True)
#root.attributes("-alpha", 0.3)窗口透明度70 %
root.attributes("-alpha", 0.2)#窗口透明度60 %
root.geometry("300x200+0+0")
canvas = Tkinter.Canvas(root)
canvas.configure(width = 300)
canvas.configure(height = 200)
# canvas.configure(bg = "blue")
canvas.configure(borderwidth = 30)
# canvas.configure(highlightthickness = 3)
canvas.pack()
x, y = 0, 0
# x1,x2,y1,y2 = 0,0,0,0
# lx,ly = 0, 0
new_x,new_y= 0,0


def move(event):
    global x,y,new_x,new_y
    new_x = (event.x-x)+root.winfo_x()
    new_y = (event.y-y)+root.winfo_y()
    s = "300x200+" + str(new_x)+"+" + str(new_y)
    root.geometry(s)
    # lx = new_x
    # ly = new_y


    print("s = ",new_x,new_y)
    # print(root.winfo_x(),root.winfo_y())

    # print(event.x,event.y)
    # print()
def button_1(event):
    global x,y
    x,y = event.x,event.y
    print("event.x, event.y = ",event.x,event.y)

	# ima = ImageGrab.grab()
	# ima.save('addr.jpeg','jpeg')
    
def key(event,path,funct):
	global new_x,new_y,img_path
	ima = ImageGrab.grab((new_x,new_y,600,400))
	ima.save(path,'jpeg')
    funct(path)
	print 'save success'
    # funct(path)
    # print "pressed",ima

def keyAdaptor(fun, outerfun, **kwds):  
    '''''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''  
    return lambda event,fun=fun, outerfun=outerfun ,kwds=kwds: fun(event, **kwds)  

def screenshot(func,ipath):
	
	# global img_path 
	# img_path = path

	canvas.bind("<B1-Motion>",move)
	canvas.bind("<Button-1>",button_1)
	canvas.bind("<Double-Button-1>",keyAdaptor(key, path = ipath,funct = func))

	root.mainloop()
