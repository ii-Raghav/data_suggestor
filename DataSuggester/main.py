import sys
from src.ui_components import DataStructureApp
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataStructureApp()
    window.show()
    sys.exit(app.exec_())
