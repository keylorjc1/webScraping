from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    # titulos = soup.find_all('h5', class_ = 'card-title')
    # for getTitutlo in titulos:
    #     print(getTitutlo.text)


    # precio = soup.find_all('div', class_ = 'card-body')
    # for getPrecios in precio:
    #     lastPrice = getPrecios.a.text.split()[-1]
    #     print(lastPrice)
    
    # contenidoP = soup.find_all('p', class_ = 'card-text')
    # for encontrar in contenidoP:
    #     print(encontrar.text)
    
    # contarCursos = len(soup.find_all('div', class_ = 'card'))
    # print(contarCursos)

    # cuestenMas = soup.find_all('div', class_ = 'card-body')

    # for contando in cuestenMas:
    #     numeroEncontrado = int(contando.a.text.split()[-1].replace('$', ''))
    #     if numeroEncontrado > 30:
    #         print(numeroEncontrado)

    # mostrarId = soup.find_all('div', class_ = 'card')

    # for buscandoId in mostrarId:
    #     idCard = buscandoId.get('id')
    #     print(idCard)


    # encontrarTexto = soup.find_all('div', class_ = 'card-body')

    # for subject in encontrarTexto:
    #     if 'Python' in subject.h5.text:
    #         print(subject.h5.text)

    # NombreCurso = soup.find_all('div', class_ = 'card-body')

    # for encontrandoText in NombreCurso:
    #     titulo = encontrandoText.h5.text
    #     precio = encontrandoText.a.text.split()[-1]

    #     print ( titulo + ' ' + precio )

    