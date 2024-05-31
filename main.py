import re

from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

URL = 'https://news.ycombinator.com/'


def change_page_body(response):
    """adding to all six-letter words ™ symbols"""
    soup = BeautifulSoup(response.text, 'html.parser')

    for elem in soup.find_all(
        string=re.compile(r'.*(^|\s)\b(\w{6})\b($|\s)[\s\S]*')
    ):
        elem.string.replace_with(
            re.sub(r'\b(\w{6})\b', r'\1' + '™', elem.string)
        )
    for elem in soup.find_all(['img', 'link', 'script']):
        if elem.get('src'):
            elem['src'] = URL + elem['src']
        elif elem.get('href'):
            elem['href'] = URL + elem['href']

    return soup.prettify()


@app.get('/')
@app.get('/{path:path}')
async def serve_my_app(request: Request, path=''):
    query = f'?{request.query_params}' if request.query_params else ''
    response = requests.get(f'{URL}{path}{query}')
    changed_body = change_page_body(response)
    return HTMLResponse(content=changed_body, status_code=200)
