from selenium import webdriver # Biblioteca usada para automação de navegador.
from selenium.webdriver.common.by import By # Biblioteca usada para localizar elementos HTML.
from selenium.webdriver.support.ui import WebDriverWait # Biblioteca usada para esperar elementos carregarem.
from selenium.webdriver.support import expected_conditions as EC # Condições de espera
import pandas as pd # Biblioteca usada para manipular dados em formato de tabela.
import time # Biblioteca usada para controle de tempo.
import re # Biblioteca usada para usar expressões regulares.

# Lista de URLs dos filmes (retirados do adorocinema):
urls = [
    "https://www.adorocinema.com/filmes/filme-1000006302/criticas/espectadores/", # Demon Slayer: Kimetsu no Yaiba - Castelo Infinito
    "https://www.adorocinema.com/filmes/filme-1000006302/criticas/espectadores/?page=2", # Demon Slayer: Kimetsu no Yaiba - Castelo Infinito
    "https://www.adorocinema.com/filmes/filme-1000006302/criticas/espectadores/?page=3", # Demon Slayer: Kimetsu no Yaiba - Castelo Infinito
    "https://www.adorocinema.com/filmes/filme-1000006302/criticas/espectadores/?page=4", # Demon Slayer: Kimetsu no Yaiba - Castelo Infinito
    "https://www.adorocinema.com/filmes/filme-1000006302/criticas/espectadores/?page=5", # Demon Slayer: Kimetsu no Yaiba - Castelo Infinito
    "https://www.adorocinema.com/filmes/filme-309613/criticas/espectadores/", # Invocação do Mal 4: O Último Ritual
    "https://www.adorocinema.com/filmes/filme-309613/criticas/espectadores/?page=2", # Invocação do Mal 4: O Último Ritual
    "https://www.adorocinema.com/filmes/filme-10568/criticas/espectadores/", # Forrest Gump - O Contador de Histórias
    "https://www.adorocinema.com/filmes/filme-10568/criticas/espectadores/?page=2", # Forrest Gump - O Contador de Histórias
    "https://www.adorocinema.com/filmes/filme-11736/criticas/espectadores/", # Um Sonho de Liberdade
    "https://www.adorocinema.com/filmes/filme-11736/criticas/espectadores/?page=2", # Um Sonho de Liberdade
    "https://www.adorocinema.com/filmes/filme-311364/criticas/espectadores/star-0/", # Uma Batalha Após A Outra
    "https://www.adorocinema.com/filmes/filme-304992/criticas/espectadores/star-1/", # Ursinho Pooh: Sangue e mel
    "https://www.adorocinema.com/filmes/filme-304992/criticas/espectadores/star-0/", # Ursinho Pooh: Sangue e mel
    "https://www.adorocinema.com/filmes/filme-304992/criticas/espectadores/star-0/?page=2", # Ursinho Pooh: Sangue e mel
    "https://www.adorocinema.com/filmes/filme-266320/criticas/espectadores/star-2/", # M3GAN
    "https://www.adorocinema.com/filmes/filme-7124/criticas/espectadores/", # O Exterminador do Futuro 2 - O Julgamento Final
    "https://www.adorocinema.com/filmes/filme-7124/criticas/espectadores/?page=2", # O Exterminador do Futuro 2 - O Julgamento Final
    "https://www.adorocinema.com/filmes/filme-7124/criticas/espectadores/?page=3", # O Exterminador do Futuro 2 - O Julgamento Final
    "https://www.adorocinema.com/filmes/filme-118948/criticas/espectadores/star-0/", # Os Estranhos
    "https://www.adorocinema.com/filmes/filme-326355/criticas/espectadores/star-5/", # Pecadores
    "https://www.adorocinema.com/filmes/filme-15002/criticas/espectadores/star-5/", # Um Drink no Inferno
    "https://www.adorocinema.com/filmes/filme-28541/criticas/espectadores/star-5/", # Kill Bill - Volume 1
    "https://www.adorocinema.com/filmes/filme-34193/criticas/espectadores/star-3/", # Donnie Darko
    "https://www.adorocinema.com/filmes/filme-131377/criticas/espectadores/star-0/", # Crepúsculo
    "https://www.adorocinema.com/filmes/filme-43225/criticas/espectadores/star-5/", # O Predador
    "https://www.adorocinema.com/filmes/filme-43225/criticas/espectadores/star-4/", # O Predador
    "https://www.adorocinema.com/filmes/filme-22092/criticas/espectadores/star-5/", # O Sexto Sentido
    "https://www.adorocinema.com/filmes/filme-22092/criticas/espectadores/star-4/", # O Predador
    "https://www.adorocinema.com/filmes/filme-242492/criticas/espectadores/star-1/", # O Jurassic World: Domínio
    "https://www.adorocinema.com/filmes/filme-33906/criticas/espectadores/", # Cruzeiro das Loucas
    "https://www.adorocinema.com/filmes/filme-47179/criticas/espectadores/star-5/", # Click
    "https://www.adorocinema.com/filmes/filme-448/criticas/espectadores/star-5/", # De Volta para o Futuro
    "https://www.adorocinema.com/filmes/filme-264422/criticas/espectadores/star-2/", # Annabelle 3: De Volta para Casa
    "https://www.adorocinema.com/filmes/filme-264422/criticas/espectadores/star-2/?page=2", # Annabelle 3: De Volta para Casa
    "https://www.adorocinema.com/filmes/filme-263120/criticas/espectadores/star-2/", # A Maldição da Chorona
    "https://www.adorocinema.com/filmes/filme-304967/criticas/espectadores/star-2/", # Sorria
    "https://www.adorocinema.com/filmes/filme-141609/criticas/espectadores/star-1/", # O Exterminador do Futuro: Gênesis
    "https://www.adorocinema.com/filmes/filme-141609/criticas/espectadores/star-2/", # O Exterminador do Futuro: Gênesis
    "https://www.adorocinema.com/filmes/filme-141609/criticas/espectadores/star-2/?page=2", # O Exterminador do Futuro: Gênesis
    "https://www.adorocinema.com/filmes/filme-140991/criticas/espectadores/star-0/", # A Saga Crepúsculo: Lua Nova
    "https://www.adorocinema.com/filmes/filme-140991/criticas/espectadores/star-1/", # A Saga Crepúsculo: Lua Nova
    "https://www.adorocinema.com/filmes/filme-140991/criticas/espectadores/star-1/?page=2", # A Saga Crepúsculo: Lua Nova
    "https://www.adorocinema.com/filmes/filme-112361/criticas/espectadores/star-0/", # Todo Mundo em Pânico 5
    "https://www.adorocinema.com/filmes/filme-112361/criticas/espectadores/star-0/?page=2", # Todo Mundo em Pânico 5
    "https://www.adorocinema.com/filmes/filme-112361/criticas/espectadores/star-1/", # Todo Mundo em Pânico 5
    "https://www.adorocinema.com/filmes/filme-26077/criticas/espectadores/star-4/", # Todo Mundo em Pânico 5
    "https://www.adorocinema.com/filmes/filme-54456/criticas/espectadores/star-5/", # As Branquelas
    "https://www.adorocinema.com/filmes/filme-54456/criticas/espectadores/star-5/?page=2", # As Branquelas
    "https://www.adorocinema.com/filmes/filme-54456/criticas/espectadores/star-5/?page=3", # As Branquelas
    "https://www.adorocinema.com/filmes/filme-114782/criticas/espectadores/star-5/", # Interestelar
    "https://www.adorocinema.com/filmes/filme-225218/criticas/espectadores/star-1/", # Annabelle 
    "https://www.adorocinema.com/filmes/filme-225218/criticas/espectadores/star-1/?page=2", # Annabelle 
    "https://www.adorocinema.com/filmes/filme-225218/criticas/espectadores/star-0/", # Annabelle 
    
]

