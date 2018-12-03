import requests
import os
import sys
import json
import bs4


os.system('clear')


status=open('info.txt','a')



def info_movie(name):
    try:
    	t = name.replace(' ','%20')
    	url = 'https://api.themoviedb.org/3/search/movie?api_key=ffb07b773769d55c36ccd83845385205&language=en-US&query='+str(t)+'&page=1&include_adult=false'
    	response = requests.get(url)
    	u = json.loads(response.text)
    	results  = u['results']
    	id = results[0]['id']
    	url2 = 'https://api.themoviedb.org/3/movie/'+str(id)+'?api_key=ffb07b773769d55c36ccd83845385205&language=en-US'
    	response = requests.get(url2)
    	w = json.loads(response.text)
    	l=[]
    	title = w['title']
    	imdb_id = w['imdb_id']
    	year = w['release_date']
    	genre = w['genres']
    	language = w['spoken_languages']
    	duration = w['runtime']
    	plot = w['overview']
    	url3 = 'http://www.imdb.com/title/'+str(imdb_id)
    	response = requests.get(url3)
    	html = response.text
    	soup = bs4.BeautifulSoup(html,"lxml")
    	data = soup.select('.ratingValue')
    	rating = data[0].get_text('',strip=True)
    	l=[title, rating, year, str(duration), genre[0]['name'], plot]
    	status.write ("\n\n--------------------------------------MOVIE INFORMATION---------------------------------\n")
    	status.write ("\n\t TITLE       : \t\t"+title)
    	status.write ("\n\t IMDB RATING : \t\t"+rating)
    	status.write ("\n\t RELEASED ON : \t\t"+year)
    	status.write ("\n\t DURATION    : \t\t"+str(duration)+" mins")
    	# status.write ("\n\t LANGUAGE    : \t\t"+language[0]['name'])
    	status.write ("\n\t GENRE       : \t\t"+genre[0]['name'])
    	status.write ("\n\t PLOT        : \t\t"+plot)
    	return l
    except:
        print "\nNo such movie titled '"+name+"' found!\n"
        status.write ("\nNo such movie titled '"+name+"' found!\n")
    
    
def top_movies(x):
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html,"lxml")
    rows = soup.select('.lister-list tr')
    status.write ("\n"+"---------------------------TOP "+str(x)+" MOVIES ACCORDING TO IMDB RATINGS-----------------------------"+"\n\n")
    status.write (" \t   TITLE\t\t\t\t\t\t\t\t\t\t   IMDB RATING\n\n")
    l=[]
    for row in range(0,x):
        tdata=rows[row].select('td')
        name=tdata[1].get_text(' ',strip=True)
        rating=tdata[2].get_text(' ',strip=True)
        ans=("\n "+name.ljust(75,' ')+"\t\t\t\t"+rating+"\n")
        ans=ans.encode('ascii','ignore')
        l1=[name, rating]
        l.append(l1)
        status.write (ans)
    return l
        
        
def folder(path):
    dirs = os.listdir(path)
    status.write ('Showing results for the path: '+path+'\n')
    l=[]
    for i in range(len(dirs)):
    	try:
    		x = dirs[i]
    		t = x.replace(' ','%20')
    		url = 'https://api.themoviedb.org/3/search/movie?api_key=ffb07b773769d55c36ccd83845385205&language=en-US&query='+str(t)+'&page=1&include_adult=false'
    		response = requests.get(url)
    		u = json.loads(response.text)
    		results  = u['results']
    		id = results[0]['id']
    		url2 = 'https://api.themoviedb.org/3/movie/'+str(id)+'?api_key=ffb07b773769d55c36ccd83845385205&language=en-US'
    		response = requests.get(url2)
    		w = json.loads(response.text)
    		title = w['title']
    		year = w['release_date']
    		imdb_id = w['imdb_id']
    		url3 = 'http://www.imdb.com/title/'+str(imdb_id)
    		response = requests.get(url3)
    		html = response.text
    		soup = bs4.BeautifulSoup(html,"lxml")
    		data = soup.select('.ratingValue strong span')
    		rating = data[0].get_text('',strip=True)
    		x = x.encode('ascii','ignore')
    		y = "["+rating+"] "+title+" ("+year+")"
    		y = y.encode('ascii','ignore')
    		l.append(y)
    		status.write ("\n"+y)
    		os.rename(os.path.join(path, x), os.path.join(path, y))			
    		status.write ('Renaming Done\n')
    	except:
			l.append("AABB"+x)
			status.write ("\nNo such movie titled '"+x+"' found else read the instructions before using this feature!\n")
	return l
            
