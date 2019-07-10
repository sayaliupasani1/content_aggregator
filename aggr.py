import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

class vicnews:
	def __init__(self, url):
		self.url = url
		self.topic = None
		self.story_link = None

	def news_page(self):
		print('This is within news_page')
		headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
		page = requests.get(self.url, headers=headers)
		soup = BeautifulSoup(page.text, 'html.parser')
		top_story = soup.find('div', attrs={'class':'large-8 columns'})
		self.topic = top_story.a.get_text()
		self.story_link = top_story.a['href']
		print('exiting class')
		return(self.topic, self.story_link)

@app.route('/')
def get_news():
	news=vicnews("https://vicnews.com")
	news.news_page()
	return render_template('page.html', topic=news.topic, story_link=news.story_link)

if __name__=='__main__':
	app.run(host='0.0.0.0')