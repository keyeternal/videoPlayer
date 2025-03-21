import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *


# Set up the MenuBar
class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()


        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(self.script_dir)

        self.mediaPlayer = QMediaPlayer()
        self.videoWidget = QVideoWidget()
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        # Создание элементов

        self.p = QIcon("assets/pauseIcon.png")

        self.playPauseButton = QPushButton()
        self.playPauseButton.setObjectName("OnlyIconButton")
        self.playPauseButton.setFlat(True)
        self.ppb = QIcon("assets/playIcon.png")
        self.playPauseButton.setIcon(self.ppb)
        self.playPauseButton.setIconSize(QSize(40, 40))
        self.playPauseButton.setFixedSize(45, 45)

        self.openFileButton = QPushButton()
        self.openFileButton.setObjectName("OnlyIconButton")
        self.openFileButton.setFlat(True)
        self.ofb = QIcon("assets/openVideoIcon.png")
        self.openFileButton.setIcon(self.ofb)
        self.openFileButton.setIconSize(QSize(40, 40))
        self.openFileButton.setFixedSize(45, 45)

        self.skipBackwardButton30 = QPushButton()
        self.skipBackwardButton30.setObjectName("OnlyIconButton")
        self.skipBackwardButton30.setFlat(True)
        self.sbb30 = QIcon("assets/replay30Icon.png")
        self.skipBackwardButton30.setIcon(self.sbb30)
        self.skipBackwardButton30.setIconSize(QSize(40, 40))
        self.skipBackwardButton30.setFixedSize(45, 45)

        self.skipForwardButton30 = QPushButton()
        self.skipForwardButton30.setObjectName("OnlyIconButton")
        self.skipForwardButton30.setFlat(True)
        self.sfb30 = QIcon("assets/forward30Icon.png")
        self.skipForwardButton30.setIcon(self.sfb30)
        self.skipForwardButton30.setIconSize(QSize(40, 40))
        self.skipForwardButton30.setFixedSize(45, 45)

        self.skipForwardButton5 = QPushButton()
        self.skipForwardButton5.setObjectName("OnlyIconButton")
        self.skipForwardButton5.setFlat(True)
        self.sfb5 = QIcon("assets/forward5Icon.png")
        self.skipForwardButton5.setIcon(self.sfb5)
        self.skipForwardButton5.setIconSize(QSize(40, 40))
        self.skipForwardButton5.setFixedSize(45, 45)

        self.skipBackwardButton5 = QPushButton()
        self.skipBackwardButton5.setObjectName("OnlyIconButton")
        self.skipBackwardButton5.setFlat(True)
        self.sbb5 = QIcon("assets/replay5Icon.png")
        self.skipBackwardButton5.setIcon(self.sbb5)
        self.skipBackwardButton5.setIconSize(QSize(40, 40))
        self.skipBackwardButton5.setFixedSize(45, 45)

        self.videoTimeLabel = QLabel("00:00")
        self.videoTimeLabel.setFixedHeight(10)

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(50)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.setValue(0)

        # Подключение элементов

        self.playPauseButton.clicked.connect(self.play_pause)
        self.openFileButton.clicked.connect(self.openVideo)
        self.skipBackwardButton30.clicked.connect(self.skipBackward30)
        self.skipBackwardButton5.clicked.connect(self.skipBackward5)
        self.skipForwardButton30.clicked.connect(self.skipForward30)
        self.skipForwardButton5.clicked.connect(self.skipForward5)
        self.volumeSlider.valueChanged.connect(self.volumeSliderChange)
        self.mediaPlayer.positionChanged.connect(self.updateSliderPosition)
        self.mediaPlayer.durationChanged.connect(self.updateDuration)
        self.positionSlider.sliderMoved.connect(self.updateMediaPosition)

        # Основной дизайн окна

        self.layout = QVBoxLayout()
        self.controls = QHBoxLayout()
        self.miniControls = QHBoxLayout()

        self.layout.addWidget(self.videoWidget)
        self.layout.addWidget(self.videoTimeLabel, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.positionSlider)

        self.rightSpacer = QSpacerItem(10, 10, QSizePolicy.Minimum)

        self.miniControls.addWidget(self.skipBackwardButton30)
        self.miniControls.addWidget(self.skipBackwardButton5)
        self.miniControls.addWidget(self.playPauseButton)
        self.miniControls.addWidget(self.skipForwardButton5)
        self.miniControls.addWidget(self.skipForwardButton30)

        self.controls.addItem(self.rightSpacer)
        self.controls.addLayout(self.miniControls)
        self.controls.addItem(self.rightSpacer)
        self.controls.addWidget(self.volumeSlider)
        self.controls.addItem(self.rightSpacer)
        self.controls.addWidget(self.openFileButton, alignment=Qt.AlignRight)

        self.layout.addLayout(self.controls)

        self.setLayout(self.layout)


    def openVideo(self): # Открытие файла и авто воспроизведение видео
        try:
            self.fileName, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Форматы: *.mp4 *.avi *.mov *.mkv")
            if self.fileName:
                print(f"Выбран файл: {self.fileName}")
                media_content = QMediaContent(QUrl.fromLocalFile(self.fileName))
                self.mediaPlayer.setMedia(media_content)
                self.mediaPlayer.play()
                self.playPauseButton.setIcon(self.p)
        except Exception as e:
            print(f"Ошибка при открытии файла: {e}")

    def play_pause(self): # Запустить / остановить воспроизведение
            if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
                self.mediaPlayer.pause()
                self.playPauseButton.setIcon(self.ppb)
            else:
                self.mediaPlayer.play()
                self.playPauseButton.setIcon(self.p)

    def skipForward30(self, videoDuration):  # Перемотка вперед (15С)
        currentPosition = self.mediaPlayer.position()
        self.mediaPlayer.setPosition(currentPosition + 30000)

    def skipForward5(self, videoDuration): # Перемотка вперед (5С)
        currentPosition = self.mediaPlayer.position()
        self.mediaPlayer.setPosition(currentPosition + 5000)

    def skipBackward30(self):  # Перемотка назад (15С)
        currentPosition = self.mediaPlayer.position()
        self.mediaPlayer.setPosition(max(0, currentPosition - 30000))

    def skipBackward5(self): # Перемотка назад (5С)
        currentPosition = self.mediaPlayer.position()
        self.mediaPlayer.setPosition(max(0, currentPosition - 5000))

    def volumeSliderChange(self, volume): # Изменение громкости в зависимости от позиции слайдера
        self.mediaPlayer.setVolume(volume)

    def updateSliderPosition(self, position): # Обновление позиции слайдера в реальном времени
        seconds = (position // 1000) % 60
        minutes = (position // (1000 * 60)) % 60
        self.videoTimeLabel.setText(f"{minutes:02}:{seconds:02}")
        self.positionSlider.setValue(position)

    def updateDuration(self, duration): # Обновление максимальной ширины слайдера после загрузки видео
        self.positionSlider.setRange(0, duration)
        self.videoDuration = int(duration)

    def updateMediaPosition(self, position): # Обновление позиции видео, в зависимости от позиции слайдера
        self.mediaPlayer.setPosition(position)
