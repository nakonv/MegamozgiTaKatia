import sys
import math
import random

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import QTimer, QPoint
from PyQt5.QtGui import QPainter, QPen, QColor, QFont, QPixmap
from PyQt5.QtWidgets import QComboBox, QSpinBox, QDoubleSpinBox, QHBoxLayout


from track import Track
from track_types import TrackFactory, CityTrack, RaceTrack, WetTrack
from Race import Race
from RaceManager import RaceManage
from driver import Driver
from Car import Car


class RaceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Racing Simulator")
        self.resize(800, 600)

        self.layout = QVBoxLayout()
        self.title = QLabel("🏎 Racing Championship")
        self.title.setAlignment(Qt.AlignCenter)  # Центруємо текст
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; margin-top: 10px;")
        self.layout.addWidget(self.title)

        self.layout.addStretch(1)  # ЦЕ ВАЖЛИВО: створює пустий простір для траси посередині

        #КНОПКИ ТРАС
        self.button_layout = QHBoxLayout()
        # Кнопка випадкової гонки
        self.randomButton = QPushButton("🎲 Випадкова гонка")
        self.randomButton.clicked.connect(lambda: self.startRace(mode="random"))
        self.button_layout.addWidget(self.randomButton)
        # Кнопка ручного налаштування
        self.customButton = QPushButton("🛠 Створити свій трек")
        self.customButton.clicked.connect(lambda: self.startRace(mode="custom"))
        self.button_layout.addWidget(self.customButton)
        self.layout.addLayout(self.button_layout)

        self.output = QTextEdit()
        self.output.setFixedHeight(100)  # Фіксуємо висоту, щоб воно не стрибало
        self.layout.addWidget(self.output)

        self.setLayout(self.layout)
        self.randomButton.clicked.connect(lambda: self.startRace(mode="random"))
        self.customButton.clicked.connect(lambda: self.startRace(mode="custom"))

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateRace)
        self.phase_shifts = [0, 0, 0]
        self.running = False
        self.angle = [0, 0]


        #ФЛАЖОК
        self.finish_img = QPixmap("flag.svg")  # Вкажи шлях до свого файлу
        self.finish_img = self.finish_img.scaled(40, 40, Qt.KeepAspectRatio)  # Змінюємо розмір

        #ВИБІР ТРАСИ
        self.settings_layout = QHBoxLayout()

        # Вибір типу
        self.type_combo = QComboBox()
        self.type_combo.addItems(["city", "race", "wet"])
        self.settings_layout.addWidget(QLabel("Тип:"))
        self.settings_layout.addWidget(self.type_combo)

        # Кількість поворотів (Turns)
        self.turns_spin = QSpinBox()
        self.turns_spin.setRange(3, 30)
        self.turns_spin.setValue(10)
        self.settings_layout.addWidget(QLabel("Повороти:"))
        self.settings_layout.addWidget(self.turns_spin)

        # Зчеплення (Grip)
        self.grip_spin = QDoubleSpinBox()
        self.grip_spin.setRange(0.1, 1.2)
        self.grip_spin.setSingleStep(0.1)
        self.grip_spin.setValue(0.8)
        self.settings_layout.addWidget(QLabel("Зчеплення:"))
        self.settings_layout.addWidget(self.grip_spin)

        # Додаємо панель в основний лейаут
        self.layout.insertLayout(1, self.settings_layout)

    def startRace(self, mode="random"):
        # Зупиняємо старий таймер
        self.timer.stop()
        self.angle = [0, 0]
        self.phase_shifts = [random.uniform(0, 6.28) for _ in range(3)]

        if mode == "random":
            # Використовуємо твою стару логіку рандому
            self.current_track = TrackFactory.create_random()
            # Оновлюємо значення в меню, щоб користувач бачив, що випало
            self.update_ui_from_track(self.current_track)
        else:
            # Беремо дані з полів вводу (QComboBox, QSpinBox і т.д.)
            track_type = self.type_combo.currentText()
            turns = self.turns_spin.value()
            grip = self.grip_spin.value()
            self.current_track = TrackFactory.create(track_type, "Мій Трек", 5000, turns, grip)

        # Спільна логіка запуску
        factor = self.current_track.getSectionSpeedFactor(0)
        base_power = 3.0
        self.speeds = [
            base_power * factor * random.uniform(0.9, 1.1),
            base_power * factor * random.uniform(0.8, 1.2)  # трохи більше розкиду
        ]

        self.output.clear()
        self.output.append(f"🏁 <b>Старт: {self.current_track.name}</b>")
        self.output.append(f"Тип: {type(self.current_track).__name__} | Поворотів: {self.current_track.turns}")

        self.running = True
        self.timer.start(50)
        self.update()

    # Допоміжний метод, щоб синхронізувати меню з рандомом
    def update_ui_from_track(self, track):
        # Це щоб після "Рандому" в спінбоксах з'явилися реальні числа треку
        if isinstance(track, CityTrack):
            self.type_combo.setCurrentText("city")
        elif isinstance(track, WetTrack):
            self.type_combo.setCurrentText("wet")
        else:
            self.type_combo.setCurrentText("race")

        self.turns_spin.setValue(track.turns)
        self.grip_spin.setValue(track.grip)

    def updateRace(self):
        if not self.running:
            return

        for i in range(len(self.angle)):
            self.angle[i] += self.speeds[i]

            # Перевірка на завершення кола (360 градусів)
            if self.angle[i] >= 360:
                self.running = False
                self.timer.stop()
                winner = "Червона" if i == 0 else "Синя"
                self.output.append(f"🏁 Фініш! Перемогла {winner} машина!")

        self.repaint()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 1. Початкові координати центру
        cx, cy = 400, 300
        num_turns = 10
        complexity = 0.2
        rx, ry = 220, 140

        # 2. Визначаємо параметри траси залежно від об'єкта треку
        if hasattr(self, 'current_track'):
            num_turns = self.current_track.turns
            complexity = self.current_track.complexity
            # Чим більше поворотів, тим сильніше "тремтить" лінія

            # --- МАЛЮЄМО ТРАСУ (Path) ---
        from PyQt5.QtGui import QPainterPath
        path = QPainterPath()

        def get_track_radius(angle_rad, lane_offset=0):
            # Базова амплітуда вигинів залежить від складності (наприклад, 0.3 * 100 = 30 пікселів)
            amplitude = complexity * 60

            # Змішуємо 3 різні хвилі для ефекту "неідеальності"
            # 1. Основні повороти (num_turns)
            wave1 = math.sin(angle_rad * num_turns + self.phase_shifts[0]) * amplitude

            # 2. Дрібні нерівності (більше частота, менша амплітуда)
            wave2 = math.sin(angle_rad * (num_turns * 1.5) + self.phase_shifts[1]) * (amplitude * 0.4)

            # 3. Великі плавні вигини всього кільця
            wave3 = math.cos(angle_rad * 2 + self.phase_shifts[2]) * (amplitude * 0.6)

            total_distortion = wave1 + wave2 + wave3

            # Застосовуємо викривлення до радіусів
            current_rx = rx + lane_offset + total_distortion
            current_ry = ry + lane_offset + total_distortion

            x = cx + current_rx * math.cos(angle_rad)
            y = cy + current_ry * math.sin(angle_rad)
            return x, y

        # Малюємо основну лінію траси
        first_x, first_y = get_track_radius(0)
        path.moveTo(first_x, first_y)

        for deg in range(1, 361):
            nx, ny = get_track_radius(math.radians(deg))
            path.lineTo(nx, ny)

        painter.setPen(QPen(QColor("gray"), 15, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawPath(path)

        #ФЛАЖОК
        # 1. Визначаємо точку початку (кут 0)
        # lane_offset=0 — це центр дороги. Якщо хочеш поставити збоку, постав 30 або -30
        start_x, start_y = get_track_radius(0, 0)

        # 2. Малюємо картинку
        # Віднімаємо половину розміру картинки (наприклад, 20), щоб центр картинки був точно на лінії
        img_w = self.finish_img.width()
        img_h = self.finish_img.height()
        painter.drawPixmap(int(start_x - 4), int(start_y - img_h), self.finish_img)

        # Додамо розмітку посередині (біла пунктирна лінія)
        painter.setPen(QPen(QColor("white"), 1, Qt.DashLine))
        painter.drawPath(path)

        # --- МАЛЮЄМО МАШИНИ ---
        if self.running:
            colors = ["red", "cyan"]
            for i, angle in enumerate(self.angle):
                rad = math.radians(angle)
                # Машини їдуть точно по тій же кривій, що і траса
                lane = i * 12 - 6  # розводимо їх на різні боки від центру дороги
                mx, my = get_track_radius(rad, lane)

                painter.setBrush(QColor(colors[i]))
                painter.setPen(QPen(Qt.black, 1))
                painter.drawEllipse(int(mx) - 6, int(my) - 6, 12, 12)


app = QApplication(sys.argv)

window = RaceWindow()
window.show()

sys.exit(app.exec_())