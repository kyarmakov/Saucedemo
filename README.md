Автоматический e2e тест для проверки сценария покупки товара на сайте [saucedemo.com](https://www.saucedemo.com/) с использованием Python и Playwright.

Для запуска теста на Вашем компьютере должен быть установлен git, Python версии не ниже 3.4 и менеджер пакетов pip.
Чтобы убедиться, что Python установлен на Вашем компьютере, Вы можете выполнить команду ```python --version``` для Windows и ```python3 --version``` для Linux и Mac.

Порядок запуска:
1) Открыть консоль (командную строку на Windows) и клонировать проект ```git clone https://github.com/kyarmakov/Saucedemo.git```
2) Перейти в папку проекта ```cd Saucedemo```
3) Создать виртуальное окружение для избежания конфликтов версий ```python -m venv myvenv``` для Windows и ```python3 -m venv myvenv``` для Linux и Mac.
   Python 3 обычно уже включает модуль `venv`, который позволяет создавать виртуальные окружения. Если по какой-то причине он не установлен, Вы можете установить Python, содержащий `venv`, через пакетный менеджер:
   ```sudo apt-get update``` и ```sudo apt install python3-venv``` для Ubuntu/Debian.
   
5) Активировать виртуальное окружение. Для Windows ```myvenv\Scripts\activate``` . Для Linux/Mac ```source myvenv/bin/activate```
6) Установить Playwright ```pip install playwright```
7) Установить плагин Pytest для Playwright ```pip install pytest-playwright```
8) Установить браузеры ```playwright install```
9) Выполнить команду ```pytest``` для запуска теста.

В файле pytest.ini содержатся настройки запуска теста.
При возникновении ошибок при установке пакетов обновите pip.
