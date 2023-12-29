from requests_html import HTMLSession # cira uma sessão HTML
from bs4 import BeautifulSoup # faz o parsing do conteudo HTML


#Criar a sessão html

sessao = HTMLSession()

# fazer faz a requisição (get do site )
r = sessao.get('https://catalogo.anqep.gov.pt/ufcdDetalhe/9039')


r.html.render(sleep=5)

soup = BeautifulSoup(r.html.html, "html.parser")

#print(soup.prettify())
nome = soup.find_all("div", {"class": "innerpage-heading"})[0].find_all_next("h1")[0].text

print(nome)

print("--" * 10)

list = soup.find_all("div", {"class": "row"})[1].find_all_next("div", {"class","characteristics-box"})

print("dados da UFCD")
ps = list[0].find_all_next("p")

"""
for p in ps:
    if p.text.__contains__(":"):
        mylista = p.text.split(":")[1].strip()
        print(mylista)
"""

for p in ps:
    if p.text.__contains__(":"):
        dados = p.text.split(":")[1].strip()
        print(dados)


print("--" * 10)
print("obj da UFCD")



list = soup.find_all("div", {"class": "row"})[1].find_all_next("div", {"class","description-list"})

obj = list[0].find_all("li")

for p in obj:
    print(p.text.strip())

print("--" * 10)


contAll = list[1].find_all("li")

print("--" * 10)

print("Conteudos")
print(contAll)

def process(cont):
    res = []
    i = 0
    while i < cont.__len__():
        aux = []
        base = ''.join([str(content) for content in cont[i].contents if content.name != 'ul'])

        subLista = cont[i].find_all("ul")[0].find_all("li")
        sublistsize = subLista.__len__()

        aux.append(base)

        if sublistsize == 0:
            i += 1
        else:
            aux.append(process(subLista))
            i += sublistsize + 1


        res.append(aux)
    return res


print(process(contAll))

"""
[<li>Invenção da escrita
    <ul>
        <li>... <ul></ul></li>
        <li>... <ul></ul></li>
        <li>... <ul></ul></li>
        <li>...<ul></ul></li>
    </ul>
</li>, 

<li>Evolução da escrita<ul></ul></li>, 
<li>Invenção da tipografia<ul></ul></li>,
 <li>Evolução da tipografia<ul></ul></li>, 
 <li>Primeiros tipos de letra<ul></ul></li>, 
 <li>Unidade de medida “ponto”<ul></ul></li>
 ]
"""


"""

[ ['Linguagem estruturada', 
    [['Estruturas lógicas', 
        [['Estruturas lógicas', ], 
        ['Desenho das estruturas diagramáticas'], 
        ['Sintaxe da linguagem']
    ]
    ]
    ], 
    ['Desenho das estruturas diagramáticas'], 
    ['Sintaxe da linguagem']
    ]
    ], 
['Construção de um algoritmo', 
    [
        ['Noções de ação e estado da ação'], 
        ['Acções e a sua sintaxe'], 
        ['Verbos'], ['Sintaxe'],
         ['Alinhamento das frases']
         
    ],

"""

"""

[['Métodos de exploração'], 
['Métodos auxiliares de caça', 
[['Secretários batedores, negaceiros, largadas']]],
 ['Secretários batedores, negaceiros, largadas'], 
 ['Tipos e caracterização dos métodos de caça mais utilizados na atividade cinegética', 
    [['Largada'], 
    ['Montaria'], 
    ['Batida'],
    ['De espera'],
    ['De salto'], 
    ['Outras']]], 
  ['Largada'], ['Montaria'], ['Batida'], ['De espera'], ['De salto'], ['Outras'], ['Troféus'], ['Fiscalização nas jornadas de caça'], ['Boas práticas de segurança, higiene e saúde']]

"""