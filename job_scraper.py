from bs4 import BeautifulSoup
import requests

url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
html_text = requests.get(url, verify=False).text  # verify=False solo para pruebas

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    company_name_tag = job.find('h3', class_='joblist-comp-name')
    skills_tag = job.find('span', class_='srp-skills')
    posted_tag = job.find('span', class_='sim-posted')

    company_name = company_name_tag.text.strip() if company_name_tag else "No company found"
    jobs_skills = skills_tag.text.strip() if skills_tag else "No skills found"
    getDay = posted_tag.text.strip() if posted_tag else "No date found"

    print(f'''
    Company Name: {company_name}
    Required Skills: {jobs_skills}
    Posted: {getDay}
    ''')
