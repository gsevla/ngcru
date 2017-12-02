import requests

page = requests.get("http://www.uece.br/uece/index.php/conhecaauece/restauranteuniversitario")
status = page.status_code

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html>
	<head>
		<title>O TESTE MASTER</title>
	</head>
	<body>
		<p>Testando</p>
		<p>Testando 123</p>
	</body>
</html>
"""

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
list(soup.children)
#[type(item) for item in list(soup.children)]
'''for item in list(soup.children):
	if(type(item) != type(list(soup.children)[2])):
		print("********")
		print(type(item))
		print(item)'''

print(soup.tbody)