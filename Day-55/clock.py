# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Clock(QMainWindow):

	def __init__(self):
		super().__init__()
		timer = QTimer(self)
		timer.timeout.connect(self.update)
		timer.start(1000)
		self.setWindowTitle('Clock')
		self.setGeometry(200, 200, 300, 300)
		self.setStyleSheet("background : black;")

		self.hPointer = QtGui.QPolygon([QPoint(6, 7),
										QPoint(-6, 7),
										QPoint(0, -50)])

		self.mPointer = QPolygon([QPoint(6, 7),
								QPoint(-6, 7),
								QPoint(0, -70)])

		self.sPointer = QPolygon([QPoint(1, 1),
								QPoint(-1, 1),
								QPoint(0, -90)])
	
		self.bColor = Qt.green

		self.sColor = Qt.red
	def paintEvent(self, event):
		rec = min(self.width(), self.height())

		tik = QTime.currentTime()
		painter = QPainter(self)
		def drawPointer(color, rotation, pointer):

			painter.setBrush(QBrush(color))

			painter.save()

			painter.rotate(rotation)

			painter.drawConvexPolygon(pointer)

			painter.restore()


		painter.setRenderHint(QPainter.Antialiasing)

		painter.translate(self.width() / 2, self.height() / 2)

		painter.scale(rec / 200, rec / 200)

		painter.setPen(QtCore.Qt.NoPen)

		drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
		drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
		drawPointer(self.sColor, (6 * tik.second()), self.sPointer)


		painter.setPen(QPen(self.bColor))
		for i in range(0, 60):

			if (i % 5) == 0:
				painter.drawLine(87, 0, 97, 0)
			painter.rotate(6)

		painter.end()
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Clock()
	win.show()
	exit(app.exec_())
