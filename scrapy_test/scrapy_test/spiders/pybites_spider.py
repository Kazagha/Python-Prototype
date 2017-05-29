import scrapy

class PybitesSpider(scrapy.Spider):
    name = "pybites_spider"
    start_urls = [
        'http://pybit.es/',
        'http://pybit.es/index2.html'
    ]

    def parse(self, response):
        for article in response.css('article'):
            yield {
                'title' : article.css('h2 a::text').extract_first(),
                'tags'  : article.css('a~ a+ a::text').extract()
            }

        self.log('Finished scraping articles')

        next_page = response.css('.btn:nth-child(1)::attr(href)').extract_first()
        if next_page is not None:
            # In the example the URL is build using this command
            # However the full URL is present here
            #next_page = response.urljoin(next_page)
            self.log(f'Moving to the next page {next_page}')
            yield scrapy.Request(next_page, callback=self.parse)

if __name__ == '__main__':
    pass

# Article
# response.css('article')

# Article Title
# article.css('h2 a::text').extract()

# Extract Tags
# article.css('a~ a+ a::text').extract()

# Older Posts Button
# response.css('.btn:nth-child(1)::attr(href)').extract()