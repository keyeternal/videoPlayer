import sys

import video_processor
from video_processor import VideoPlayer
from PyQt5.QtWidgets import QApplication

# Дизайн окна

StyleSheet = ("""
   QWidget {
      background-color: #e6f2ff;
      font-size: 12px;
   }   
    QSlider::handle:horizontal {
        background-color: #009adb
        width: 18px;
        border-radius: 10px;
    }
    
    QPushButton {
        border: none;
        background: transparent;
    }
    
    QPushButton:pressed {
        background: transparent;
    }
""")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = VideoPlayer()
    win.setStyleSheet(StyleSheet)
    win.setWindowTitle("Видео-проигрыватель")
    win.setFixedSize(700, 500)
    win.show()
    sys.exit(app.exec_())
