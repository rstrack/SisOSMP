from PyQt6 import QtWidgets, QtGui, QtCore

class HoverButton(QtWidgets.QPushButton):
    def __init__(self, title, icon_path, icon_path_hover, parent=None):
        super(QtWidgets.QPushButton, self).__init__()
        self.setText(title)
        self.setObjectName(title)
        self.defaultIcon = QtGui.QIcon(icon_path)
        self.hoverIcon = QtGui.QIcon(icon_path_hover)
        self.setIcon(self.defaultIcon)
        self.setIconSize(QtCore.QSize(15, 15))
        self.installEventFilter(self)
      
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Type.HoverEnter:
            self.setIcon(self.hoverIcon)
            self.setIconSize(QtCore.QSize(15, 15))
        elif event.type() == QtCore.QEvent.Type.HoverLeave:
            self.setIcon(self.defaultIcon)
        
        return super().eventFilter(source, event)