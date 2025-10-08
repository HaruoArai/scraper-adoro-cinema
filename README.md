# 🎬 AdoroCinema Scraper 

Este projeto realiza a raspagem de críticas de filmes do site [AdoroCinema](https://www.adorocinema.com), classificando-as como **positivas** ou **negativas** com base na nota atribuída pelos usuários.

## 📦 Funcionalidades

- Coleta automática de críticas de múltiplos filmes;
- Extração de nota e texto da crítica;
- Classificação de sentimento (positiva/negativa);
- Exportação dos dados para CSV compatível com Excel. 

## 🧰 Tecnologias Utilizadas

- **Visual Studio Code (VS Code)**: ambiente de desenvolvimento recomendado e utilizado neste trabalho.
- **Python**: linguagem principal do projeto.
- **Selenium + ChromeDriver**: automação de navegador para raspagem de dados.
- **Pandas**: manipulação e exportação de dados em formato tabular.
- **Expressões Regulares (re)**: extração de notas das críticas.
- **CSV**: formato de saída dos dados coletados.

## 💻 Como executar o projeto (Windows 10/11 + VS Code)

### 1. Instale os programas necessários

- [Visual Studio Code](https://code.visualstudio.com/) com a extensão **Python**
- [Python](https://www.python.org/downloads) (versão 3.10 ou superior)
- [Google Chrome](https://www.google.com/chrome/) (necessário para o Selenium funcionar corretamente)

---

### 2. Prepare o ambiente no VS Code

- Crie uma pasta chamada `adoro-cinema`
- Coloque o arquivo `scraper.py` disponibilizado neste repositório dentro da pasta

Abra o terminal do VS Code (`Ctrl + Shift + '` ou vá em **Terminal → Novo Terminal**) e siga os passos abaixo:

---

#### a) Verifique se o Python está instalado

```bash
py --version

---

#### b) Instale as bibliotecas necessárias

py -m pip install selenium pandas requests beautifulsoup4

---

#### c) Execute o programa

py scraper.py

---

### 3. Resultado final

- Ao terminar, será gerado o arquivo: reviews_adorocinema_multifilmes.csv
- Esse arquivo estará na mesma pasta do projeto e conterá todas as críticas coletadas, com as colunas:
• **id** → número identificador da crítica;  
• **nota** → avaliação atribuída pelo usuário (de 0 a 5);  
• **texto** → conteúdo da crítica escrita;  
• **rotulo** → classificação da crítica como positiva ou negativa, com base na nota.


