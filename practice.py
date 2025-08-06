from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    get_titles = soup.find_all('h5', class_ = 'card-title')
    for getAll in get_titles:
        print(getAll.text)

    
    get_price = soup.find_all('div', class_='card-body')
    for prices in get_price:
        price = prices.a.text.split()[-1]
        print(price)

    text_p = soup.find_all('div', class_ = 'card-body')
    for get_p in text_p:
        description = get_p.p.text
        print(description)

        total_courses = len(soup.find_all('div', class_='card'))
        print(f'Total courses: {total_courses}')

    