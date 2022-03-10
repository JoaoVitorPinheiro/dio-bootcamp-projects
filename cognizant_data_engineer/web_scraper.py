from bs4 import BeautifulSoup
import requests

link = 'https://www.globo.com'
# Objeto site recebendo o conteúdo da requisição
site = requests.get(link).content
# Objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')
#transforma html em string e exibe
print(soup.prettify)
print(soup.title)
print(soup.title.string)
search = soup.find("Tecnologia")
print(f"{search}")
