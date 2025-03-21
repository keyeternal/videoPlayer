import sys
from video_processor import VideoPlayer
from PyQt5.QtWidgets import QApplication

# Дизайн окна

StyleSheet = ("""
   QWidget {
      background-color: #e6f2ff;
      font-size: 12px;
   }

   QPushButton {
      background-color: #009adb;
      color: white;
      border-radius: 5px;
      padding: 5px;
      font-size: 12px;
   }
   
   QSlider::handle:horizontal {
    background-color: #009adb
    width: 18px;
    border-radius: 10px;
}
""")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = VideoPlayer()
    win.setWindowTitle("Видео-проигрыватель")
    win.setFixedSize(700, 500)
    win.show()
    sys.exit(app.exec_())
