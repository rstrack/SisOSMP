import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen, QPainterPath, QTextOption, QIcon, QColorConstants
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QGridLayout, QPushButton

class ExplanationBalloon(QWidget):
    def __init__(self, widget: QWidget, width: float, height: float, text: str):
        super().__init__()
        self.installEventFilter(self)
        self._widget = widget
        self._widget.installEventFilter(self)
        self._window = self._widget.window()
        self._window.installEventFilter(self)

        self.__initUi(width, height, text)

    def __initUi(self, width, height, text):
        self.setFixedSize(width + 2, height + 10)
        self.__initBalloon(width, height, text)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self._btn = QPushButton()
        ico_filename = './resources/close-icon.png'
        self._btn.setIcon(QIcon(ico_filename))
        self._btn.clicked.connect(self.close)
        self._btn.setStyleSheet('QPushButton{background-color: transparent;}')

        lay = QGridLayout()
        lay.addWidget(self._btn, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        lay.setContentsMargins(5, 5, 5, 5)
        self.setLayout(lay)

    def __initBalloon(self, width, height, text):
        self._border_width = 1
        self._width = width
        self._height = height
        self._text = text
        self._background_color = QColor(255,255,255,255)
        self._balloon = self.__getBalloonShape(self._width, self._height)

    def __setIsosceles(self, x, y, width: float, height: float, orientation=Qt.Orientation.Horizontal) -> QPainterPath:
        isosceles = QPainterPath()
        # horizontal
        x1 = x
        y1 = y

        x2 = x1+width
        y2 = y1

        x3 = (x1+x2) / 2
        y3 = y1+height

        isosceles.moveTo(x1, y1)
        isosceles.lineTo(x2, y2)
        isosceles.lineTo(x3, y3)
        isosceles.lineTo(x1, y1)

        return isosceles

    def paintEvent(self, e):
        painter = QPainter(self)
        brush = QBrush(self._background_color)
        pen = QPen(QColor(QColorConstants.DarkGray), self._border_width)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.drawPath(self._balloon)
        textOption = QTextOption()
        textOption.setAlignment(Qt.AlignmentFlag.AlignCenter)
        textOption.setWrapMode(QTextOption.WrapMode.WordWrap)
        painter.drawText(self._balloon.boundingRect(), self._text, textOption)

        return super().paintEvent(e)

    def __getBalloonShape(self, width: float, height: float):
        path1 = QPainterPath()
        path1.addRoundedRect(0, 0, width, height, 10.0, 10.0)

        path2 = self.__setIsosceles(20.0, height - 3, 30.0, 10.0)

        path3 = path2.united(path1)

        return path3

    def setPosition(self):
        x, y = self._widget.geometry().x(), self._widget.geometry().y()
        x, y = x + self._window.geometry().x(), y + self._window.geometry().y()
        print([x, y])
        # self.move(x, y-self.height())
        self.move(x+self.width(), y+self.height())

    def setBackgroundColor(self, color: QColor):
        self._background_color = color

    def eventFilter(self, obj, e):
        if isinstance(obj, type(self._widget)):
            self.setPosition()
        elif isinstance(obj, type(self._window)):
            self.raise_()
            # if window has moved or resized
            if e.type() == 13 or e.type() == 14:
                self.setPosition()
        elif isinstance(obj, type(self)):
            # if font has changed
            # should resize the balloon or let user set on his own?
            if e.type() == 97:
                print(self.fontMetrics().boundingRect(self._text))
        return super().eventFilter(obj, e)