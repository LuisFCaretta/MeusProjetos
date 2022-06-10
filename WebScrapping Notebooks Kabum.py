from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import math
from time import sleep
import smtplib
import email.message

URL = "https://www.kabum.com.br/computadores/notebooks?page_number=1&page_size=20&facet_filters=eyJjYXRlZ29yeSI6WyJDb21wdXRhZG9yZXMiXSwicHJpY2UiOnsibWluIjo5MjMuNzYsIm1heCI6OTk5OTkuOTl9fQ==&sort=most_searched"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33"}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, "html.parser")
qtd_itens = soup.find("div", id="listingCount").get_text().strip()
index = qtd_itens.index(' ')
qtd = qtd_itens[:index]
print(f"Quantidade de intens: {qtd}.")

ultima_pagina = math.ceil(int(qtd)/20)

dict_notebooks = {"Nome": [], "Valor": []}
print("Coletando dados...")

for i in range(1, ultima_pagina+1):
    url_pag = f'https://www.kabum.com.br/computadores/notebooks?page_number={i}&page_size=20&facet_filters=eyJjYXRlZ29yeSI6WyJDb21wdXRhZG9yZXMiXSwicHJpY2UiOnsibWluIjo5MjMuNzYsIm1heCI6OTk5OTkuOTl9fQ==&sort=most_searched'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, "html.parser")
    produtos = soup.find_all('div', class_=re.compile("productCard"))
    for produto in produtos:
        Nome = produto.find("span", class_=re.compile('nameCard')).get_text()
        Valor = produto.find("span", class_=re.compile("priceCard")).get_text().strip().replace("R$", '')
        dict_notebooks["Nome"].append(Nome)
        dict_notebooks["Valor"].append(Valor)
print("Criando tabela...")
sleep(3)

#Lembre-se de criar um arquivo .csv em branco e refernciá-lo abaixo
df = pd.DataFrame(dict_notebooks)
df.to_csv("NotebooksKabum.csv", encoding='utf8', sep=";")
print(f"Exportado para Desktop")

"""
def enviar_email():
    email_content = "https://www.kabum.com.br/computadores/notebooks?page_number=1&page_size=20&facet_filters=eyJjYXRlZ29yeSI6WyJDb21wdXRhZG9yZXMiXSwicHJpY2UiOnsibWluIjo5MjMuNzYsIm1heCI6OTk5OTkuOTl9fQ==&sort=most_searched" #Link aqui do site ou produto
    msg = email.message.Message()
    msg["Subject"] = "Seu arquivo 'NotebooksKabum.csv' está pronto!" #Mensagem que deseja enviar
    msg["From"] = "" #Aqui o email do remetente
    msg["To"] = "" #Aqui o email do destinatário
    password = "" #Senha do remetente
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(email_content)
    s = smtplib.SMTP("smtp.gmail.com:587")
    s.starttls()
    s.login(msg["From"], password)
    s.sendmail(msg["From"], msg["To"], msg.as_string())
    print(f"Email enviado para: {msg['To']}")
enviar_email()
"""

