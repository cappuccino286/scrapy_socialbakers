# scrapy_socialbakers

## Description
* A scrapy project to scrape top 50 Brands - Facebook pages from Socialbakers.com

## Extracted data
* The extracted data looks like this sample:
```
    {
        "pos": "1",
        "brand_name": "Air France",
        "url_page": "https://www.facebook.com/airfrance/",
        "image_urls": ["https://scontent.xx.fbcdn.net/v/t1.0-1/p200x200/21370945_10159206772650526_1490209162810591076_n.jpg?oh=6b880cea37f004e1ccfa853c96040ace&oe=5AC53533"]
    }
```

## Spiders
By default, this spider extract top 50 brands in France. However, it can receive argument "country" that extract top 50 brands in a country specific.

    $ scrapy crawl topbrand
    $ scrapy crawl topbrand -a country=vietnam
    

## Author
* Sy Hung NGHIEM - University of Technology of Troyes
