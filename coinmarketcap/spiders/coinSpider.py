import scrapy

class CoinSpider(scrapy.Spider):
    name = "coin"

    def start_requests(self):
        url = "https://coinmarketcap.com/all/views/all/"
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for row in response.css("tbody tr"):
            yield {
                "name": row.css("a.currency-name-container::text").extract_first(),
                "symbol": row.css("td.col-symbol::text").extract_first(),
                "market_cap": row.css("td.market-cap::text").extract_first(),
                "price": row.css("a.price::attr(data-usd)").extract_first(),
                "circulating_supply": row.css("td.circulating-supply span::attr(data-supply)").extract_first(),
                "volume": row.css("a.volume::attr(data-usd)").extract_first()
            }