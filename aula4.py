import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = 'Primeira Janela'

        botao1 = QPushButton('Botao 1', self)
        botao1.move(150, 200)
        botao1.resize(150, 80)
        botao1.setStyleSheet("QPushButton{background-color:blue; font:bold; font-size:20px}")
        botao1.clicked.connect(self.botao1_click)
        self.label_1 = QLabel(self)
        self.label_1.setText('Aperte algum botão!')
        self.label_1.move(50, 100)
        self.label_1.resize(360, 50)
        self.label_1.setStyleSheet('QLabel {font:bold; font-size: 30px; color:green}')

        self.carro = QLabel(self)
        self.carro.move(50, 400)
        self.carro.setPixmap(QtGui.QPixmap('carro azul.png'))
        self.carro.resize(450, 200)

        botao2 = QPushButton('Botao 2', self)
        botao2.move(350, 200)
        botao2.resize(150, 80)
        botao2.setStyleSheet("QPushButton{background-color:red; font:bold; font-size:20px}")
        botao2.clicked.connect(self.botao2_click)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label_1.setText('Carro Azul selecionado')
        self.label_1.setStyleSheet('QLabel {font:bold; font-size: 25px; color:blue}')
        self.carro.setPixmap(QtGui.QPixmap('carro azul.png'))

    def botao2_click(self):
        self.label_1.setText('Carro Vermelho selecionado')
        self.label_1.setStyleSheet('QLabel {font:bold; font-size: 25px; color:red}')
        self.carro.setPixmap(QtGui.QPixmap('carro vermelho.png'))


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
