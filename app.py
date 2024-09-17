from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import openpyxl
import schedule
from selenium.webdriver.chrome.options import Options
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
import sys
from interface import Ui_MainWindow  # Arquivo gerado pelo pyuic5
from PyQt5.QtCore import QThread, pyqtSignal


class ConsultaThread(QThread):
    status_atualizado = pyqtSignal(str)  # Sinal para atualizar o lbl_status
    preco_atualizado = pyqtSignal(str)  # Sinal para atualizar o lbl_preco
    consulta_concluida = pyqtSignal()  # Sinal para indicar que a consulta terminou

    def __init__(self, bot, produto, url):
        super().__init__()
        self.bot = bot
        self.produto = produto
        self.url = url

    def run(self):
        self.status_atualizado.emit(f"Consultando preço do produto: {self.produto}")
        driver = self.bot.iniciar_driver()

        self.status_atualizado.emit(f"Acessando a página do produto......")
        driver.get(self.url)

        try:
            self.status_atualizado.emit("Procurando o preço no site...")
            time.sleep(5)
            preco_element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[7]/div[5]/div/div/div/div/p')
            preco_texto = preco_element.text
            preco_numerico = float(preco_texto.replace('R$', '').replace('.', '').replace(',', '.').strip())

            self.preco_atualizado.emit(f"R${preco_numerico}")
            self.status_atualizado.emit(f"Preço encontrado: R${preco_numerico}")

            # Adicionar na tabela de histórico
            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.bot.adicionar_historico(self.produto, data_atual, preco_numerico, self.url)

            # Salvar na planilha Excel
            self.status_atualizado.emit("Atualizando a planilha de preços...")
            time.sleep(5)
            self.bot.atualizar_planilha(self.produto, data_atual, preco_numerico, self.url)
            time.sleep(5)
            self.status_atualizado.emit("Preço registrado com sucesso na planilha.")

        except Exception as e:
            self.status_atualizado.emit(f"Erro ao consultar o preço: {e}")
        finally:
            driver.quit()
            self.status_atualizado.emit("Consulta finalizada e WebDriver encerrado.")
            self.consulta_concluida.emit()

class PrecoBot(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PrecoBot, self).__init__()
        self.setupUi(self)

        # Conectar botões com as funções
        self.btn_iniciar.clicked.connect(self.iniciar_consulta)
        self.btn_parar.clicked.connect(self.parar_consulta)

        # Timer para atualizar a consulta de 30 em 30 minutos
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.consultar_preco)

        # Variável de controle para rodar ou parar as consultas
        self.consultando = False
    
    def iniciar_driver(self):
        """Configura e inicia o WebDriver."""
        self.lbl_status.setText("Iniciando o WebDriver...")
      
        chrome_options = Options()
        arguments = [
            '--lang=pt-BR',
            '--window-size=800,600',
            '--incognito',
            '--disable-notifications'
        ]
        for argument in arguments:
            chrome_options.add_argument(argument)

        driver = webdriver.Chrome(options=chrome_options)
        self.lbl_status.setText("WebDriver iniciado com sucesso.")
        return driver
    
    def consultar_preco(self):
        produto = "NoteBook Vaio FE15 AMD Ryzen"
        url = "https://www.magazineluiza.com.br/notebook-vaio-fe15-amd-ryzen-5-16gb-ram-ssd-512gb-156-full-hd-windows-11-3344279/p/238469000/in/fe15/"

        # Criar e iniciar a thread de consulta
        self.thread = ConsultaThread(self, produto, url)
        self.thread.status_atualizado.connect(self.lbl_status.setText)
        self.thread.preco_atualizado.connect(self.lbl_preco.setText)
        self.thread.consulta_concluida.connect(self.timer.start)  # Reiniciar o timer ao fim da consulta
        self.thread.start()

    def adicionar_historico(self, produto, data, preco, url):
        linha = self.table_historico.rowCount()
        self.table_historico.insertRow(linha)
        self.table_historico.setItem(linha, 0, QtWidgets.QTableWidgetItem(produto))
        self.table_historico.setItem(linha, 1, QtWidgets.QTableWidgetItem(data))
        self.table_historico.setItem(linha, 2, QtWidgets.QTableWidgetItem(f"R${preco}"))
        self.table_historico.setItem(linha, 3, QtWidgets.QTableWidgetItem(url))

    def atualizar_planilha(self, produto, data, preco, url):
        nome_arquivo = 'precos_produto.xlsx'
        
        try:
            # Tentar abrir a planilha existente
            workbook = openpyxl.load_workbook(nome_arquivo)
            sheet = workbook.active
        except FileNotFoundError:
            # Criar uma nova planilha se não existir
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            # Criar cabeçalho
            sheet.append(['Produto', 'Data', 'Valor', 'Link'])
        
        # Adicionar os dados
        sheet.append([produto, data, preco, url])
        
        # Salvar a planilha
        workbook.save(nome_arquivo)
    
    def iniciar_consulta(self):
        """Inicia o processo de consulta de preço de 30 em 30 minutos."""
        self.consultando = True
        self.lbl_status.setText("Consulta iniciada!")
        self.timer.start(1800000)  # 30 minutos em milissegundos
        self.consultar_preco()  # Executa a primeira consulta imediatamente
    
    def parar_consulta(self):
        """Para o processo de consulta."""
        self.consultando = False
        self.timer.stop()
        self.lbl_status.setText("Consulta parada!")
        

# Inicializando a aplicação
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    janela = PrecoBot()
    janela.show()
    sys.exit(app.exec_())
