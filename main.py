from PyQt5.QtWidgets import QApplication
import sys
from modules.BaguncinhaArquivos import Baguncinha

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Janela = Baguncinha()
    sys.exit(App.exec())
