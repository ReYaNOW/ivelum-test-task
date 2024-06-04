import re

import aiohttp
from bs4 import BeautifulSoup
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

URL = 'https://news.ycombinator.com/'


@app.get('/{path:path}')
async def serve_my_app(request: Request, path=''):
    query = f'?{request.query_params}' if request.query_params else ''
    response = await make_request(f'{URL}{path}{query}')
    changed_body = change_page_body(response)
    return HTMLResponse(content=changed_body, status_code=200)


async def make_request(final_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(final_url) as response:
            return await response.read()


def change_page_body(text):
    """adding to all six-letter words ™ symbols"""
    soup = BeautifulSoup(text, 'html.parser')

    for elem in soup.find_all(string=re.compile(r'\b\w{6}\b')):
        elem.replace_with(re.sub(r'\b(\w{6})\b', r'\1™', elem))

    for elem in soup.find_all(['img', 'link', 'script']):
        if elem.get('src'):
            elem['src'] = URL + elem['src']
        elif elem.get('href'):
            elem['href'] = URL + elem['href']

    return soup.prettify()
