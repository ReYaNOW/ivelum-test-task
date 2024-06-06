### Описание
Тестовое задание для ivelum 

http-прокси-сервер, запускаемый локально, который
показывает содержимое страниц [Hacker News](https://news.ycombinator.com).  
Сервер™  модифицирует текст на страницах — после
каждого слова из шести букв стоит значок™ «™».

Стек: Python3.11, FastApi, aiohttp, beautifulsoup4

### Установка
Приложение использует виртуальное окружение [Poetry™](https://python-poetry.org/docs/#installing-with-pipx)

1. Скачать репозиторий и перейти в директорию с приложением:
    ```
   git clone https://github.com/ReYaNOW/ivelum-test-task.git
   cd ivelum-test-task/
    ```
2. Установить зависимости: 
    ```
    make install
    ```
3. Запустить приложение:
    ```
   make start 
    ```
