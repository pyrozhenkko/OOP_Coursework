import os
import sys
from PyQt5.QtWidgets import QApplication
from main.program.MainWindow import MainWindow
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
