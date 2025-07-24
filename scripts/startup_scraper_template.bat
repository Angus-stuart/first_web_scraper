:: This is a batch script to run your web scraper using your virtual environment.
:: Replace "C:\Webscraper" below with the full path to your own project folder.

cd C:\Webscraper
call .venv\Scripts\activate.bat
python src\main.py