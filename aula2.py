import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip


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
        print('O Botão 1 Foi Clicado')

    def botao2_click(self):
        print('O Botão 2 Foi Clicado')



aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())