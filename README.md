Created a Webscrapper using Scrapy

Scrapped this lovely site [Books to Scrape](https://books.toscrape.com/)

1) Checked the HTML divs to obtain information about 1 book
2) Automated this for all books in a page
3) Handled all irregular links, that is, change in structure of links
4) Traversed all pages to obtain all books from the site
5) Stored it in a JSON file

How to run?

Install `Scrapy` using pip. Other required dependencies will be automatically installed 

Run the scrapper by:

```bash
scrapy crawl bookspider
```

Things to do in the future:

1) Add multiple user agents to avoid detection
2) Store to a database
3) Not sure what?
