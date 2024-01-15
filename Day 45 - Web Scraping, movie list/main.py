from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

with open("./movies.txt", "w", encoding="utf-8") as movie_list:
    article_titles = []
    titles = soup.findAll(name="h3", class_="title")
    for title in titles:
        article_titles.append(title.getText())
    article_titles.reverse()
    for movie in article_titles:
        movie_list.write(movie + f"\n")

