import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

class vicnews:
	def __init__(self, url):
		self.url = url
		self.topic = None
		self.story_link = None
		self.dict = {}

	def news_page(self):
		headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
		page = requests.get(self.url, headers=headers)
		soup = BeautifulSoup(page.text, 'html.parser')
		top_story = soup.find('div', attrs={'class':'large-8 columns'})
		self.topic = top_story.a.get_text()
		self.story_link = top_story.a['href']

		# Below code is to fetch other latest news links
		latest = soup.find(class_='story-list hero')
		for a in latest.find_all('a', href=True):
			latest_title = a.get_text()
			latest_link = a['href']
			self.dict[latest_title] = latest_link
		return(self.topic, self.story_link, self.dict)

@app.route('/')
def get_news():
	news=vicnews("https://vicnews.com")
	news.news_page()
	return render_template('page.html', topic=news.topic, story_link=news.story_link, latest_link='Further latest news links coming up')

if __name__=='__main__':
	app.run(host='0.0.0.0')