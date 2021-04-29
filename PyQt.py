import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "primeira janela"

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(25 ,8)
        self.caixa_texto.resize(250, 30)

        self.label_caixa = QLabel(self)
        self.label_caixa.move(400, 200)
        self.label_caixa.resize(250 ,40)
        self.label_caixa.setStyleSheet('QLabel {font-size: 30px}')
        self.label_caixa.setText('Digitou: ')


        botao1 = QPushButton('Botao1', self)
        botao1.move(100,100)
        botao1.resize(150,80)
        botao1.setStyleSheet('QPushButton {background-color:#0fd328;fonte:bold;font-size:20px }')
        botao1.clicked.connect(self.botao_click)

        botao2 = QPushButton('Botao2', self)
        botao2.move(300, 100)
        botao2.resize(150, 80)
        botao2.setStyleSheet('QPushButton {background-color:#0fa4b1;fonte:bold;font-size:20px }')
        botao2.clicked.connect(self.botao_click2)

        botao3 = QPushButton('Enviar Texto', self)
        botao3.move(500, 100)
        botao3.resize(150, 80)
        botao3.setStyleSheet('QPushButton {background-color:#ff5510;fonte:bold;font-size:20px }')
        botao3.clicked.connect(self.captura_texto)


        self.label_1 = QLabel(self)
        self.label_1.setText("Click em algum botão")
        self.label_1.setStyleSheet('QLabel {font-size: 30px}')
        self.label_1.move(30, 30)
        self.label_1.resize(500, 80)

        self.borboleta = QLabel(self)
        self.borboleta.move(150,300)
        self.borboleta.resize(200, 146)

        self.CarregarJanela()

    def CarregarJanela(self):
            self.setGeometry(self.esquerda, self.topo,self.largura, self.altura)
            self.setWindowTitle(self.titulo)
            self.show()

    def botao_click(self):
        self.label_1.setText('Borboleta 1')
        self.setStyleSheet('QLabel {fonte:bold;font-size:20px;color:green }')
        self.borboleta.setPixmap(QtGui.QPixmap('borboleta1.png'))

    def botao_click2(self):
        self.label_1.setText('Borboleta 2')
        self.setStyleSheet('QLabel {fonte:bold;font-size:20px;color:red }')
        self.borboleta.setPixmap(QtGui.QPixmap('borboleta2.jpg'))

    def captura_texto(self):
        conteudo = self.caixa_texto.text()
        self.label_caixa.setText('Digitou: ' + conteudo)


aplicacao = QApplication(sys.argv)
jan = Janela()
sys.exit(aplicacao.exec())
