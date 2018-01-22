#!/usr/bin/env python
# -*- coding:utf-8 -*-
import Tkinter
root = Tkinter.Tk()
root.overrideredirect(True)
#root.attributes("-alpha", 0.3)窗口透明度70 %
root.attributes("-alpha", 0.4)#窗口透明度60 %
root.geometry("300x200+10+10")
canvas = Tkinter.Canvas(root)
canvas.configure(width = 300)
canvas.configure(height = 200)
canvas.configure(bg = "blue")
canvas.configure(highlightthickness = 0)
canvas.pack()
x, y = 0, 0
def move(event):
    global x,y
    new_x = (event.x-x)+root.winfo_x()
    new_y = (event.y-y)+root.winfo_y()
    s = "300x200+" + str(new_x)+"+" + str(new_y)
    root.geometry(s)
    print("s = ",s)
    print(root.winfo_x(),root.winfo_y())
    print(event.x,event.y)
    print()
def button_1(event):
    global x,y
    x,y = event.x,event.y
    print("event.x, event.y = ",event.x,event.y)
canvas.bind("<B1-Motion>",move)
canvas.bind("<Button-1>",button_1)
root.mainloop()

# import sys
# from PyQt4 import QtGui, QtCore

# class Trans(QtGui.QWidget):

#     def __init__(self):
#         super(Trans, self).__init__()
#         self.initUI()
#         button = QtGui.QPushButton('Close', self)
#         self.connect(button, QtCore.SIGNAL('clicked()'), QtGui.qApp,
#                      QtCore.SLOT('quit()'))

#     def initUI(self):
#         #self.setAttribute(QtCore.Qt.WA_NoSystemBackground, False)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
#         self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#     trans = Trans()
#     trans.show()
#     sys.exit(app.exec_())

# import sys,time
# import os.path
# from PyQt4 import QtGui, QtCore, QtWebKit
# from PIL import ImageGrab

# im = ImageGrab.grab((300, 100, 1400, 600))

# im.save('testt/testJt3.jpeg','jpeg')