from abc import abstractmethod
from os import DirEntry
from typing import overload
from bs4 import BeautifulSoup
import requests
import re
import csv
#import pandas

class Scrapper:

    @staticmethod
    def getUrlSoup(url):
        netflixHTML = requests.get(url)
        soup = BeautifulSoup(netflixHTML.text, 'html.parser')
        return soup

    def getTitle(self,url):
        soup = self.getUrlSoup(url)
        return soup.find('h1').string

    def getGenres(self,url):
        soup = self.getUrlSoup(url)
        rawGenres = soup.find_all('span', class_='item-genres')
        genreList = []
        for genre in rawGenres:
            genreList.append(genre.text.split(',')[0])
        return genreList

    def getYear(self,url):
        soup = self.getUrlSoup(url)
        estreno = soup.find('span', class_="item-year").string
        return estreno

    def getCast(self,url):
        soup = self.getUrlSoup(url)
        cast = soup.find('div',class_='item-starring').find('span',class_='title-data-info-item-list').string.split(',')
        return cast
    
    def getLink(self,url):
        return url
    
    def getDescription(self,url):
        soup = self.getUrlSoup(url)
        desc = soup.find('div',class_='title-info-synopsis').string
        return desc
    
    def getMaturity(self,url):
        soup = self.getUrlSoup(url)
        maturity = soup.find('span', class_="maturity-number").string
        return maturity
            

class Show(Scrapper):

    def getLinks(genre):
        #Obtiene el link de cada serie en un genero
        return

    def getCantTemporadas(self,url):
        netflixHTML = requests.get(url)
        src = netflixHTML.content
        soup = BeautifulSoup(src, 'html.parser')
        temporadas = soup.find_all('div', class_="season")
        return len(temporadas)

    def getDirector(self,url):
        soup = self.getUrlSoup(url)
        directors = soup.find('div',class_="item-creators").find('span',class_="title-data-info-item-list").string
        return directors

class Movie(Scrapper):
    def getLinks(genre):
        #Obtiene el link de cada Pelicula en un genero
        return

    #Siquiera tiene directores?
    def getDirector(self,url):
        soup = self.getUrlSoup(url)
        directors = soup.find_all('div',class_="item-creators")
        return directors
 
if __name__ == "__main__":
    #Apertura del archivo CSV
    csvFile = open('netflix_catalog.csv','w')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['Titulo', 'Año de Estreno', 'Director', 'Actores', 'URL', 'Descripcion','Generos','Rating','Tipo'])
    
    #Orden de scrapeo:
    #   Se inicia sesion con selenium
    #   Se navega hasta la parte de Peliculas/Series
    #   Se obtiene el link de cada genero de pelicula/serie.
    movieGenres = []
    showGenres = []

    #   Se obtiene el link de cada pelicula/serie por genero(Son sets para no tener repetidas).
    movieLinks = {}
    showLinks = {}

    for genre in movieGenres:
        #links.append(Movies.getLinks(genre)) con selenium y requests
        exit

    for genre in showGenres:
        #links.append(Show.getLinks(genre)) con selenium y requests
        exit
        
    for link in movieLinks:
        #Movie.getAllAndSave(link,file)---> procuprar asignar el tipo y la url en esta funcion
        exit
    
    for link in showLinks:
        #Show.getAllAndSave(link,file) ---> procuprar asignar el tipo y la url en esta funcion
        exit

    csvFile.close()



#Testeo Manual

#print(Scrapper.getGenres('https://www.netflix.com/watch/80175798?tctx=1%2C0%2C%2C%2C%2C'))
#print(Scrapper().getGenres('https://www.netflix.com/title/70155589'))
#print(Show().get_cant_temporadas('https://www.netflix.com/title/70242311'))

#with open("pelicula2.txt", mode='w', encoding='UTF-8') as f:
#    f.write(str(Scrapper.getUrlSoup('https://www.netflix.com/title/80196789')))

#Series

#Creadores
desencanto = 'https://www.netflix.com/title/80095697'
print(Show().getDirector(desencanto))

#Elenco
print(Show().getCast(desencanto))

#Descripcion
print(Show().getDescription(desencanto))

#Maturity
print(Show().getMaturity(desencanto))


#Peliculas

#Creadores
birdBox = 'https://www.netflix.com/title/80196789'
print(Movie().getDirector(birdBox))

#Elenco
print(Movie().getCast(birdBox))

#Descripcion
print(Show().getDescription(birdBox))

#Maturity
print(Show().getMaturity(birdBox))