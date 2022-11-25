from bs4 import BeautifulSoup
import requests



def get_all_customer_urls():
    try:
        page = requests.get('https://stackoverflow.com/questions/45368525/excel-data-load-into-azure-sql-using-sql-query')
        soup = BeautifulSoup(page.content, features='html.parser')
        print(soup)
        # for form in soup.find_all('input', id_='post-id'):
        #     print(form)
    except Exception as e:
        print(e)