# Inicializa o navegador Chrome.
driver = webdriver.Chrome()
driver.maximize_window() # Maximiza a janela para garantir visibilidade dos elementos.

# Lista para armazenar todas as críticas coletadas.
reviews = []
contador = 1  # Contador para atribuir um ID único a cada crítica.

# Loop para visitar cada URL da lista.
for url in urls:
    driver.get(url) # Acessa a página da URL atual.
    print(f"Coletando críticas de: {url}") # Exibe no terminal qual página está sendo processada.

    try:
        # Aguarda até que os elementos de crítica estejam visíveis na página.
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".review-card"))
        )
    except:
        # Se os elementos não carregarem, exibe aviso e pula para a próxima URL.
        print(f"Não foi possível carregar críticas de: {url}")
        continue

    # Coleta os primeiros 10 blocos de crítica da página (máximo de críticas por página no adorocinema).    
    blocos = driver.find_elements(By.CSS_SELECTOR, ".review-card")[:10]

    # Loop para processar cada bloco de crítica.
    for bloco in blocos:
        try:
            texto_completo = bloco.text.strip() # Extrai o texto bruto do bloco.
            match = re.search(r"(\d,\d)\s+Enviada", texto_completo) # Busca a nota usando expressão regular.
            if not match:
                continue # Se não encontrar a nota, ignora essa crítica.

            nota = float(match.group(1).replace(",", ".")) # Converte a nota para formato numérico.

            try:
                # Tenta extrair o texto da crítica usando seletor específico. 
                texto = bloco.find_element(By.CSS_SELECTOR, ".content-txt").text.strip()
            except:
                # Se falhar, usa o texto bruto como alternativa.
                partes = texto_completo.split("Enviada em")
                texto = partes[1].strip() if len(partes) > 1 else ""

            # Define o rótulo com base na nota.
            rotulo = "positiva" if nota >= 3 else "negativa"

            # Adiciona os dados da crítica à lista.
            reviews.append([contador, nota, texto, rotulo])
            contador += 1 # Incrementa o ID para a próxima crítica.
        except Exception as e:
            # Se ocorrer erro ao processar a crítica, exibe aviso e continua.
            print(f"Erro ao processar crítica: {e}")
            continue

# Encerra o navegador após o término da coleta.
driver.quit()

# Cria um DataFrame com os dados coletados.
df = pd.DataFrame(reviews, columns=["id", "nota", "texto", "rotulo"])

# Salva os dados em um arquivo CSV com separador compatível com Excel.
df.to_csv("reviews_adorocinema_multifilmes.csv", index=False, encoding="utf-8-sig", sep=";")

# Exibe resumo da coleta no terminal.
print(f"Coletadas {len(df)} críticas de {len(urls)} filmes com sucesso!")
print(df.head()) # Mostra as primeiras linhas da tabela.
