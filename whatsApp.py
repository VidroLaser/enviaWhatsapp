import os
import sys
import time

from selenium import webdriver  # pip install selenium
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchWindowException, \
    NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def config_driver():
    try:
        options = webdriver.ChromeOptions()

        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        options.add_argument(f"user-data-dir={user_data_dir}")

        driver = webdriver.Chrome(options=options)  # Sem necessidade de especificar o caminho do driver
        wait = WebDriverWait(driver, 600)  # Espera até 10 minutos para o QR Code ser escaneado
        return driver, wait
    except WebDriverException:
        print("Erro na configuração do Drive")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao configurar o driver: {e}")
        return None, None


def open_whatsapp(driver, wait):
    try:
        driver.get("https://web.whatsapp.com")
        # Esperar o campo de mensagem estar disponível
        wait.until(ec.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
    except NoSuchWindowException:
        print("Erro ao abrir o Whatsapp")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado {e}")
        sys.exit(1)


def buscar_contato(driver, contato):
    try:
        campo_pesquisa = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        time.sleep(2)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        campo_pesquisa.send_keys(Keys.ENTER)
        time.sleep(2)
    except ElementClickInterceptedException:
        print(f"Erro ao buscar contato")
        sys.exit(1)
    except NoSuchWindowException:
        print("Janela ja foi fechada")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado {e} ")


def limpa_contato(driver):
    try:
        campo_pesquisa = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        time.sleep(2)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(Keys.ESCAPE)
        time.sleep(2)
    except ElementClickInterceptedException:
        print(f"Erro ao apagar contato")
        sys.exit(1)
    except NoSuchWindowException:
        print("Janela ja foi fechada")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado {e} ")


def append_file_click(driver):
    try:
        attach_button = driver.find_element(By.XPATH, '//div[@title="Anexar"]')
        attach_button.click()
        time.sleep(2)
    except ElementClickInterceptedException:
        print(f"Erro ao clicar no botão de anexar")
    except NoSuchWindowException:
        print("Janela ja foi fechada")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado: {e} ")


def anexa_arquivos(driver, pdf_path):
    try:
        # Clicar no botão de anexar documento
        document_button = driver.find_element(By.XPATH, '//input[@accept="*"]')
        document_button.send_keys(os.path.abspath(pdf_path))
    except ElementClickInterceptedException:
        print(f"Erro ao anexar arquivos")
    except NoSuchElementException:
        print(f"Sem arquivos")
    except NoSuchWindowException:
        print("Janela ja foi fechada")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado: {e} ")


def enviar_mensagem(driver, mensagem):
    try:
        campo_mensagem = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        time.sleep(2)
        campo_mensagem.click()
        campo_mensagem.send_keys(mensagem)
        campo_mensagem.send_keys(Keys.RETURN)
    except ElementClickInterceptedException:
        print(f"Erro ao enviar mensagem")
    except NoSuchWindowException:
        print("Janela ja foi fechada")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado: {e} ")


def enviar(driver):
    try:
        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()
    except ElementClickInterceptedException:
        print(f"Erro ao clicar no botão de enviar")
    except NoSuchElementException:
        print(f"Sem arquivos")
    except NoSuchWindowException:
        print("Janela ja foi fechada")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado: {e} ")


def close_driver(driver):
    try:
        driver.quit()
    except NoSuchWindowException:
        print("Janela ja foi fechada")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao fechar o driver: {e}")
        sys.exit(1)
