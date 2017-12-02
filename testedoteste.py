import requests
from bs4 import BeautifulSoup

## captura tudo quanto é html da página e transforma em um objeto(objeto response)
page = requests.get("http://www.uece.br/uece/index.php/conhecaauece/restauranteuniversitario")
#status = page.status_code		-> retorna se deu certo

## convertendo todo o conteúdo da string em objeto beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser')

## .tbody retorna todo o conteúdo da tag tbody
soup_tbody = soup.tbody

## .find_all(tag) retorna o conteúdo da tag td que está dentro da tbody
listatr = soup_tbody.find_all('td')
for item in listatr:
	print(item.prettify())