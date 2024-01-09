# Passo a passo do projeto

# Bibliotecas utilizadas
import time
import pandas as pd
import pyautogui
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar atalho -> pyautogui.hotkey
# scroll -> pyautogui.scroll

# Passo 1 - Entrar no sistema da empresa
URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
EMAIL = "test@email.br"
PASSWORD = "test123456"
pyautogui.PAUSE = 1

# aperta a tecla do windows
pyautogui.press('win')
# digite o nome do programa (chrome)
pyautogui.write('chrome')
# aperta enter
pyautogui.press('enter')
# digitar o link
pyautogui.write(URL)
# apertar enter
pyautogui.press('enter')

# esperar 5 segundos
time.sleep(5)

# Passo 2 - Fazer Login
# clicar no campo de email
pyautogui.click(x=461, y=383)
# Digitar o email
pyautogui.write(EMAIL)
# clicar no campo de senha
# pyautogui.click(x=555, y=484)
pyautogui.press('tab')
# Digitar senha
pyautogui.write(PASSWORD)
# Clicar em logar
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)
pyautogui.press('esc')

# Passo 3 - Importar a base de dados

tabela = pd.read_csv('produtos.csv')

# print(tabela)

# Passo 4 - Cadastrar um produto
def adicionar_produto(produto: object) -> None:
    """Função responsável por preencher os dados do produto na pagina e salvá-lo

    Args:
        produto (object): O produto é um objeto que deve conter:
            Código, Marca
            Tipo
            Categoria
            Preço Unitário
            Custo
            Obs
    """
    # Clicar no campo de código do produto e inserí-lo
    pyautogui.click(x=561, y=266)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)

    # MARCA
    marca = tabela.loc[linha, 'marca']
    pyautogui.press('tab')
    pyautogui.write(marca)

    # TIPO
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.press('tab')
    pyautogui.write(tipo)

    # Categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.press('tab')
    pyautogui.write(categoria)

    # Preço unitário
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.press('tab')
    pyautogui.write(preco_unitario)

    # Custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.press('tab')
    pyautogui.write(custo)

    # obs
    obs = tabela.loc[linha, 'obs']
    pyautogui.press('tab')
    if not pd.isna(obs):
        pyautogui.write(obs)

    # Salvar o produto
    pyautogui.press('tab')
    pyautogui.press('enter')

    # rolar para o topo da tela
    pyautogui.scroll(2000)


# Passo 5 - Repetir isso até acabar a base de dados
for linha in tabela.index:
    adicionar_produto(linha)
