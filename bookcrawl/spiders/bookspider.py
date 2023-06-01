import scrapy
from bookcrawl.items import ClassBook

url = "http://books.toscrape.com/"


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        yield response.follow(response.url, callback=self.page_parse)

    def page_parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            rel_url = book.css('h3 a::attr(href)').get()
            # print(rel_url+"Hello")
            if 'catalogue/' not in rel_url:
                rel_url = 'catalogue/'+rel_url
            # print(rel_url)
            book_url = url + rel_url
            # print(book_url)
            yield response.follow(book_url, callback=self.book_parse)

        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            if 'catalogue/' not in next_page:
                next_page = 'catalogue/'+next_page
            next_url = url + next_page
            yield response.follow(next_url, callback=self.page_parse)

    def book_parse(self, response):
        # print(response.url)
        table = response.css("table tr")
        book = ClassBook()

        book['url'] = response.url
        book['title'] = response.css('.product_main h1::text').get()
        book['upc'] = table[0].css("td::text").get()
        book['product_type'] = table[1].css("td::text").get()
        book['price_excl_tax'] = table[2].css("td::text").get()
        book['price_incl_tax'] = table[3].css("td::text").get()
        book['tax'] = table[4].css("td::text").get()
        book['availability'] = table[5].css("td::text").get()
        book['num_reviews'] = table[6].css("td::text").get()
        book['stars'] = response.css("p.star-rating").attrib['class']
        book['category'] = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()
        book['description'] = response.xpath(
            "//div[@id='product_description']/following-sibling::p/text()").get()
        book['price'] = response.css('p.price_color ::text').get()

        yield book
