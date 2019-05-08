from modules.JanelaSorteador_ui import Ui_MainWindowJanelaBaguncinha
from modules.janela_ajuda_ui import Ui_JanelaAjuda
import os
import shutil
import random
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog


class Baguncinha(QMainWindow):
    """Classe para bagunçar os arquivos"""
    def __init__(self):
        super().__init__()
        self.title = "Baguncinha de Arquivos"
        self.top = 300
        self.left = 200
        self.width = 480
        self.height = 190
        self.ui = Ui_MainWindowJanelaBaguncinha()
        self.ui.setupUi(self)
        self.allfiles = []
        self.folderBaguncinha = ""
        self.dir = ""
        self.initUI()
        random.seed(datetime.now())
        #Conectores de sinais e slots

        self.ui.pushButtonAbrir.clicked.connect(self.abrirDiretorio)
        self.ui.pushButtonBaguncar.clicked.connect(self.baguncarArquivos)
        self.ui.actionSair.triggered.connect(self.close)
        self.ui.actionAjuda.triggered.connect(self.janelaAjuda)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.show()

    # Slots

    def baguncarArquivos(self):
        if os.path.isdir(self.ui.lineEditDiretorio.text()):
            self.dir = self.ui.lineEditDiretorio.text()
            for file in os.listdir(self.dir): # vasculha todos dados do dir
                if os.path.isfile(os.path.join(self.dir, file)): # verifica se são arquivos
                    self.allfiles.append(file) # adiciona na lista o nome do arquivo
            self.folderBaguncinha = self.dir + " (baguncinha)"
        try:
            os.mkdir(self.folderBaguncinha)
            for f in self.allfiles:
                shutil.copyfile(os.path.join(self.dir, f),
                                os.path.join(self.folderBaguncinha, f))
            self.renomearArquivos()
        except:
            QMessageBox.critical(self, "Error", "Não foi possivel bagunçar os arquivos")
            self.resetarVariaveis()

    def abrirDiretorio(self):
        try:
            temp = str(QFileDialog.getExistingDirectory(self, "Selecione o diretório"))
            self.ui.lineEditDiretorio.setText(temp)
        except:
            QMessageBox.critical(self, "Error", "Não foi possivel abrir a pasta")
            self.resetarVariaveis()

    def renomearArquivos(self):
        try:
            random.shuffle(self.allfiles)
            i = 0
            for file in self.allfiles:
                filename, file_ext = os.path.splitext(file)
                os.rename(os.path.join(self.folderBaguncinha, file),
                          os.path.join(self.folderBaguncinha, str(i) + file_ext))
                i = i + 1
            self.resetarVariaveis()
        except:
            QMessageBox.critical(self, "Error", "Não foi possivel renomear os arquivos")
            self.resetarVariaveis()

    def resetarVariaveis(self):
        self.allfiles = []
        self.folderBaguncinha = ""
        self.dir = ""
        self.ui.lineEditDiretorio.clear()

    def janelaAjuda(self):
        """"Abri uma janela de ajuda"""
        janela = QDialog(self)
        ui = Ui_JanelaAjuda()
        ui.setupUi(janela)
        janela.setWindowTitle("Ajuda")
        janela.setFixedSize(330, 320)
        janela.show()
