import requests
from bs4 import BeautifulSoup

## captura tudo quanto é html da página e transforma em um objeto(objeto response)
page = requests.get("http://www.uece.br/uece/index.php/conhecaauece/restauranteuniversitario")
#status = page.status_code		-> retorna se deu certo

## convertendo todo o conteúdo da string em objeto beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser')

## .tbody retorna todo o conteúdo da tag tbody
soup_tbody = soup.tbody

## .find_all(tag) retorna as tags da tag td que está dentro da tbody, mostrando o tipo das tags
listatd = soup_tbody.find_all('td')
for item in listatd:
	print(type(item))
	print(item.prettify())
	print("****************")

print("****************************************")
print("****************************************")

arquivo = open('content.txt', 'a')

## .get_text retorna o conteúdo da tag td e escreve no arquivo
final = soup.tbody.find_all('td')
for item in final:
	print(item.get_text())
	arquivo.write(item.get_text())