# import scrapy


# class AmazonSpider(scrapy.Spider):
#     name = "Amazon"
#     page_number = 2
#     start_urls = [
#         "https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172504&qid=1671468709&ref=sr_pg_1"
#     ]

#     def parse(self, response):

#         for products in response.css("div.sg-col-inner"):

#             yield {
#                 "name": products.css("span.a-size-base-plus::text").get(),
#                 "price": products.css("span.a-offscreen::text").get(),
#             }

#             next_page = (
#                 "https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172504&page="
#                 + str(AmazonSpider.page_number)
#                 + "&qid=1671398595&ref=sr_pg_2"
#             )
#             if AmazonSpider.page_number < 148:
#                 AmazonSpider.page_number += 1
#                 yield response.follow(next_page, callback=self.parse)
#                 # after def.parse mathod it will automatically look for  respnose.follow function.response.follow needs 2 parameter (where should it go,what should do after go to the next page)


import scrapy

from ..items import AmazonScrapyItem

class AmazonSpider(scrapy.Spider):
    name = "Amazon"
    start_urls = [
        "https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172504&qid=1671435197&ref=sr_pg_1"
    ]

    def parse(self, response):

        products = AmazonScrapyItem()
        name = response.css(".a-size-base-plus::text").extract()
        reviws = response.css(".s-underline-text::text").extract()
        products ["p_name"] =name
        products["review"] =  reviws
        yield products
       
        

        # for allProducts in response.css("div.sg-col-inner"):

            

        #     yield {
        #         "name": allProducts.css("span.a-size-base-plus::text").get(),
        #         "price": allProducts.css("span.a-offscreen::text").get(),
        #         "rating":allProducts.css("span.a-icon-alt::text").get(),
        #         "image_url":allProducts.css("img.s-image::attr(src)").get()


        #     }
   
 
        # next_page = response.css(".s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator::attr(href)").get()
        # if next_page is not None:
        #   yield response.follow(next_page, callback=self.parse)
           