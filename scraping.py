from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import mysql.connector
import re

data_connection = {"user": "root",
                   "password": "Yecgaa134",
                   "host": "127.0.0.1",
                   "database": "scraping",
                   "charset": "utf8"}

connection = mysql.connector.connect(**data_connection)
cursor = connection.cursor()


def record_data(title, url, contents):
    """ function to record the data """
    cursor.execute("insert into paginas (title, url, contents "
                   "values (%s, %s, %s", (title, url, contents))

    connection.commit()


def get_links(url_old):
    """ function to return page links """
    url = "http://pt.wikipedia.org" + url_old
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    title = bs.find("h1").get_text()
    contents = bs.find("div", {"id": "mw-content-text"}).find("p").get_text()
    record_data(title, url, contents)

    return bs.find("div", {"id": "bodyContent"}).\
        findAll("a", href=re.compile('^(/wiki/)((?!:).)*$'))


links = get_links('/wiki/Copa_do_Mundo_FIFA_de_2026')

try:
    cont = 1
    while len(links) > 0 and cont <= 10:
        new_article = links[random.randint(0, len(links) - 1)].attrs["href"]
        links = get_links(new_article)
        cont += 1
finally:
    cursor.close()
    connection.close()
