import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=URL)
content = response.text

soap = BeautifulSoup(content, "html.parser")
list_movies = soap.find_all(name="h3", class_="title")

name_movies = [title.getText() for title in list_movies]


with open("movies.txt", mode="a", encoding='utf-8') as movies:
    for n in range(99, -1, -1):
        print(name_movies[n])
        movies.write(f"{name_movies[n]}\n")
