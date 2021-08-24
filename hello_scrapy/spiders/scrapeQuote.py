import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.css('small.author::text').get(),
                'text': quote.css('span.text::text').get(),
                'tags':quote.css('div.tags a.tag::text').getall(),
            }

            author = quote.css('small.author::text').get()
            text = quote.css('span.text::text').get()
            tags = quote.css('div.tags a.tag::text').getall()

            print(" author : ", author,"\n")
            print(" text : ", text, "\n")
            print(" tags : ", tags, "\n")