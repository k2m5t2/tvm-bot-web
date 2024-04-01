import scrapy
from scrapy_playwright.page import PageMethod

class DiscussSpider(scrapy.Spider):
    name = 'discuss'
    start_urls = ['https://meta.discourse.org/']

    async def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods=[
                        PageMethod('wait_for_selector', 'a.title.raw-link.raw-topic-link')
                    ]
                ),
            )

    async def parse(self, response):
        page = response.meta['playwright_page']
        titles = await page.query_selector_all('a.title.raw-link.raw-topic-link')
        for title in titles:
            text = await title.text_content()
            print(text)
        await page.close()
