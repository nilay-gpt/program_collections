# coding: utf-8
from BeautifulSoup import BeautifulSoup
import urllib2
import json
import timeit


def movie_list():
    # search = "2018_in_film"
    start = timeit.default_timer()
    name_list = []
    count = 1
    c1 = 1
    link = ['List_of_Bollywood_films_of_2018', '2018_in_film']
    for i in link:
        url = "https://en.wikipedia.org/wiki/" + i
        data = urllib2.urlopen(url)
        soup = BeautifulSoup(data.read())
        page = soup.findAll("table", {'class': 'wikitable sortable'})
        if len(page) == 0:
            print '++++++++++ taking the wikitable as search++++++'
            page = soup.findAll("table", {'class': 'wikitable'})
        for tag in page:
            name = tag.findAll('i')
            for movie in name:
                name_list.append(movie.text)
        name_list = list(set(name_list))

    for movie in name_list:
        movie = movie.replace(" ", "+")
        base_url = "http://www.omdbapi.com/?t="
        url = base_url + movie + '&y=&plot=short&r=json'
        try:
            data = urllib2.urlopen(url)
            soup = BeautifulSoup(data.read())
            text = json.loads(soup.text)
            try:
                print 'movie=', text['Title'], 'date==', text['Released'], 'ratings=', text['imdbRating'], '/10'
            except:
                count += 1
                pass
        except:
            c1 += 1
            pass
    stop = timeit.default_timer()
    print 'volllllaaaa the time is here ------->', stop - start
    print 'total movies--', len(name_list)

    print '-----due to fail in 1st reason-----', count
    print '---due to url open problem----', c1


if  __name__=="__main__":
    movie_list()
