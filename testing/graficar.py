import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QTimer, QPointF
import math

class TriangleWindow(QMainWindow):
    def __init__(self, points):
        super().__init__()
        self.points = points
        self.angle = 0
        self.initUI()
        self.startTimer()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Triangle')
        self.show()

    def startTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateRotation)
        self.timer.start(50)  # Update every 50 milliseconds

    def updateRotation(self):
        self.angle += 5
        if self.angle >= 360:
            self.angle = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        
        if len(self.points) == 3:
            center = QPointF(sum(point.x() for point in self.points) / 3,
                             sum(point.y() for point in self.points) / 3)
            rotated_points = [self.rotate_point(point, center, self.angle) for point in self.points]
            painter.drawPolygon(*rotated_points)

    def rotate_point(self, point, center, angle):
        rad = math.radians(angle)
        x = math.cos(rad) * (point.x() - center.x()) - math.sin(rad) * (point.y() - center.y()) + center.x()
        y = math.sin(rad) * (point.x() - center.x()) + math.cos(rad) * (point.y() - center.y()) + center.y()
        return QPointF(x, y)

def main(points):
    app = QApplication(sys.argv)
    ex = TriangleWindow(points)
    sys.exit(app.exec_())

if __name__ == '__main__':
    # Define the points of the triangle (x, y)
    points = [QPointF(100, 100), QPointF(200, 300), QPointF(300, 100)]
    main(points)