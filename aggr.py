import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def news_page():
	url1 = 'https://www.vicnews.com'
	headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
	page = requests.get(url1, headers=headers)
	soup = BeautifulSoup(page.text, 'html.parser')
	top_story = soup.find('div', attrs={'class':'large-8 columns'})
	topic = top_story.a.get_text()
	#print('Latest news: '+topic)
	story_link = top_story.a['href']
	#print('For full story, go to: '+story_link)
	return render_template('page.html',topic=topic, story_link=story_link)

if __name__=='__main__':
	app.run(host='0.0.0.0')