import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# sys.path.insert(1,'/usr/local/lib/python3.6/site-packages/')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.resize(450, 150)
    w.move(300, 300)
    w.setWindowTitle('自动调试')
    w.show()
    sys.exit(app.exec_())
