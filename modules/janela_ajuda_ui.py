# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela_ajuda.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JanelaAjuda(object):
    def setupUi(self, JanelaAjuda):
        JanelaAjuda.setObjectName("JanelaAjuda")
        JanelaAjuda.resize(330, 320)
        self.labelCriado = QtWidgets.QLabel(JanelaAjuda)
        self.labelCriado.setGeometry(QtCore.QRect(140, 290, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelCriado.setFont(font)
        self.labelCriado.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelCriado.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.labelCriado.setWordWrap(True)
        self.labelCriado.setObjectName("labelCriado")
        self.layoutWidget = QtWidgets.QWidget(JanelaAjuda)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 311, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitulo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitulo.setObjectName("labelTitulo")
        self.verticalLayout.addWidget(self.labelTitulo)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.layoutWidget1 = QtWidgets.QWidget(JanelaAjuda)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 170, 311, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)

        self.retranslateUi(JanelaAjuda)
        QtCore.QMetaObject.connectSlotsByName(JanelaAjuda)

    def retranslateUi(self, JanelaAjuda):
        _translate = QtCore.QCoreApplication.translate
        JanelaAjuda.setWindowTitle(_translate("JanelaAjuda", "Dialog"))
        self.labelCriado.setText(_translate("JanelaAjuda", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Created by HA4LAKA</span></p></body></html>"))
        self.labelTitulo.setText(_translate("JanelaAjuda", "Baguncinha de Arquivos"))
        self.label.setText(_translate("JanelaAjuda", "Programa feito para \'bagunçar\' os arquivos de uma pasta. Ele copia os arquivos da pasta em outra com \"... (baguncinha)\" e nomea os arquivos com números para sortear. CERTIFIQUE-SE QUE NA PASTA PODE CRIAR OUTRAS PASTAS OU COPIAR ARQUIVOS. Dica: copie a pasta com os arquivos na área de trabalho e selecione ela."))
        self.label_2.setText(_translate("JanelaAjuda", "<html><head/><body><p><span style=\" font-weight:600;\">Abrir</span> - abre uma janela de browser para selecionar a pasta com os arquivos</p><p><br/></p></body></html>"))
        self.label_3.setText(_translate("JanelaAjuda", "<html><head/><body><p><span style=\" font-weight:600;\">Bagunçar</span> - verifica se o diretório é válido da pasta e faz o sorteio renomeando os arquivos em seguida</p><p><br/></p></body></html>"))

