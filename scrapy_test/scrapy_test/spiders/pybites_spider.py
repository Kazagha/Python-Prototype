import scrapy

class PybitesSpider(scrapy.Spider):
    name = "pybites_spider"
    start_urls = [
        'http://pybit.es/'
    ]

    def parse(self, response):
        for article in response.css('article'):
            yield {
                'title' : article.css('h2 a::text').extract(),
                'tags'  : article.css('a~ a+ a::text').extract()
            }

if __name__ == '__main__':
    pass

# Article
# response.css('article')

# Article Title
# article.css('h2 a::text').extract()

# Extract Tags
# article.css('a~ a+ a::text').extract()