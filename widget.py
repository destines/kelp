"""
Date         : 2024-02-19 15:35:44
LastEditors  : xis 2684219495@qq.com
LastEditTime : 2024-02-19 19:07:41
FilePath     : /untitled6/widget.py
Description  : 
"""

# This Python file uses the following encoding: utf-8
import mss
import time
import psutil
import pynvml
import subprocess

from PySide6.QtCore import Qt, QPoint, QTimer
from PySide6.QtWidgets import QWidget

# from PySide6.

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_widget import Ui_Widget


class Widget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setMouseTracking(True)

        self.offset = QPoint()
        self.mousePressed = False

        self.opacity = 1

        # 初始化 NVIDIA Management Library (NVML)
        pynvml.nvmlInit()

        self.timerManager(True)

    def timerManager(self, cmd: bool):

        if cmd == True:
            self.cpu_pwr_t = QTimer(self)
            self.cpu_pwr_t.timeout.connect(self.update_cpu_pwr)

            self.vram_t = QTimer(self)
            self.vram_t.timeout.connect(self.update_vram)

            self.ram_t = QTimer(self)
            self.ram_t.timeout.connect(self.update_ram)

            self.heat_t = QTimer(self)
            self.heat_t.timeout.connect(self.update_heat)

            self.gpu_t = QTimer(self)
            self.gpu_t.timeout.connect(self.update_gpu)

            self.fps_t = QTimer(self)
            self.fps_t.timeout.connect(self.update_fps)

            self.cpu_pwr_t.start(1500)
            self.vram_t.start(1500)
            self.ram_t.start(1500)
            self.heat_t.start(1500)
            self.gpu_t.start(1500)
            self.fps_t.start(1500)
        elif cmd == False:
            self.cpu_pwr_t.stop()
            self.vram_t.stop()
            self.ram_t.stop()
            self.heat_t.stop()
            self.gpu_t.stop()
            self.fps_t.stop()

    def get_fps(self):
        # hardClassInit
        fpss = []
        with mss.mss() as sct:
            frame_count = 0
            start_time = time.time()
            for monitor in sct.monitors:
                while True:
                    # captrue green
                    sct.grab(monitor)

                    # calculate FPS
                    frame_count += 1

                    elapsed_time = time.time() - start_time
                    if elapsed_time >= 1:  # 每隔一秒计算一次FPS
                        fpss.append(frame_count / elapsed_time)
                        break
        return fpss

    def get_vram(self) -> float:
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)  # 默认使用第一个 GPU
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        vram_total = mem_info.total / 1024**2  # 将字节转换为兆字节
        vram_used = mem_info.used / 1024**2
        vram_usage = (vram_used / vram_total) * 100
        return vram_usage

    def get_ram(self):
        ram = psutil.virtual_memory()
        ram_total = ram.total / (1024**2)  # 将字节转换为兆字节
        ram_used = ram.used / (1024**2)
        ram_usage = (ram_used / ram_total) * 100
        return ram_usage

    def get_heat(self):
        output = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=temperature.gpu",
                "--format=csv,noheader,nounits",
            ]
        )
        gpu_temperatures = output.decode("utf-8").strip().split("\n")
        return [int(temperature) for temperature in gpu_temperatures]

    def get_gpu(self):
        output = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=utilization.gpu",
                "--format=csv,noheader,nounits",
            ]
        )
        gpu_utilization = output.decode("utf-8").strip().split("\n")
        return [int(utilization) for utilization in gpu_utilization]

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.mousePressed = True
            self.offset = event.position().toPoint()
            self.timerManager(False)

    def mouseMoveEvent(self, event):
        if self.mousePressed:
            self.move(event.globalPosition().toPoint() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.RightButton:
            self.mousePressed = False
            self.timerManager(True)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.RightButton:
            self.close()
            self.__del__()
        if event.button() == Qt.LeftButton:
            # 设置窗口初始透明度
            self.opacity -= 0.25
            self.setWindowOpacity(self.opacity)
            if (self.opacity - 0) <= 0:
                self.close()
                self.__del__()

    def update_cpu_pwr(self):
        # 更新对应线程的标签文本
        self.ui.c_label.setText(f"CPU     {psutil.cpu_percent(interval=1):.2f}%")
        self.ui.p_label.setText(f"PWR    {psutil.sensors_battery()[0]}%")

    def update_vram(self):
        self.ui.v_label.setText(f"RAM    {self.get_vram():.2f}%")

    def update_ram(self):
        self.ui.r_label.setText(f"VRAM  {self.get_ram():.2f}%")

    def update_heat(self):
        self.ui.h_label.setText(f"HEAT   {self.get_heat()[0]}°C")

    def update_fps(self):
        self.ui.f_label.setText(f"FPS      {self.get_fps()[0]:.0f}")

    def update_gpu(self):
        data = self.get_gpu()
        self.ui.g_label.setText(f"GPU     {sum(data)/len(data):.2f}%")

    def __del__(self):

        # 结束 NVML
        pynvml.nvmlShutdown()
        quit()
