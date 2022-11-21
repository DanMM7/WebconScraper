from bs4 import BeautifulSoup
import requests

def get_all_customer_urls():
    try:
        page = requests.get('')
        soup = BeautifulSoup(page.content, features='html.parser')
    except Exception as e:
        print(e)