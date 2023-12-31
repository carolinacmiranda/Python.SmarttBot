import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

import conftest


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.pagina_logada = (By.XPATH, "//*[contains(text(), 'Análise geral')]")
        self.botao_criar_robo = (By.XPATH, "//*[contains(text(), 'Criar Robô')]")
        self.criacao_facil = (By.XPATH, "//*[contains(text(), 'Escolher Robô')]")
        self.robo_dourado = (By.XPATH, "(//*[contains(text(), 'Criar')])[2]")
        self.modo_simulado = (By.XPATH, "(//sb-button[@data-testid='button'][contains(.,'Configurar')])[1]")
        self.botao_play = (By.XPATH, "(//*[contains(text(), 'Play')])")
        self.botao_segundo_play = (By.XPATH, "//sb-button[contains(@data-testid,'play-button')]")
        self.criacao_completa = (By.XPATH, "//sb-button[@type='solid'][contains(.,'Configurar')]")
        self.robo_sardinha = (By.XPATH, "//div[@class='truncate'][contains(.,'SardinhaAutor: SmarttBot')]")
        self.botao_avancar = (By.XPATH, "//sb-button[@type='link'][contains(.,'Avançar')]")
        self.botao_salvar = (By.XPATH, "//button[contains(@aria-label,'Salvar')]")
        self.botao_iniciar = (By.XPATH, "//button[starts-with(@id, 'simulado_robo_iniciar')]")
        self.verificar_status_modo_facil = (By.XPATH, "//button[starts-with(@id, 'simulado_robo_parar')]")
        self.verificar_status_modo_completo = (By.XPATH, "//button[contains(@aria-label,'Parar')]")
        self.modal_confirmacao_parar_robo = (By.XPATH, "//button[@name='confirm'][contains(.,'Sim, parar mesmo assim')]")
        self.modal_robo_parado_com_sucesso = (By.XPATH, "//sb-result-modal[contains(@title,'Robô parado com sucesso!')]")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.pagina_logada)

    def criar_robo_modo_facil(self):
        self.clicar(self.botao_criar_robo)
        self.clicar(self.criacao_facil)
        self.clicar(self.robo_dourado)
        self.clicar(self.modo_simulado)
        self.clicar(self.botao_play)
        time.sleep(1)
        self.clicar_modal_confirmacao()
        self.clicar(self.botao_segundo_play)

    def criar_robo_modo_completo(self, text):
        self.clicar(self.botao_criar_robo)
        self.clicar(self.criacao_completa)
        self.clicar(self.robo_sardinha)
        self.clicar(self.modo_simulado)
        self.preencher_nome_robo_shadow(text)
        self.clicar(self.botao_avancar)
        self.clicar(self.botao_salvar)
        time.sleep(1)
        self.clicar_modal_confirmacao()
        self.clicar(self.botao_iniciar)

    def verificar_status_do_robo_modo_facil(self):
        self.verificar_se_elemento_existe(self.verificar_status_modo_facil)

    def parar_robo_modo_facil(self):
        self.clicar(self.verificar_status_modo_facil)
        time.sleep(1)
        self.clicar(self.modal_confirmacao_parar_robo)

    def verificar_status_parado_modo_facil(self):
        time.sleep(1)
        self.verificar_se_elemento_existe(self.modal_robo_parado_com_sucesso)

    def verificar_status_do_robo_modo_completo(self):
        self.verificar_se_elemento_existe(self.verificar_status_modo_completo)

    def parar_robo_modo_completo(self):
        self.clicar(self.verificar_status_modo_completo)
        time.sleep(1)
        self.clicar(self.modal_confirmacao_parar_robo)

    def verificar_status_parado_modo_completo(self):
        time.sleep(1)
        self.verificar_se_elemento_existe(self.modal_robo_parado_com_sucesso)
