Basic idea of this repo: This repo includes a python based application code, which can scrape news from specified websites and display it in a aggregated way.

This was mainly initiated since we plan to use this in our home automation system wherein we would like to view the relevant news highlights from multiple sites on a home tab.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The code makes use of 3 main python modules:

1) Flask to serve a webpage
2) requests to access the specified website and get the page contents
3) BeautifulSoup using which we can scrape desired content from the available data.

To run, you can simply execute the app.py file. You will need to have a template that will be rendered inorder to serve your scrapped data in specified manner.

Note: This code involves scraping for a specific news website. Based on the website of your choice, you might need to employ slightly different logic and bs4 attributes in order to scrape desired content.

This repo is still in progress as I plan to add following:

1) Few more websites to scrape the news update from.
2) A logic to automatically check for updates/change in news.
3) Store past few updates for the day that can be accessed.