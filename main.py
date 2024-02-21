import sys
# import multiprocessing

from widget import Widget

from PySide6.QtWidgets import QApplication

if __name__ == "__main__":

    # multiprocessing.freeze_support()  # 并发声明
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
