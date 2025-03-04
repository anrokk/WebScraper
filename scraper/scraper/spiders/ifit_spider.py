import scrapy


class IfitSpider(scrapy.Spider):
    name = "ifit_spider"
    allowed_domains = ["ifit.ee"]
    start_urls = ["https://www.ifit.ee/et/c/proteiinid?page=1"]

    def parse(self, response, **kwargs):
        products = response.css("div.src-product-3")

        for product in products.getall():
            yield {
                "Title": product.css("a.title::text").get().strip(),
                "Price": product.css("div.price::text, strong.price::text").get().strip(),
                "Picture href": product.css("a.img-wrap img::attr(src)").get()
            }

        current_page = int(response.url.split("page=")[-1])
        if current_page < 8:
            next_page = f"https://www.ifit.ee/et/c/proteiinid?page={current_page + 1}"
            yield response.follow(next_page, callback=self.parse)
