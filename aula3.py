import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel


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
        botao1.setStyleSheet("QPushButton{background-color:green; font:bold; font-size:20px}")
        botao1.clicked.connect(self.botao1_click)
        self.label_1 = QLabel(self)
        self.label_1.setText('Aperte algum botão!')
        self.label_1.move(50, 50)
        self.label_1.resize(300, 30)
        self.label_1.setStyleSheet('QLabel {font:bold; font-size: 25px; color:blue}')

        botao2 = QPushButton('Botao 2', self)
        botao2.move(350, 200)
        botao2.resize(150, 80)
        botao2.setStyleSheet("QPushButton{background-color:red; font:bold; font-size:20px}")
        botao2.clicked.connect(self.botao2_click)



        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.largura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):

        self.label_1.setText('O Botão 1 foi clicado')
        self.label_1.setStyleSheet('QLabel {font:bold; font-size: 25px; color:violet}')

    def botao2_click(self):

        self.label_1.setText('O Botão 2 foi clicado')
        self.label_1.setStyleSheet('QLabel {font:bold; font-size: 25px; color:Brown}')


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())
