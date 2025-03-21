import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# Set up the MenuBar
class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()


        # Назначение рабочей директории

        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(self.script_dir)

        # Создание виджета видео и привязка мультимедиа

        self.mediaPlayer = QMediaPlayer()
        self.videoWidget = QVideoWidget()
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        # Создание элементов

        self.playPauseButton = QPushButton()
        self.playPauseButton.setObjectName("OnlyIconButton")
        self.playPauseButton.setFlat(True)
        self.p = QIcon("assets/pauseIcon.png")
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

        # Настройка сочетаний клавиш

        self.pps = QShortcut("space", self)
        self.pps.activated.connect(self.play_pause)
        self.sbs = QShortcut("left", self)
        self.sbs.activated.connect(self.skipBackward5)
        self.skipForwardShortcut = QShortcut("right", self)
        self.skipForwardShortcut.activated.connect(self.skipForward5)

        # Назначение элементов

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

        self.menuBar = QMenuBar(self) # Создание меню-бара

        # Создание меню в меню-баре

        self.fileMenu = self.menuBar.addMenu("Файл")
        self.videoMenu = self.menuBar.addMenu("Видео")

        # Добавление пунктов в меню "Файл"

        self.openAction = QAction("Открыть ( Ctrl + O )", self)
        self.openAction.setShortcut("Ctrl + O")
        self.openAction.triggered.connect(self.openVideo)

        self.exitAction = QAction("Выход ( Ctrl + Q )", self)
        self.exitAction.setShortcut("Ctrl + Q")
        self.exitAction.triggered.connect(self.close)

        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.exitAction)

        # Добавление пунктов в меню "Видео"

        self.playPauseAction = QAction("Запуск/Пауза", self)
        self.playPauseAction.triggered.connect(self.play_pause)
        self.videoMenu.addAction(self.playPauseAction)
        self.videoMenu.addSeparator()

        # Суб-меню перемотки в меню "Видео"

        self.skipMenu = self.videoMenu.addMenu("Перемотка")
        self.skipForward30Action = QAction("+ 30с", self)
        self.skipForward30Action.triggered.connect(self.skipForward30)
        self.skipForward5Action = QAction("+ 5с", self)
        self.skipForward5Action.triggered.connect(self.skipForward5)
        self.skipBack30Action = QAction("- 30с", self)
        self.skipBack30Action.triggered.connect(self.skipBackward30)
        self.skipBack5Action = QAction("- 5с", self)
        self.skipBack5Action.triggered.connect(self.skipBackward5)

        self.skipMenu.addAction(self.skipForward30Action)
        self.skipMenu.addAction(self.skipForward5Action)
        self.skipMenu.addAction(self.skipBack30Action)
        self.skipMenu.addAction(self.skipBack5Action)

        # Суб-меню скорости воспроизведения в меню "Видео"

        self.playbackSpeedMenu = self.videoMenu.addMenu("Скорость видео")
        self.speed05x = QAction("0.5x", self)
        self.speed1x = QAction("1x ( Нормальная )", self)
        self.speed2x = QAction("2x", self)
        self.speed05x.triggered.connect(lambda: self.setPlaybackSpeed(0.5))
        self.speed1x.triggered.connect(lambda: self.setPlaybackSpeed(1))
        self.speed2x.triggered.connect(lambda: self.setPlaybackSpeed(2))

        self.playbackSpeedMenu.addAction(self.speed05x)
        self.playbackSpeedMenu.addAction(self.speed1x)
        self.playbackSpeedMenu.addAction(self.speed2x)

        self.layout.setMenuBar(self.menuBar) # Добавление менюбара к окну

    def setPlaybackSpeed(self, speed): # Изменение скорости видео
        print(f"Изминение скорости на {speed}")
        self.mediaPlayer.setPlaybackRate(speed)

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

    def skipForward30(self):  # Перемотка вперед (30C)
        currentPosition = self.mediaPlayer.position()
        self.mediaPlayer.setPosition(currentPosition + 30000)

    def skipForward5(self): # Перемотка вперед (5С)
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