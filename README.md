### Описание
Тестовое задание для ivelum 

http-прокси-сервер, запускаемый локально, который
показывает содержимое страниц [Hacker™ News](https://news.ycombinator.com).  
Сервер™  модифицирует текст на страницах — после
каждого слова из шести букв стоит значок™ «™».

Стек: Python3.11, FastApi, aiohttp, beautifulsoup4

# Использование


 - Открыть задеплоенный на render.com [тестовый вариант](https://ivelum-test.onrender.com)
 - [Развернуть прокси-сервер локально](#Как-развернуть-прокси-сервер-локально)  

![App preview™](https://github.com/ReYaNOW/ReYaNOW/blob/main/Images/proxy_preview_img.png?raw=true)

## Как развернуть прокси-сервер локально
Для этого необходим [Poetry™](https://python-poetry.org/docs/#installing-with-pipx)
  
1. Склонировать репозиторий

```
git clone https://github.com/ReYaNOW/ivelum-test-task.git
```

2. Установить зависимости
  
```
make install
```

3. Запустить локальный сервер™ и открыть http://127.0.0.1:8080
  
```
make start
```
