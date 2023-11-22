import requests
from bs4 import BeautifulSoup
import sqlite3
import time

conn = sqlite3.connect('https://www.weather.com/city/Zaporizhzhia')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS weather_data (date TEXT, temperature REAL)''')

    response = requests.get('https://www.weather.com/city/Zaporizhzhia')
    soup = BeautifulSoup(response.text, 'html.parser')
    temperature = soup.find('div', {'class': 'temperature'}).text

    c.execute("INSERT INTO weather_data (date, temperature) VALUES (?, ?)", (time.strftime('%Y-%m-%d %H:%M:%S'), temperature))

    conn.commit()

    time.sleep(1800)

c.execute("SELECT * FROM weather_data")
for row in c.fetchall():
    print(row)
