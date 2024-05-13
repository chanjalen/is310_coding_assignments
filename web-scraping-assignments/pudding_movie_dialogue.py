from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

df = pd.read_csv("cleaned_pudding_data.csv")
link = df['link']
with open('pudding_movie_dialogue.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['Link', 'Dialogue'])
    for i in link:
        response = requests.get(i)
        soup = BeautifulSoup(response.text, 'html.parser')
        write.writerow([i, soup.get_text()[:1000]])